from ast import dump
from utils import *
from dotenv import load_dotenv
import os
import settings
from googled import Drive
import datetime
import schedule
import time

drive = Drive()
keep_hours_back = 24 * 7 # 7 days

def clean_old_backups():
    files = drive.list_files_in_folder('nodebb_forum_backups')
    hours_back_date = datetime.datetime.now() - datetime.timedelta(hours=keep_hours_back)
    to_delete = []
    for f in files:
        creation_date = datetime.datetime.fromisoformat(f['createdTime'][:-1])
        if hours_back_date > creation_date: # Too old
            to_delete.append(f['id'])
    if to_delete:
        drive.delete_multiple_files(to_delete)


def backup_nodebb():
    clean_old_backups()
    set_nodebb(settings.NODE_BB_PATH, False)
    now = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
    dump_name = f'nodebb-{now}.gz'
    print(dump_name)
    backup_mongo(settings.DB_NAME, os.environ['DB_USER'], os.environ['DB_PASSW'], dump_name)
    set_nodebb(settings.NODE_BB_PATH, True)

    folder_id = drive.create_folder_if_not_exist('nodebb_forum_backups')
    drive.upload2_folder_by_id(dump_name, folder_id)
    os.remove(dump_name)



def main():
    load_dotenv()
    backup_nodebb()
    schedule.every().day.at("00:00").do(backup_nodebb)
    schedule.every().day.at("12:00").do(backup_nodebb)
    print('Starting schedule...')
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
