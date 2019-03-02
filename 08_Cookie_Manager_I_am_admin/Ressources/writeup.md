### CTF

First, launch a cookie manager addon (for this example, we used Cookie Manager for Firefox) on any given page of the website. There is a single cookie named I_am_admin with an expiration date:

    I_am_admin=68934a3e9455fa72420237eb05902327

Said cookie has a 32-bit value; it very much ressembles the other md5 hashes we have already decoded. Decrypt it. Our intuition was correct, as the hashed value is "false". Then encode the string "true" and edit the original value of the cookie for the md5 version of said string.

    I_am_admin=b326b5062b2f0e69046810717534cb09

You now are the admin.

### How to protect yourself


