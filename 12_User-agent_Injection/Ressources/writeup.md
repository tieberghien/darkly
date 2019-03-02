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

Cookies should be checked server-side, and there should be a unique ID for each section. You should not be able to retrieve cookies pertaining to identifying the user.
