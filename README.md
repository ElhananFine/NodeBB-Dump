Hello!
It is a daily backup script for Google Drive of nodeBB-based forums.
The script stops MongoDB and nodeBB before starting the backup, performs a backup, and runs back.
The setting in the script is a daily backup at 12 pm and noon, and automatic deletion of their backups older than 3 days, but you are free to change the hours in the main.py file.

How to use a script:
To log in to your Google drive API account, retrieve the credentials.json file as guided here:
https://github.com/thewh1teagle/googled and place it in the script folder.
Then, enter the MongoDB access information in utils.py file
Good luck and good day!
