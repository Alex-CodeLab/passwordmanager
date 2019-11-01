# passwordmanager
##### minimalist commandline passwordmanager using Keyring

Generate passwords, store it in the system Keyring.
By default, when looking up a password, it is copied to the clipboard
(and removed from clipboard after 15seconds.)

Passwords are generated/derived using a 24 character masterkey .
Store the masterkey in a save place, so passwords can be re-generated if needed.


        Usage: pwman.py <url> <loginname> [-g] | [-hvdt]

        Options:

          -g, --generate          Generate and store new password.
          -d, --dump-masterkey    Show masterkey.
          -p, --print             Display password, do not copy to clipboard
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
- [X] Create tests.
- [X] Use Keyring
- [X] Have a decent working commandline application.
- [ ] Create a browser-plugin to request the login credentials.
- [ ] Use some USB device to unlock data


##### Contribute.
Yes, build whatever you want. Start with creating a ticket that describes the problem.

Check [issues](https://github.com/Alex-CodeLab/passwordmanager/issues) for improvements, ideas, etc.
