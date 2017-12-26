Django Proton focuses on easy development and fast deployment. Django Proton is setup to easily deploy to Heroku by default and currently only supports Heroku for fast deployment. Future drivers will be added.

## Deployment

Since all the `Procfile` and `requirements.txt` files are already in your project, we are already ready to deploy. To deploy to Heroku just run:

    $ python proton deploy

This will use the application name in `your_project/proton_settings/deployment.py` and create a Heroku instance.

**NOTE: This will deploy your application dependent on the `origin/master` branch of your application.**

If there is no Heroku app with the name of your Django Proton application name then `proton` will ask you if you want to create the Heroku application. type `y` to create the application or `n` to abort.

If you enter `y` then sit back and watch as your Django Proton app is deployed to Heroku.

## Types of Deployment

There are three different types of deployment to Heroku.

If you want to deploy your origin/master branch then simply run: 

    $ python proton deploy

If you want to deploy your local master branch then simply run:

    $ python proton deploy --local

If you want to deploy your current branch you are on (as in you branched off master and are on a testbranch) then run: 

    $ python proton deploy --current 

which will deploy `HEAD` to heroku master