''' Proton Commands '''

import subprocess
import sys
import os
from djangoproton.proton_settings import deployment

def deploy():
    try:
        output = subprocess.Popen(
            ['heroku', 'git:remote', '-a', str(deployment.DRIVERS[deployment.DEFAULT]['app'].lower())], stdout=subprocess.PIPE).communicate()[0]
    except FileNotFoundError:
        raise Exception(
            '\033[91mThe deploy command requires the Heroku CLI tool. Go to https://devcenter.heroku.com/articles/heroku-cli to learn more\033[0m'
        )
    if not output:
        create_app = input(
            "\n\033[92mApp doesn't exist for this account. Would you like to create one?\033[0m \n\n[y/n] > ")  # Python 2
        if 'y' in create_app:
            subprocess.call(
                ['heroku', 'create', deployment.DRIVERS[deployment.DEFAULT]['app'].lower()])
            if '--local' in sys.argv:
                subprocess.call(['python', 'proton', 'deploy', '--local'])
            elif '--current' in sys.argv:
                subprocess.call(['python', 'proton', 'deploy', '--current'])
            else:
                subprocess.call(['python', 'proton', 'deploy'])
    else:
        if '--local' in sys.argv:
            subprocess.call(['git', 'push', 'heroku', 'master:master'])
        elif '--current' in sys.argv:
            subprocess.call(['git', 'push', 'heroku', 'HEAD:master'])
        else:
            subprocess.call(['git', 'push', 'heroku', 'master'])
