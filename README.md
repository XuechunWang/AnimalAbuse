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
run on terminal： `python manage.py runserver` \
Open on the terminal: http://127.0.0.1:8000/ \
To upload csv file: http://127.0.0.1:8000/upload-csv \
Administration page: http://127.0.0.1:8000/admin \

### Make Migrations (when you make change on models.py file)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Make Super User 
```bash
python manage.py createsuperuser
```
