===================================
A FanVue Test
===================================

This technical test consists in building an API for Listings of Music Genres, Albums and Artists.

- Python version: 3.9
- Django version: 3.2
- Django Rest Framework version: 3.12.4
- Database used: SQLite


Installation and Usage
======================

Installing Requirements
_______________________

After cloning this project, install the packages from `requirements.txt` using pip (using a virtual
environment is preferred)::

    $ pip install -r requirements.txt



Start Django Server
___________________

You can start the django server using the following command::

    $ python manage.py runserver


After that, the server will be running at http://127.0.0.1:8000/.


Generate Fake Data Using The Management Command Option
_____________________________

In order to create the first data, you need to run the management command::

    $ python manage.py createfakedata


By executing this command, Django will create sample Genres, Artists and Albums of the authors choice.


After Everything...
_____________________________

Access http://127.0.0.1:8000/genres/view to view the list of genres available and proceed from there.

Thank you!