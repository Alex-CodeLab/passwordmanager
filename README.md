# passwordmanager
minimalist commandline passwordmanager

Passwords are generated/derived using a 32 character masterkey (Make shure to change it!).

Store the masterkey in a save place, so passwords can be re-generated if needed.



        Usage: pwman.py <url> [-l <loginname>] [-g] | [-d] | <url> [-l <loginname>]

        Options:
            -d, --dump        Dump all.
            -g, --generate    Generate new password.
            -u, --url         Target url.
            -h, --help        Show this screen.
            -v, --version     Show version.


Examples: 

Generate and lookup
    
      $ ./pwman.py google.com -l user@gmail.com -g     
      $ ./pwman.py google.com -l user@gmail.com 
        XSFavSZqlcpPlYveYTa+ueaQwBvM1wUn6fNOfC3wqZ0=
    
      $ ./pwman.py twitter.com  -g     
      $ ./pwman.py google.com  
        ZS5eSceE9fRuhE/RRkoqzrw9xvbbjyPYcKtthXQr1w=
    
      
