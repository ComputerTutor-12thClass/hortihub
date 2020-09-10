Deploying Project on PythonAnywhere
----------------------------------------------------------------------------------------------------------------
Step 1: Start a new app on pythonanywhere
Step 2: Open terminal and clone the project
	e.g. git clone <git repository url>
Step 3: Set the path of source code of your project.
	e.g. /home/computertutor/mysite
Step 4: Configure the WSGI configuration file of your project for django.
	* set the path of my manage.py
	* set the path of settings.py
Step 5: Create the virtualenv for python3
	* python3 -m venv <virtualenv-name> 
Step 5: Set the path of your virtual environment.
Step 6: Open the terminal from your virtual environment and install the requirements.
	* Use command : pip install -r requirements.txt
Step 7: Set the path of your static url and root
	e.g.	|url	|path					|
 		|/static/	|/home/computertutor/mysite/staticfiles/	|
Step 8: Now, reload your project.
