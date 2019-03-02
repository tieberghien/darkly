### CTF

First, go to the Members page of the website. You are asked to enter a member's id in order to find their profile. By doing so, you should get a result that looks very much liek this:
```
    ID: 1 
    First name: Barack Hussein
    Surname : Obama
```
Now, we test if the queries are vulnerable to SQL injections. Indeed, a simple injection (eg. '105 OR 1=1') allows us to see all registered members. One is particularly interesting, as it is called "GetTheFlag". We now want to retrieve as much data as possible using SQL queries.

A quick request tell us that we are dealing with a MySql database. The correct syntax to retrieve all sensitive information is:

    1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns

(Note that we know `information_schema` has two columns upon further investigation.)

The table `users` has `first_name`, `last_name`, `town`, `country`, `planet`, `Commentaire` and `countersign` columns.
```
    ID: 1 AND 1=2 UNION SELECT Commentaire, countersign FROM users 
	First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
	Surname : 5ff9d0165b4f92b14994e5c685cdce28
```
We simply follow the given instructions: the password is `fortytwo`

### How to protect yourself

There are multiple solutions:
- One simple solution, and one of the most secured would be to use _prepared SQL requests_, meaning requests taking parameters.
Prepared requests' parameters are not interpreted as SQL, so you can't alter the initial request.
- Use of stored procedures, that is, creating an alias to a SQL request, this alias can take parameters.  
However this solution is not fullproof, especially if it includes any unsafe dynamic SQL generation.
- You could also create a whitelist input validation. This can be useful if you expect different specific values.
- Another solution would be to escape all user inputs so they can't be interpreted as a request.  
Of course you would not escape password inputs, you should hash them, because... who still stores clear passwords ?

