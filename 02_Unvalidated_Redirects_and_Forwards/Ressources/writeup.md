### CTF

For this exploit, go to any page which contains links to 42's facebook, twitter and instagram (scroll down the bottom of the page). As we inspect the "redirect" form, we notice the link to the facebook page is

    <a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a>

Luckily for us, there is no redirect validation. This means we can forward users to any malicious webpage.
