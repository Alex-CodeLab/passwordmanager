# passwordmanager
##### minimalist commandline passwordmanager using Keyring

Passwords are generated/derived using a 32 character masterkey .

Store the masterkey in a save place, so passwords can be re-generated if needed.


        Minimalist Password manager / generator, using Keyring.

        Usage: pwman.py <url> <loginname> [-g] | [-hvd]

        Options:

          -g, --generate          Generate and store new password.
          -d, --dump-masterkey    Show masterkey.
          -h, --help              Show this screen.
          -v, --version           Show version.


##### install
 - `pip install -r requirements.txt`

##### Examples:

Generate and lookup

      $ python pwman.py google.com  user@gmail.com -g     
      $ python pwman.py google.com  user@gmail.com
        Password has been copied to the clipboard.

      $ python pwman.py twitter.com testname  -g     
      $ python pwman.py twitter.com testname -p
        ZS5eSceE1fRuhE/RRkoqzrw9xvbbjyPYcKtthXQr1w=


##### Keyring
The system Keyring is used for storage.
See `keyring --help` for more info.

##### Roadmap:
0. Create tests.
1. Have a decent working commandline application.
2. Create a browser-plugin to request the login credentials.
3. Port to micro-python.
4. Run this app on some hardware usb device.  


##### Contribute.
Yes build whatever

Check [issues](https://github.com/Alex-CodeLab/passwordmanager/issues) for improvements, ideas, etc.
