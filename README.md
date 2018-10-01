2018.08.30
python3.5 django1.11.5 大项目开发框架。特点：项目的各个应用完全独立。
$ cd ../envpy3
$ source bin/activate
$ python -V
… python3.5.4
$ cd ..      #py3_django wuchunlong$
$ ./start.sh

一、注册用户
admin/1234qazx     管理员 超级用户/密码
test/1234qazx        普通用户/密码

恢复到版本：
py3_django wuchunlong$
$ git reset --hard  3437ac4012  # Basic framework
$ git reset --hard  b65b1dd758  # Basic framework README.md
$ git reset --hard  1137c03ee4  # Basic-framework-README.md

git ci -a -m 'register'
git ci -a -m 'login-register'
git ci -a -m 'login-register-list'

git ci -a -m 'video play 2018-10-01'
git ci -a -m '2018-10-01'    #$ git reset --hard     05b5851831f687b3
