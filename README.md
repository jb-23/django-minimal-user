# Django Minimalist Custom User Model

This project presents the smallest possible Django user model, featuring only
username and password fields. This minimal model is able to operate with the
standard Django auth interface for logging in, logging out, and authenticating
the user on each page visit.

Also included is a demo app that shows the custom user model working.

The user model given here is as small as possible at all costs, and lacks fields
that are required for accessing the Django admin site.

The actual user model classes can be found in [customusers/models.py](customusers/models.py).

[Information about the design of this user model](http://www.bamfordresearch.com/2021/django-minimalist-user-model)
is available on my website.


## Demo Instructions

To try the demo, run the following commands:

`python manage.py migrate`

`python manage.py loaddata demo`

`python manage.py runserver`

View the local test site at http://127.0.0.1:8000/ and try logging in,
logging out, and attempting to log in with incorrect credentials.

The supplied data fixture creates a user with username of "user" and the
password "password".

You can also create users with the command `python manage.py createsuperuser`.
