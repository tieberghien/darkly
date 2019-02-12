### CTF

Thanks to the robots.txt file we recovered in a previous exploit, we now know there is a **.hidden** folder any user-agent can access. In order to find the relevant files amongst the thousands of README the folder contains, we wrote a folder scraping script:

   usage: ./scrap.sh IP_ADDRESS

One file stands out, as it merely contains a 32 character string, instead of a fairly derogatory sentence. Congratulations, this is our flag.
