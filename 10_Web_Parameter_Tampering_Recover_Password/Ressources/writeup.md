### CTF

First, go to the sign in page. Follow the "I forgot my password" link. Once you get there, you will motice something odd. There is no field in which you can submit your email address, as to recover your password. Upon further inspection, we notice that the form action for the "Submit" button calls a POST method to an email: webmaster@borntosec.com. All you have to do now is change the value of the parameter to any other email address.
