### CTP

Much like the XSS exploit in the Feedback page, this page too is vulnerable to XSS filter evasion. This can be tested by changing the value of **src** with a malicious search query in this URL:

    http://IP_ADDRESS/?page=media&src=<script>alert('test');</script>

However, even though an alert window popped up, this is not the exact solution. Encrypt the query with base64.

    http://IP_ADDRESS/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdCcpOzwvc2NyaXB0Pg==

### How to protect yourself

There are multiple solutions:
1. [HTML/XML escape](https://www.w3.org/International/questions/qa-escapes#use) all user inputs so they can't be interpreted by the browser as HTML.
2. [Javascript escape](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.md#safe-and-functionally-correct-example) all user inputs so they can never be interpreted as javascript.
3. Be more careful when inserting untrusted data in event handlers. The fact that the query needed to be base64 encoded did not help. 
