### CTF

Thanks to the robots.txt file we recovered in a previous exploit, we now know there is a **.hidden** folder any user-agent can access. In order to find the relevant files amongst the thousands of README the folder contains, we wrote a folder scraping script:

    usage: ./scrap.sh IP_ADDRESS

One file stands out, as it merely contains a 32 character string, instead of a fairly derogatory sentence. Congratulations, this is our flag.

### How To Protect Yourself

You have to configure your server in order to disable directory listing. Here is an Nginx example:
```
server {
        listen   80;
        server_name  domain.com www.domain.com;
        access_log  /var/...........................;
        root   /path/to/root;
        location / {
                index  index.php index.html index.htm;
		autoindex off;
        }
}
```
[List of solutions](https://www.netsparker.com/blog/web-security/disable-directory-listing-web-servers) for different server engines.

You could also protect those folders with `.htaccess` and `.htpasswd`.
