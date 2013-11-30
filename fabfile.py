# coding: utf-8

from contextlib import contextmanager

from fabric.api import cd, env, get, local, put, run, sudo, prefix

try:
    from fabenv import env
except ImportError:
    msg = "Kurulum için lütfen README.md belgesini okuyun."
    raise RuntimeError(msg)


@contextmanager
def venv():
    with cd('%(root)s%(project_name)s' % env), prefix(env.activate):
        yield


def deploy():
    """Deploy the latest version."""
    with venv():
        run('git pull')
        update_dependencies()

    update_static()
    restart()
    restart_nginx()


def start():
    with venv():
        run('gunicorn -c conf/gunicorn.py app:app')

    restart_nginx()


def restart():
    with venv():
        sudo('sudo kill -HUP `cat /tmp/' + env.project_name + '.pid`')


def restart_nginx():
    """Restart the nginx process."""
    sudo('/etc/init.d/nginx restart')


def update_dependencies():
    """Update requirements remotely."""
    with venv():
        run('pip install -r conf/requirements.txt')


def update_nginx_conf():
    sudo('rm /etc/nginx/sites-enabled/' + env.domain)
    sudo('ln -s /home/wakefield/pyistanbul/conf/nginx.conf /etc/nginx/sites-enabled/' + env.domain)
    restart_nginx()


def update_static():
    """Update static files."""
    with venv():
        sudo('rm -r static/')
        sudo('python manage.py collectstatic --noinput')


def setup():
    """Configure basic tools."""
    with cd(env.root):
        run('git clone git://github.com/pyistanbul/website.git ' + env.project_name)

    with cd('%(root)s%(project_name)s' % env):
        run('virtualenv venv')

    with venv():
        run('pip install -r conf/requirements.txt')

    update_nginx_conf()
    update_static()
    start()


def setup_vm():
    """Setup the VM."""
    sudo('apt-get update && apt-get upgrade && apt-get install git-core '
         'python-setuptools python-pip python-dev build-essential '
         'nginx curl libcurl3')
    sudo('pip install virtualenv')


def clean():
    """Clean the current setup."""
    with cd(env.root):
        sudo('rm -r %s/' % env.project_name)
        sudo('rm /etc/nginx/sites-enabled/' + env.domain)


def clean_pyc():
    """Remove all .pyc files."""
    local('find . -name "*.pyc" -exec rm {} \;')
