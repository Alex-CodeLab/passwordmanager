# passwordmanager
##### minimalist commandline passwordmanager

Passwords are generated/derived using a 32 character masterkey (Make sure to change it!).

Store the masterkey in a save place, so passwords can be re-generated if needed.

Data is stored in a encrypted database.


        Usage: pwman.py <url> [-l <loginname>] [-g] | [-d] | <url> [-l <loginname>]

        Options:
            -d, --dump        Dump all.
            -g, --generate    Generate new password.
            -u, --url         Target url.
            -h, --help        Show this screen.
            -v, --version     Show version.


##### Examples:

Generate and lookup

      $ ./pwman.py google.com -l user@gmail.com -g     
      $ ./pwman.py google.com -l user@gmail.com
        XSFavSZqlcpPlYveYTa+ueaQwBvM1wUn6fNOfC3wqZ0=

      $ ./pwman.py twitter.com  -g     
      $ ./pwman.py google.com  
        ZS5eSceE9fRuhE/RRkoqzrw9xvbbjyPYcKtthXQr1w=



Check [issues](https://github.com/Alex-CodeLab/passwordmanager/issues) for improvements, ideas, etc.




##### Roadmap:
0. Create tests.
1. Have a decent working commandline application.
2. Create a browser-plugin to request the login credentials.
3. Port to micro-python.
4. Run this app on some hardware usb device.  
