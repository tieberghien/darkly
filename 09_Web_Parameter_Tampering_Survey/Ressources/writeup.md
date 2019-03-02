### CTF

Let's say, for the sake of argument, you are Zaz. You are feeling very aggravated because you are coming last in the poll. Well, I have got good news for you. First, inspect the Survey page: each contender has got an id number (eg. Zaz is in 5th place, value=6). You may tamper with the id attached to any other contender, so any given votes increase your grade. You may also want the "real" value of each grade, from 1 to 10, to be much bigger than the voter think it is. Increase the grade value that will be used to calculate the mean value, and sip your beer to your heart's content, as you are slowly but surely winning the race. You truly are the most malevolent being to ever walk this earth.

### How to protect yourself

This request should be send to and checked by the back-end part of the website. There should never be a form out front. Cf. [example 2](https://www.owasp.org/index.php/Web_Parameter_Tampering) 
