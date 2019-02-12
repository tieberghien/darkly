### CTF

It is possible to insert a malicious string as the variable parameter to access files located outside the web publish directory. More specifically, the following URL shows example of *NIX password file exploitation:

    http://IP_ADDRESS/?page=../../../../../../../etc/passwd

This kind of attack is possible only if the validation checkpoint fails. This means there is no Access Control Lists (ACL) which identify which users or groups are supposed to be able to access, modify, or execute a specific file on the server.

### How to protect yourself

For example you may follow the principle of least user access or least-privileged user account (LUA), the concept that all users and modules at all times should run with as few privileges as possible.
