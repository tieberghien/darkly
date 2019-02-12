### CTP

Much like the XSS exploit in the Feedback page, this page too is vulnerable to XSS filter evasion. This can be tested by changing the value of **src** with a malicious search query in this URL:

    http://IP_ADDRESS/?page=media&src=<script>alert('test');</script>

However, even though an alert window popped up, this is not the exact solution. Encrypt the query with base64.

    http://IP_ADDRESS/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdCcpOzwvc2NyaXB0Pg==
