import unittest
import base64
import hashlib
from pwman  import PwManager

import tracemalloc
tracemalloc.start()


class TestPwManager(unittest.TestCase):
    def setUp(self):
        self.pwman = PwManager()
        self.pwman.test = True
        self.pwman.name = "test_pypwmanager"
        self.pwman.init_keyring()

    def test_getname(self):
        self.assertEqual(self.pwman.name, 'test_pypwmanager')

    def test_show_masterkeykey(self):
        self.assertEqual(self.pwman.showkey(), self.pwman.masterkey)

    def test_generate_pw(self):
        url = 'htpps://testpypwmanager.com'
        loginname = 'some_username'
        pw = self.pwman.generate_pw(url, loginname)
        if not pw is False:
            r = self.pwman.keyring.set_password(url, loginname, pw)

    def test_lookup_false(self):
        r = self.pwman.lookup('hgfdsfds.com', 'username')
        self.assertEqual(r, False)

    def test_lookup_false(self):
        r = self.pwman.lookup('hgfdsfds.com', 'username')
        self.assertEqual(r, None)

    def test_lookup(self):
        url = 'htpps://testpypwmanager.com'
        loginname = 'some_username'
        r = self.pwman.lookup(url, loginname)
        s = hashlib.sha256(loginname.encode() +
                           self.pwman.masterkey.encode() + url.encode())
        S = base64.b64encode(bytes.fromhex(s.hexdigest())).decode('utf-8')
        self.assertEqual(r, S)


if __name__ == '__main__':
    unittest.main()
