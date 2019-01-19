import logging
import os

# BASE_DIR = os.path.dirname(__file__)
# logging.basicConfig(level=logging.INFO,
#                     filename=os.path.join(BASE_DIR, 'backupdb.log'),
#                     format='%(asctime)s [%(levelname)s] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')
# log = logging.getLogger("backupdb")

cmdStr = (r'cd {webdir}/src '
          '&& rm -rf db1 db2'
          '&& dd if=db.txt |openssl des3 -d -k "{passwd}"|tar zxf - '
          '&& mv db1 db2 '
          '&& [ "x$(diff db2/production.sqlite3 {webdir}/src/mysite/production.sqlite3)" != "x" ] '
          '&& rm -rf {webdir}/src/db1 '
          '&& mkdir -p {webdir}/src/db1 '
          '&& cp {webdir}/src/mysite/production.sqlite3 {webdir}/src/db1 '
          '&& cd {webdir}/src '
          '&& rm -rf db.txt '
          '&& tar -zcvf - db1|openssl des3 -salt -k "{passwd}" | dd of=db.txt '
          '&& git commit -a -m "`date +%Y%m%d[%H:%M:%S]`"'
          '&& git push'.format(webdir=r'''{remote_website_dir}''', 
                               passwd=r'''{db_zip_password}'''))

print(cmdStr)
os.system(cmdStr)
