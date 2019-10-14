import base64
import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from docopt import docopt
import pyperclip


class PwManager():
    """
        Minimalist Password manager.

        Usage: pwman.py <url> [-l <loginname>] [-g] | [-d] | <url> [-l <loginname>] -p

        Options:
            -d, --dump        Dump all.
            -g, --generate    Generate new password.
            -p, --print       Print password to the terminal.
            -u, --url         Target url.
            -h, --help        Show this screen.
            -v, --version     Show version.
    """

    def __init__(self):
        self.db = []
        # 32 char key. replace with your own!
        self.masterkey = b'14XnLu3EQ6YZZwPbagdj8NV1kap1aL62'
        self.readdb()

    def readdb(self):
        if not os.path.isfile('db.txt'):
            self.create_db()
        a = []
        with open('db.txt', 'rb') as f:
            content = f.read()
            if content:
                content = self.decrypt(content)
                for line in content.split('\n'):
                    if len(line) > 2:
                        a.append(line.split(' '))
            self.db = a

    def create_db(self):
        print('Creating new password database...')
        f = open('db.txt', 'w+')
        f.close()

    def lookup(self, url, username=False):

        for row in self.db:
            if len(row) > 0:
                if row[0] == url:
                    if username:
                        if len(row) > 2:
                            if row[2] == username:
                                return row[1]
                    else:
                        return row[1]
        return False

    def generate_pw(self, url, username):
        url = url.strip()
        if len(url) < 5:
            print('Not a valid url.')
            exit()
        if username:
            s = hashlib.sha256(username.encode() +
                               self.masterkey + url.encode())
        else:
            s = hashlib.sha256(self.masterkey + url.encode())
        S = base64.b64encode(bytes.fromhex(s.hexdigest())).decode('utf-8')
        return S

    def add_pw(self, url, pw, loginname=False):
        if self.lookup(url, loginname) == False:
            if loginname:
                self.db.append([url, pw, loginname])
            else:
                self.db.append([url, pw])

    def encrypt(self, content):
        iv = get_random_bytes(16)
        cipher = AES.new(self.masterkey, AES.MODE_CFB, iv)
        ciphertext = cipher.encrypt(content)
        return iv + ciphertext

    def decrypt(self, ciphertext):
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]
        cipher = AES.new(self.masterkey, AES.MODE_CFB, iv)
        msg = cipher.decrypt(ciphertext)
        return msg.decode("utf-8")

    def save_db(self):
        content = ''
        for line in self.db:
            content = content + ' '.join(line) + '\n'
        content = self.encrypt(content)
        with open('db.txt', 'wb') as f:
            f.write(content)
            f.close()

    def dump_all(self):
        dump = []
        for line in self.db:
            if len(line) > 2:
                dump.append('{} {} {}'.format(line[0], line[2], line[1]))
            else:
                dump.append('{} {}'.format(line[0],  line[1]))
        return dump if len(dump) else False

if __name__ == '__main__':
    pwman = PwManager()

    args = docopt(pwman.__doc__, version='0.1')
    if args.get('--dump'):
        entries = pwman.dump_all()
        print(entries if entries else 'db empty ...')
        exit()

    url = args.get('<url>', '')
    loginname = args.get('<loginname>', '')

    if args.get('--generate'):
        pw = pwman.generate_pw(url, loginname)
        if pw:
            pwman.add_pw(url, pw, loginname)
            pwman.save_db()
        exit()

    if args.get('<url>'):
        entry = pwman.lookup(url, loginname)
        if entry:
            entry = entry if entry else ''
            if args.get('--print'):
                print(entry)
            else:
                pyperclip.copy(entry)
                print('Password has been copied to the clipboard.')
        else:
            print('No entry found for: {} - {}'.format(url, loginname))
