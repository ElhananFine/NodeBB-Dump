Hello! <br>
It is a daily backup script for Google Drive of NodeBB-based forums. <br>
The script stops MongoDB and NodeBB before starting the backup, performs a backup, and runs back. <br>
The setting in the script is a daily backup at 12 in the morning and at noon, and automatic deletion of their backups older than 3 days, but you are free to change the hours in the main.py file. <br>
<br>
How to use a script: <br>
To log in to your Google drive API account, retrieve the credentials.json file as guided here: <br>
https://github.com/thewh1teagle/googled and place it in the script folder. <br>
Then, enter the MongoDB access information in utils.py file <br>
Good luck and good day! <br>
<br>
