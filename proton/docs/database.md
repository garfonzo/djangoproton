## Database

Out of the box, Proton comes set up to be used with a postgres database, however you'll need to add one more file to round out the setup. 

In `proton/settings` you'll see a `database.py` file. In that same directory, create a file called `db_creds.py`. In that file, all you need to add are the following two lines:
```
USER = 'your_username'
PASSWORD = 'your_password'
```

**Note:**
* This is your username/password for the Postgres database to which Proton will connect. 
* The single quotes are required
* The capitalized words are required

This all assumes that you're run `createdb my-database` (replacing 'my-database' with the name of the database you want Proton to connect to)