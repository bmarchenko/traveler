Traveler
=======

http://travel.stegelman.com

I like to travel, so I made a site about it.  Go figure.  Anyway, using this site is easy.  I suggest using your own design, but if you want to use my crappy one thats fine.

Tech Stack
----------

- Python
- Django
- Google Maps API

Get Running
-----------

I would use a virtual environment to setup the dependencies.  Then....

```
pip install -r conf/requirements.txt
python manage.py syncdb --settings=settings.local
python manage.py migrate --settings=settings.local
python manage.py runserver --settings=settings.local
```

Good luck.