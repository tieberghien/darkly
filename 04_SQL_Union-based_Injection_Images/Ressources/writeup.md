### CTF

The solution of this CTF is very much analogous to this of [Members Injection](../../03_SQL_Union-based_Injection_Members). Enter the following SQL request in the `Image number` field, found in the `Search image` page.
```
    1 AND 1=2 UNION SELECT title, comment FROM list_images
```
Follow the instruction. The password is `albatroz`

### How to protect yourself

There are multiple solutions:
- One simple solution, and one of the most secured would be to use _prepared SQL requests_, meaning requests taking parameters.
Prepared requests' parameters are not interpreted as SQL, so you can't alter the initial request.
- Use of stored procedures, that is, creating an alias to a SQL request, this alias can take parameters.
However this solution is not fullproof, especially if it includes any unsafe dynamic SQL generation.
- You could also create a whitelist input validation. This can be useful if you expect different specific values.
- Another solution would be to escape all user inputs so they can't be interpreted as a request.
Of course you would not escape password inputs, you should hash them, because... who still stores clear passwords ?
