import base64
import hashlib
import os
import string
import subprocess
from secrets import token_urlsafe
from docopt import docopt
import pyperclip
import keyring


class PwManager():
    """
  Minimalist Password manager / generator, using Keyring.

  Usage: pwman.py <url> <loginname> [-g] | [-hvd]

  Options:

    -g, --generate          Generate and store new password.
    -d, --dump-masterkey    Show masterkey.
    -h, --help              Show this screen.
    -v, --version           Show version.
    """

    def __init__(self):
        self.name = "pypwmanager"
        self.init_keyring()

    def init_keyring(self):
        self.keyring = keyring.get_keyring()
        m = self.keyring.get_password(self.name, 'masterkey')
        if not m:
            m = token_urlsafe(32)
            print('...new masterkey: {}'.format(m))
            self.keyring.set_password(self.name, 'masterkey', m)
        self.masterkey = m

    def lookup(self, url, username):
        return self.keyring.get_password(url, username)

    def showkey(self):
        key = self.lookup(self.name, 'masterkey')
        return key

    def generate_pw(self, url, username):
        if self.lookup(url, username):
            print('Entry already exists.')
            exit()

        url = url.strip()
        if len(url) < 5:
            print('Not a valid url.')
            exit()
        if username:
            s = hashlib.sha256(username.encode() +
                               self.masterkey.encode() + url.encode())
        else:
            s = hashlib.sha256(self.masterkey.encode() + url.encode())
        S = base64.b64encode(bytes.fromhex(s.hexdigest())).decode('utf-8')
        return S


if __name__ == '__main__':
    pwman = PwManager()
    args = docopt(pwman.__doc__, version='0.3')
    url = args.get('<url>', '')
    loginname = args.get('<loginname>')

    if args.get('--generate'):
        pw = pwman.generate_pw(url, loginname)
        if pw:
            pwman.keyring.set_password(url, loginname, pw)
        exit()


    if args.get('--dump-masterkey'):
        s = pwman.showkey()
        if s:
            print('Masterkey:')
            print(s)
        else:
            print('No masterkey available')


    if args.get('<url>') and args.get('<loginname>'):
        entry = pwman.lookup(url, loginname)
        if entry:
            entry = entry if entry else ''
            if args.get('--print'):
                print(entry)
            else:
                pyperclip.copy(entry)
                print('Password has been copied to the clipboard.')
                import subprocess
                subprocess.Popen(os.getcwd() + '/clear_clipboard.py')
        else:
            print('No entry found for: {} - {}'.format(url, loginname))
