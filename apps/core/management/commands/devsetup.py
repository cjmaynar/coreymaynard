import os
import settings

from django.core.management.base import NoArgsCommand
from django.core.management.commands import syncdb


def confirm(warning=None):
    if warning is not None:
            print warning
    response = raw_input('Continue? (Yes/No)\n').lower().strip()
    while 1:
            if response not in ('yes', 'no', 'y', 'n'):
                    response = raw_input('Your answer did not match expected input.\nTry again: ').lower().strip()
                    continue
            else:
                if response in ('yes', 'y'):
                    # continue with setup
                    return True
                else:
                    # cancel setup
                    break

    return False


class Command(NoArgsCommand):
    '''This Command is used to replace the default Django syncdb command. It
    ensures that all tables in the database are dropped, and then readded. If
    the auth module is listed in the INSTALLED_APPS, a superuser is created
    based off the informations in the site's settings file.'''
    def handle_noargs(self, **options):
        dropcmd = 'DROP DATABASE %s;' % (settings.DATABASE_NAME,)
        createcmd = 'CREATE DATABASE %s;' % (settings.DATABASE_NAME,)
        mysqlcmd = 'mysql -h%s -u%s -p%s' % (
            settings.DATABASE_HOST,
            settings.DATABASE_USER,
            settings.DATABASE_PASSWORD,
        )

        print
        print "Your current database: %s" % (settings.DATABASE_NAME)
        print
        if not confirm('Warning: this will destory your current database'):
                print 'Canceled'
                return
        else:
                sqlpipe = os.popen(mysqlcmd, 'w')
                print 'Dropping old database...'
                sqlpipe.write(dropcmd)
                print 'Creating new database...'
                sqlpipe.write(createcmd)
                sqlpipe.close()
                print 'Syncing database...'
                syncdb.Command().handle_noargs(interactive=False)

                if 'django.contrib.auth' in settings.INSTALLED_APPS:
                    # Only add superuser if auth is installed
                    print 'Adding Superuser...'
                    from django.contrib.auth.management.commands import createsuperuser
                    from django.core.management import call_command

                    call_command('createsuperuser', interactive=True, username=settings.USER_NAME, email=settings.EMAIL)

                print
                print 'Database setup complete.'
                '''
                if not confirm('Run fixture scripts?'):
                print 'Exiting.'
                return
                else:
                print 'Running installed fixtures...'
                for app in settings.INSTALLED_APPS:
                    if app[0:6] != 'django':
                        print "App: %s" % (app)

                print 'Fixtures completed.'
                '''
