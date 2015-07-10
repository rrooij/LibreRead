BookList
========

BookList is a AGPLv3.0 licensed web applicationi made in Django
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

License
-------

See the file called `LICENSE`.
