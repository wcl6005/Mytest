# -*- encoding: utf-8 -*-

import os
import datetime
from fabric.api import (cd, env, lcd, put, prompt, local, sudo, run,
                        prefix, shell_env, settings, hide)

git_db_passwd = '6yhn(IJN&U*'

# fab git_push
def git_push():
    local('rm -rf env && git add . && git commit -a -m "add" && git push')
    
# fab push
def push(): 
    '''
    1、创建 db.txt
    2、push 工程
    '''
    local('[ ! -f db.txt ] && '
        'mkdir -p db1 && '  
        'chmod -R 777 db1 && '
        'cp ./mysite/db.sqlite3 ./db1/production.sqlite3 && '
        'tar -zcvf - db1|openssl des3 -salt -k "%s" | dd of=db.txt && '
        'rm -rf db1 || [ false ]' %(git_db_passwd))  
    git_push()




