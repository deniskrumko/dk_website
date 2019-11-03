import subprocess

from fabric.api import task, local
from fabric.operations import prompt
from core.display import print_msg


# MAIN COMMANDS
# ============================================================================

@task
def manage(command):
    """Run ``python3 manage.py`` command."""
    return local('python3 manage.py {}'.format(command))


@task
def remote(host='192.168.1.13', port=8000):
    """Run remove server."""
    ifconfig = subprocess.check_output('ifconfig')
    if host not in ifconfig.decode('utf-8'):
        return print_msg(f'Host {host} not in "ifconfig"', error=True)

    return manage(f'runserver {host}:{port}')


@task
def run():
    """Run server"""
    return manage('runserver')


@task
def shell():
    """Run python shell."""
    return manage('shell_plus')


@task
def startapp(app_name):
    """Start new application.

    Name of application can be nested, like "apps.app_name" or
    "apps.utils.app_name".

    """
    names_list = app_name.split('.')

    if len(names_list) == 1:
        return print_msg(
            'Name of app must include root folder. '
            'Like "apps.{}"'.format(names_list[0]),
            error=True
        )

    path = '/'.join(names_list)
    local('mkdir {0}'.format(path))
    manage(
        'startapp --template=core/app_template {0} {1}'
        .format(names_list[-1], path)
    )
    return print_msg('Please, add your app to "INSTALLED_APPS"')


# GIT
# ============================================================================

@task
def push():
    """Push changes to all servers."""
    print_msg('1. Pushing to origin')
    local('git push origin master --tags')

    print_msg('2. Pushing to Heroku')
    local('git push heroku master')


# LOCALES
# ============================================================================

@task
def makemessages():
    """Make messages."""
    return manage('makemessages -l ru --no-location')


@task
def compilemessages():
    """Compile messages."""
    return manage('compilemessages')


# MIGRATIONS AND DATABASE
# ============================================================================

@task
def makemigrations():
    """Make migrations for database."""
    manage('makemigrations')


@task
def migrate():
    """Apply migrations to database."""
    print_msg('Applying migrations')
    manage('migrate')


@task
def createsuperuser(email='root@root.ru'):
    """Create superuser with default credentials."""
    print_msg('Creating superuser')
    return manage('createsuperuser --username root --email {}'.format(email))


@task
def resetdb():
    """Reset database to initial state."""
    print_msg('Remove "scr/media" folder')
    local('rm -rf media/')

    print_msg('Reset database')
    manage('reset_db -c --noinput')

    migrate()
    createsuperuser()

    print_msg('Populate database?')
    answer = prompt('\n', default='yes')

    if answer.lower() in ('y', 'yes', 1):
        populate_db()


# STATIC CHECKS: ISORT AND PEP8
# ============================================================================

@task
def isort():
    """Fix imports formatting."""
    print_msg('Running imports fix')
    local('isort apps core config -y -rc')


@task
def pep8(path='apps core'):
    """Check PEP8 errors."""
    print_msg('Checking PEP8 errors')
    return local('flake8 --config=.flake8 {}'.format(path))


# REQUIREMENTS
# ============================================================================

@task
def requirements():
    """Install requirements."""
    print_msg('Installing requirements')
    local('pip install -r requirements.txt')


# HEROKU
# ============================================================================

@task
def hlogs():
    """Get Heroku logs."""
    local('heroku logs --source app --tail')


# MANAGEMENT COMMANDS SHORTCUTS
# ============================================================================

@task
def populate_db():
    """Populate database with dummy data."""
    print_msg('Start populating DB')
    manage('populate_db')
