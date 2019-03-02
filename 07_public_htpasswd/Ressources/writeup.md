### CTF

We were able to fetch a direcotry map of the http server by executing this command:
```bash
wget -r -R '*index.(html|php)*' ${SEVER_IP}
```

By doing this we noticed that we had access to the `.htpasswd` used by the `.htaccess` that protects the access of many pages like the admin page.  
The file was located in `/whatever/.htpasswd`

As passwords in `.htpasswd` are encrypted in base64, we were able to decrypt it to find that the password is `dragon`.

### How To Protect Yourself

#### Main Solutions

You could simply put the `.htpasswd` in a `.htaccess` protected directory, so that the file is only accessible if the password is known.  

Another solution would be to configure the web server to deny access to those files. On an Apache server you would have to add those lines to your configuration:
```
<FilesMatch "^.(htaccess|htpasswd)$">
	Order Allow,Deny
	Deny from all
</FilesMatch>
```

