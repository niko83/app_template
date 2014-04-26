sudo add-apt-repository ppa:fkrull/deadsnakes

echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > "/etc/apt/sources.list.d/pgdg.list"
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -


sudo apt-get update;
sudo apt-get upgrade;
sudo apt-get install vim git tree colordiff sysstat ack-grep htop skype subversion mysql-server memcached rabbitmq-server libgeoip1 libgeoip-dev libmemcached-dev zlib1g-dev libssl-dev python-dev build-essential mysql-server python-mysqldb libmysqlclient-dev python-virtualenv python-pip postgresql-9.3 terminator python2.6-dev

#store git password
sudo apt-get install libgnome-keyring-dev
sudo make --directory=/usr/share/doc/git/contrib/credential/gnome-keyring
git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring
                         

git config --global push.default simple
git config --global diff.tool vimdiff
git config --global difftool.prompt false
git config --global alias.d difftool
git config --global user.email "ktotutus@gmail.com"
git config --global user.name "niko"

sudo apt-get install exuberant-ctags nodejs
cd ~; git clone  https://github.com/klen/.vim.git .vim
cd ~/.vim && git submodule init && git submodule update
echo "source ~/.vim/rc.vim" > ~/.vimrc

sudo mkdir /var/www
sudo chown niko:niko -R /var/www/


VIM
#source ~/.vim/rc.vim
#
#" Fast scrool
#nnoremap <C-e> 3<C-e>
#nnoremap <C-y> 3<C-y>
#
#" Session UI
#nnoremap <Leader>ss :SSave<CR>
#nnoremap <Leader>sr :Unite session<CR>
#nnoremap <Leader>sl :SLoad last.vim<CR>
#
#let g:pymode_lint_ignore = "E501,C0110,C0111"
#let g:pymode_lint_ignore = "E501,C0110,C0111,W191,W0312,E711,E126,W0403,E126"
#let g:pymode_lint_checker = "pylint,pep8,pyflakes,mccabe"
#" ~/.vim/bundle/python-mode/pymode/libs/pylama/lint/pylama_pylint/pylint.rc
#" [FORMAT]
#" max-line-length=99
#" [MASTER]
#" init-hook='import sys; sys.path.append("/home/niko/testproject/");sys.path.append("/var/www/test_sp/");' 
#
#au BufNewFile,BufRead *.py setl colorcolumn=80,99
#
#call jsmode#Default("g:jsmode_largefile", 10)
#
#set tpm=100
#
#" ~/.vim/bundle/python-mode.git/pylibs/ropevim.py
#" 342             if isinstance(ci['info'], unicode):
#" 343                 ci['info'] = repr(ci['info'])



sudo pip install virtualenvwrapper
echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc


sudo vim /etc/postgresql/9.3/main/pg_hba.conf

# исправляем в этой строке peer на md5
#local   all             all                                     md5
sudo /etc/init.d/postgresql restart
sudo su postgres
createuser -P username
psql -c"ALTER USER username WITH SUPERUSER;"
createdb -Uusername -W "portal_trunk"
#проверяем
psql -Uusername -W portal_trunk

sudo wget http://hg.rabbitmq.com/rabbitmq-management/raw-file/rabbitmq_v2_8_7/bin/rabbitmqadmin -O /usr/local/bin/rabbitmqadmin
sudo chmod +x /usr/local/bin/rabbitmqadmin
sudo sh -c 'rabbitmqadmin --bash-completion > /etc/bash_completion.d/rabbitmqadmin'

sudo rabbitmqctl add_user niko qweR123$
sudo rabbitmqctl add_vhost /niko
sudo rabbitmqctl set_permissions -p /niko niko ".*" ".*" ".*"
sudo rabbitmqctl set_user_tags niko administrator

mkdir $HOME/.pip_download_cache
echo "export PIP_DOWNLOAD_CACHE=$HOME/.pip_download_cache" >> ~/.bashrc

wget -O ~/.django_bash_completion.sh https://raw.github.com/django/django/master/extras/django_bash_completion
echo "source $HOME/.django_bash_completion.sh" >> ~/.bashrc

[mysqld]                                                                                               
character-set-server = utf8
collation-server = utf8_general_ci
transaction-isolation = READ-COMMITTED
default-time-zone = '+00:00'

USEFUL
======
git show remote origin
git log --graph --color-words --color --source --decorate --all
