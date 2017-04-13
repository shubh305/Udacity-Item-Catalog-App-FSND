# Udacity-Item-Catalog-App-FSND
Item Catalog App Project in the Udacity Full stack web developer Nanodegree.

## Requirements :-

* Python 2.7
* Flask
* SQLAlchemy
* httplib2
* apiclient
* Flask-SeaSurf
* google-api-python-client
* httplib2
* Jinja2

Please refer to the requirements.txt file and install the prequisite requirements using :
```
$ pip install -r requirements.txt
```

## Initial Setup :-

* Download the zip and extract or Clone the repository : ```$ git clone https://github.com/shubh305/Udacity-Item-Catalog-App-FSND.git```

* Place the downloaded/cloned folder inside vagrant directory.

## Google credentials file - 

* Go to https://console.cloud.google.com/apis/credentials/oauthclient and setup Google OAuth API Credentials. 

* Enter http://localhost:5000 in the Authorized JavaScript origins and http://localhost:5000/goauth2redirect in the Authorized redirect URIs.

* After saving, download and rename the file to ```g_client_secrets.json``` and replace that file in the project directory.

## Facebook credentials file -
 
* Go to https://developers.facebook.com/apps and setup a new app.

* Add a new product "Facebook Login" and add http://localhost:5000 in the Valid OAuth redirect URIs.

* Replace your Client id and secret in the ```fb_client_secret.json``` file.

## Instructions to run the project :-

* Download the zip and extract or Clone the repository using ```$ git clone https://github.com/shubh305/Udacity-Item-Catalog-App-FSND.git```.

* Place the downloaded/cloned folder inside vagrant directory.

* Start vagrant and then migrate to the project directory in the terminal.

* Initialize the database : ```$ python database_setup.py```

* Populate the database with pre configured categories and items : ```python lotsofcategories.py```

* Launch the application : ```$ python catalog.py```

* Open the browser and go to http://localhost:5000

It is important you use *localhost* instead of *0.0.0.0* inside the URL address. That will prevent OAuth from failing.

## Access the JSON endpoint :-

You can access the JSON endpoint within the provided interface in the app itselft, or just go to http://localhost:5000/catalog/json to directly access the JSON endpoint.
