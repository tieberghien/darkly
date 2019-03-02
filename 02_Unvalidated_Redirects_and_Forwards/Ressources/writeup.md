### CTF

For this exploit, go to any page which contains links to 42's facebook, twitter and instagram (scroll down the bottom of the page). As we inspect the "redirect" form, we notice the link to the facebook page is

    <a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a>

Luckily for us, there is no redirect validation. This means we can forward users to any webpage. Needless to say this is a grave oversight, as any malicious user may manipulate cookies in order to redirect clueless users to a malicious webpage.

### How to protect yourself

Once again, the website is not protected against untrusted input. Here's a [link](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) to help you differentiate between safe and unsafe redirects: 
 
