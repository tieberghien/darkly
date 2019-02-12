### CTF

It is possible to insert a malicious string as the variable parameter to access files located outside the web publish directory. More specifically, the following URL shows example of *NIX password file exploitation:

    http://IP_ADDRESS/?page=../../../../../../../etc/passwd
