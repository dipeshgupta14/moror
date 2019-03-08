# moror
mororai website using django

# Create app using Heroku

Pre Requisite Knowledge

=> Creating a Project in Django

After creating the desired app Install the following packages using 'pip' command:

=> gunicorn

=> django-heroku

In 'settings.py' import 'django_heroku' and at last line (in settings.py) write 'django_heroku.settings(locals())'

Create 'requirements.txt' and include python packages with their version.

Create a file named 'Procfile'(note: this file must be without any extension) and write 'web: gunicorn <app name>.wsgi --log-file -'

Upload 'requirements.txt' and 'Procfile' on your Git profile.

=> these file must be in the root folder.

Heroku:

=> Sign up on Heroku

=> Create app

     ->Download and install Heroku CLI
     
     ->Run Command Prompt and enter following commands:
     
     	 -heroku login
           
     	 -heroku config:set DISABLE_COLLECTSTATIC=1

=> In Setting section , under 'Add Buildpack' select 'Python'.

=> In 'Deploy' section, select 'Connect with Git' option.

=> Connect with your git repository.

=> Click on 'Enable Automatic Deploy'

=> Click on 'Deploy Branch'

=> Run https://<app name>.herokuapp.com/.
