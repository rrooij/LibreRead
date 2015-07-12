LibreRead
========

LibreRead is a AGPLv3.0 licensed web application made in Django
for managing book collections. This is still a work in progress,
I'm not even sure if I will finish this.

Installation
------------

Run the application on a web server supporting Python 3 and Django.

1. Change settings in booklist/settings.py, by renaming settings.sample.py to settings.py
2. Run `python manage.py migrate` to create the necessary tables
3. Host the application

Progress
--------

For now, there isn't much functionality. Feel free to contribute.

The basic functionality that I'm aiming for is:

* Ability to add a book to your personal list and give it a status (Read, to-read etc.)
* The ability for users to add books
* Being able to rate books and write reviews

Reason
------

There is no AGPLv3.0 web application for managing book collections, with social media features.
My aim is to make a site like GoodReads, but without the corporate backing of Amazon and involving the
community with the development.

It's also a learning opportunity for me. This is my first time using Django, so don't be afraid to point
me to mistakes I've made.

License
-------

See the file called `LICENSE`.
