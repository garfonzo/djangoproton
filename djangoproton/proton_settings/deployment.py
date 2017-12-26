''' Deployment Settings Module '''
import os

'''
|--------------------------------------------------------------------------
| Default Driver
|--------------------------------------------------------------------------
|
| The default driver will be used whenever a deployment command is used.
| Your may specify the driver used when deploying.
|
| drivers supported: heroku
'''

DEFAULT = 'heroku'

'''
|--------------------------------------------------------------------------
| Dictionary of Drivers
|--------------------------------------------------------------------------
|
| All drivers can be put in here as a dictionary.
|
'''

DRIVERS = {
    'heroku': {
        'app': 'DjangoProton',
        'hosts': [
            'djangoproton.herokuapp.com'
        ]
    }
}
