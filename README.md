# django-versatileimagefield-repro

just reproducing an issue see https://github.com/respondcreate/django-versatileimagefield/issues/204

To run:

```
git clone https://github.com/nicksellen/django-versatileimagefield-repro.git
cd django-versatileimagefield-repro
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py reproduce
```
