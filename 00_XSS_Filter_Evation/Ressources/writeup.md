### CTF

First, go to the Feedback page. You are asked to leave a feedback in the guestbook. The Message field is vulnerable to XSS filter bypass. The correct syntax for this exploit is something along those lines:

    <script>alert('test');</script>


