# -*- coding: utf-8 -*-
#!/usr/bin/env bash
pushd `dirname $0` > /dev/null
BASE_DIR=`pwd -P`
popd > /dev/null

#############
# Functions
#############
function logging {
    echo "[INFO] $*"
}
function build_venv {
    if [ ! -d env ]; then
        virtualenv env
    fi
    . env/bin/activate
    pip install -r requirements.txt

}
cd ${BASE_DIR}
build_venv
OPT_ENV_FORCE=$1

function creator_db {
    logging "makemigrations"
	python "${BASE_DIR}/mysite/manage.py" "makemigrations"

	logging "migrate"
	python "${BASE_DIR}/mysite/manage.py" "migrate"

}
function write_data_db {
	logging "initdb.py"
	python "${BASE_DIR}/mysite/initdb.py"

}


function launch_webapp {
    python "${BASE_DIR}/mysite/manage.py" "runserver" 
}
#############
# Main
#############
#cd ${BASE_DIR}
cd ${BASE_DIR}/mysite


#创建数据库表，适合添加数据库后操作，能重复操作，不会破坏数据。
if [ "${OPT_ENV_FORCE}x" == "-cx" ];then    
    creator_db
fi
# 创建数据表、创建超级用户，不会破坏数据。
if [ "${OPT_ENV_FORCE}x" == "-cax" ];then    
    creator_db
    python "${BASE_DIR}/mysite/manage.py" "createsuperuser" #创建超级用户
fi

# 初始化数据库。创建数据表,删除数据后再加载数据。谨慎操作！！！
if [ "${OPT_ENV_FORCE}x" == "-ix" ];then    
    
    rm -rf "${BASE_DIR}/mysite/db.sqlite3"
    creator_db
    write_data_db
fi

#删除数据库表，数据不可恢复，谨慎操作！！！
if [ "${OPT_ENV_FORCE}x" == "-dx" ];then
	rm -rf "${BASE_DIR}/mysite/db.sqlite3"
    logging "${BASE_DIR}/mysite/db.sqlite3"
fi
#python "${BASE_DIR}/initsortAPI.py"
launch_webapp
