## Deployer sur heroku

### la première fois

* heroku git:remote -a komuso
* git push heroku master
* heroku ps:scale web=1
* heroku run python manage.py syncdb

### les fois suivantes

* git push heroku master
* heroku run python manage.py syncdb
