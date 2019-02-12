### CTF

First, go to the Members page of the website. You are asked to enter a member's id in order to find their profile. By doing so, you should get a result that looks very much liek this:

    ID: 1 
    First name: Barack Hussein
    Surname : Obama

Now, we test if the queries are vulnerable to SQL injections. Indeed, a simple injection (eg. '105 OR 1=1') allows us to see all registered members. One is particularly interesting, as it is called "GetTheFlag". We now want to retrieve as much data as possible using SQL queries.

A quick request tell us that we are dealing with a MySql database. The correct syntax to retrieve all sensitive information is:

    1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns

(Note that we know information_schema has two columns based on further investigation.)

The table_name "users" has "first_name", "last_name", "town", "country", "planet", "Commentaire" and "countersign" columns.

    ID: 1 AND 1=2 UNION SELECT Commentaire, countersign FROM users 
	First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
	Surname : 5ff9d0165b4f92b14994e5c685cdce28

We simply follow the given instructions: the password is **fortytwo**

### How to protect yourself
