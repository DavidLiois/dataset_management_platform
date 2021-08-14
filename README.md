# Dataset Management Platform
 
 Dataset Management Platform

 Heroku Link : https://dataset-management.herokuapp.com/
 
 For heroku authentication : <br />
 Username : user01 and user02 <br />
 Password : User123456789 <br />
 (Both with same password)

 Or using your localhost instead :
 1. Need the latest version for Python (3.9.6), pip (21.2.3), and Django(3.2.6).
 2. Clone this repository.
 3. Go to the directory where manage.py is located.
 4. Open your CMD.
 5. Run "py -m pip install -r requirements.txt" if error occured you can use this command instead "py -m pip install django-heroku" (the command I use in this step is for Windows CMD).
 6. Run "py manage.py makemigrations" and  "py manage.py migrate".
 7. Run "py manage.py createsuperuser" to create an admin account and follow the procedure (if there's no error occurred in step 6).
 8. Run "py manage.py runserver" and go to http://127.0.0.1:8000/ on your browser.

### Built With
* Django, Python, HTML5, CSS3

Documentation used for making this website :

* https://www.w3schools.com/
* https://zetcode.com/django/fileresponse/
* https://stackoverflow.com/questions/43120326/django-check-if-the-uploaded-file-is-a-zip-file
* https://docs.djangoproject.com/en/3.2/
* https://github.com/axelpale/minimal-django-file-upload-example
