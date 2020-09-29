# AnimalAbuse

### Make a virtual environment:
```bash
pip install virtualenv
virtualenv myenv
python3 -m venv myenv
source myenv/bin/activate
```
### Install Required packages
```bash
pip install django
pip install django-filters
pip install django-bootstrap-form
```

### To deactivate the environment run the following
```bash
deactivate
```

### Start Running：
run on terminal： `python manage.py runserver`


### Make Migrations
```bash
./manage.py makemigrations
./manage.py migrate
```


### Make Super User 
```bash
./manage.py createsuperuser
```
