import pathlib
import subprocess
import os

def shell_command(command, wait = True, stdout = None):
    p = subprocess.Popen(command, shell=True, stdout = stdout)
    if wait:
        return p.wait() 

def backup_mongo(db_name, user, passw, out_path):
    # command_0 = 'mongodump --host 127.0.0.1 --port 27017 --db nodebb  --authenticationDatabase admin --username admin --password yaakov1q2w --gzip --archive >  dump_`date "+%Y-%m-%d-%H-%M"`.gz'
    command = f'mongodump --db {db_name}  --authenticationDatabase admin --username {user} --password {passw} --gzip --archive >  {out_path}'
    status = shell_command(command)
    assert status == 0

def set_nodebb(node_bb_path, status):
    print(f'{"Starting" if status else "Stopping"} NodeBB')
    p = pathlib.PurePosixPath(node_bb_path) / 'nodebb'
    command = f'{p} {"start" if status else "stop"}'
    status = shell_command(command)
    # print(stderr.read().decode())
    assert status == 0
