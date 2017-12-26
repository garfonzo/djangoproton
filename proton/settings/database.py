# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

"""
The "db_creds" file is to be located in the same directory as this file, 
and contains just the username and password for your PSQL database. Like so:


USER = 'your_username'
PASSWORD = 'your_password'


That's it - just two lines. And the single quotes are needed!
"""

from db_creds import USER, PASSWORD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangoproton',
        'USER': NAME,
        'PASSWORD': PASSWORD
    }
}
