Rent Rocket
============

Rent Rocket is a web based application for crowdsourcing energy usage in rental properties.  The goal is to enable renters to make informed decisions of where to rent based on the total cost of a rental property.  We hope that this will increase demand for more energy efficient units, which in turn will encourage property owners to improve the energy efficiency of their properties. 

Vagrant
-------------
To assist with getting a development environment set up quickly, Rent Rocket uses vagrant to create a virtual machine with all of the necessary requirements.

Start with a copy of the source code repository:

git clone https://github.com/City-of-Bloomington/green-rental.git rentrocket

Be sure to download and install the latest version of Vagrant:
(apt-get versions can be out of date)

https://www.vagrantup.com/downloads.html

Also download and install the latest VirtualBox for your OS:

https://www.virtualbox.org/

Then you should be able to:

cd rentrocket
vagrant up

This may take a while, but when the command finishes, you should have a working development server.

Next:

vagrant ssh

for now, create tables manually:

    cd /vagrant
    python manage.py syncdb

    ./manage.py migrate utility
    ./manage.py migrate building
    ./manage.py migrate person
    ./manage.py migrate city
    ./manage.py migrate content
    ./manage.py migrate inspection
    ./manage.py migrate manager
    ./manage.py migrate source
    ./manage.py migrate allauth.socialaccount

    cd /vagrant/scripts
    python make_cities.py

    /home/vagrant/google_appengine/dev_appserver.py --host 0.0.0.0 /vagrant



Then, back on your main (host) system, open a browser and navigate to:

http://localhost:8888/building/

The map will be blank... no data has been imported, but everything should work!

Resources
-----------------

Rent Rocket uses the following tools and resources to implement the application:

http://www.python.org/

https://www.djangoproject.com/

https://developers.google.com/appengine/?csw=1

http://www.mysql.com/

https://developers.google.com/maps/documentation/javascript/

https://code.google.com/p/geopy/

http://www.rentrocket.org/building/bloomington_in

http://git-scm.com/


Source code is available here:

https://github.com/City-of-Bloomington/green-rental

Requirements
-----------------

Python, a MySQL server, Django, and the Google App Engine SDK are required for running a local development environment. 

Other required libraries have been included in the local project directory so they will be available when deployed to App Engine.  They should be available already. 

Development Server
------------------------

For starting a local development server:

     /path/to/google_appengine/dev_appserver.py rentrocket

Where rentrocket is your local copy of this repository. 

Database synchronization
----------------------------------

A development server won't do much until the database schema is in place and initial data has been created.  This is done with:

     python manage.py syncdb

https://docs.djangoproject.com/en/dev/howto/initial-data/#where-django-finds-fixtures
may need to do this manually... good way to verify it works if values not shown

     python manage.py loaddata rentrocket/fixtures/initial_data.json

     ./rentrocket/scripts/make_service_providers.py
     
field type reference:
https://docs.djangoproject.com/en/1.5/ref/models/fields/#django.db.models.CharField

    ./manage.py schemamigration building --auto
    ./manage.py schemamigration city --auto
    ./manage.py schemamigration content --auto
    ./manage.py schemamigration inspection --auto
    ./manage.py schemamigration manager --auto
    ./manage.py schemamigration person --auto
    ./manage.py schemamigration utility --auto
    ./manage.py schemamigration source --auto


    ./manage.py migrate utility

    ./manage.py migrate building
    ./manage.py migrate city
    ./manage.py migrate person
    ./manage.py migrate content
    ./manage.py migrate inspection
    ./manage.py migrate manager
    ./manage.py migrate source
    ./manage.py migrate allauth.socialaccount

    python ./scripts/make_cities.py

    #if enabled: (not currently)
    ./manage.py migrate allauth.socialaccount.providers.facebook
    ./manage.py migrate allauth.socialaccount.providers.twitter


Database reset
----------------------------------

Remove existing tables with a tool like Sequel Pro.  Then resync as above:

    python manage.py syncdb


Production
-------------------

    SETTINGS_MODE='prod' ./manage.py migrate building
    SETTINGS_MODE='prod' ./manage.py migrate city
    SETTINGS_MODE='prod' ./manage.py migrate content
    SETTINGS_MODE='prod' ./manage.py migrate inspection
    SETTINGS_MODE='prod' ./manage.py migrate manager
    SETTINGS_MODE='prod' ./manage.py migrate person
    SETTINGS_MODE='prod' ./manage.py migrate utility
    SETTINGS_MODE='prod' ./manage.py migrate source
    SETTINGS_MODE='prod' ./manage.py migrate allauth.socialaccount


    SETTINGS_MODE='prod' ./manage.py migrate allauth.socialaccount.providers.facebook
    SETTINGS_MODE='prod' ./manage.py migrate allauth.socialaccount.providers.twitter


    SETTINGS_MODE='prod' 


Creating initial migrations with South
------------------------------------------

Shouldn't need to do this often / ever:

    rm -rf building/migrations
    rm -rf city/migrations
    rm -rf content/migrations
    rm -rf inspection/migrations
    rm -rf manager/migrations
    rm -rf person/migrations
    rm -rf utility/migrations
    rm -rf source/migrations

    ./manage.py schemamigration building --initial
    ./manage.py schemamigration city --initial
    ./manage.py schemamigration content --initial
    ./manage.py schemamigration inspection --initial
    ./manage.py schemamigration manager --initial
    ./manage.py schemamigration person --initial
    ./manage.py schemamigration utility --initial
    ./manage.py schemamigration source --initial



Other Dependencies
-----------------------

As mentioned above, these have been included locally already:

   sudo pip install geopy

for database migrations:

   sudo pip install South


