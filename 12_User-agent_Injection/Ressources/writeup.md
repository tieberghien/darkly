### CTF

Go to the @ BornToSec page, virtually at the bottom of every page. Inspect: there are comments written inside the HTML elements. Two comments are of particular interest:

	You must cumming from : "https://www.nsa.gov/" to go to the next step
	Let's use this browser : "ft_bornToSec". It will help you a lot.

This is a little cryptic, but the solution is fairly straight-forward. "ft_bornToSec" is the name of an user-agent and the NSA webpage is the __referer__ from which you want to connect to @ BornToSec page.

```bash
    curl -A "ft_bornToSec" --referer https://www.nsa.gov/ http://10.12.1.106/\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c
```

Simply grep the flag.

### How to protect yourself

Once again, no sanitize mechanism is in place.
There are multiple solutions:
1. [HTML/XML escape](https://www.w3.org/International/questions/qa-escapes#use) all user inputs so they can't be interpreted by the browser as HTML.
2. [Javascript escape](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.md#safe-and-functionally-correct-example) all user inputs so they can never be interpreted as javascript.
3. Be more careful when inserting untrusted data in event handlers.
