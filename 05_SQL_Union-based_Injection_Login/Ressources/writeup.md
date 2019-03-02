### CTF

Once again, we will be using SQL injections in order to capture the flag. We are however going to go through a slightly different method. But first, got to the Members page.

We have already noticed the `db_default` contains two interesting pieces of information, `username` and `password`, in a previous exploit. However, injecting a request such as:
```
    1 AND 1=2 UNION SELECT username, password FROM db_defaut.columns
```
will return the following error:
```
    SELECT command denied to user 'borntosec'@'localhost' for table 'columns'
```
Finally, a request that requires user privilege! Fear not, there is simple way of getting around this issue. Let's look at the different table schemas via
```
    1 AND 1=2 UNION SELECT table_schema, table_name FROM information_schema.tables
```
The actual table is `Member_Brute_Force.db_default`, as `db_default belongs` to `Member_Brute_Force`. Simply type:
```
    1 AND 1=2 UNION SELECT username, password FROM Member_Brute_Force.db_default
```
There are merely two users, root and admin, which share the same password `shadow`. Enter one or the other logins at sign in and you've got yourself another flag.

### How to protect yourself

There are multiple solutions:
- One simple solution, and one of the most secured would be to use _prepared SQL requests_, meaning requests taking parameters.
Prepared requests' parameters are not interpreted as SQL, so you can't alter the initial request.
- Use of stored procedures, that is, creating an alias to a SQL request, this alias can take parameters.
However this solution is not fullproof, especially if it includes any unsafe dynamic SQL generation.
- You could also create a whitelist input validation. This can be useful if you expect different specific values.
- Another solution would be to escape all user inputs so they can't be interpreted as a request.
Of course you would not escape password inputs, you should hash them, because... who still stores clear passwords ?
