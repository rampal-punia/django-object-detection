# Django Advance Boilerplate With Different Image Upload Apps.

Django boilerplate for any scalable WebApp project. Equipped with __users app__, __celery__, __django-debug-toolbar__, __lightbox.js__, __dropzone.js__ and __cropper.js__.

## Why this boilerplate?
- To avoid the repetitive tasks of setting up a new Django Web App project. If a project requires image upload, and user login/register functionalities, this boilerplate can be used for easy start up. 
 

## Project Structure
- Separate app folder containing all apps
    - Apps details:
        - singleimages: To upload single image at a time using django forms and models.

        - multipleimages: To upload multiple images using django forms and models.

        - croppedimages: To upload single original image using django forms and models, and then cropping that image(using cropperjs) and storing all cropped images corresponding to the orig image.

        - dropzoneimages: To upload multiple images using dropzonejs.

        - Users: A users app with login, logout and sign up pages.

- Reusable/Pluggable Apps 
    - All apps can be added to other projects with tweaking a little.(Yes few lines need to be added or deleted from settings, urls, and views if an app is removed.)

- Settings.py
    - base.py
    - development.py
    - production.py
    - test.py

- Secrets.json (For boilerplate only. Preferably add in .gitignore)
    - To store database, email backend credentials and the secret-key

- static
    - Local static files with, bootstrap

- Templates folder
    - base.html
    - partials folder contains _nav, _paginator, _scripts and other html file

- Requirements folder
    - Separate for base, development, production & testing

## Overview

### Login
<img src="static\img\login.png" height=auto width=450>

### Register
<img src="static\img\register.png" height=auto width=450>

### Registration under approval.
- Login through django admin after createsuperuser command, in users model check active box.
- Logout from django admin
- Restart app and login again.

<img src="static\img\reg_under_approve.png" height=auto width=450>

### Main page
<img src="static\img\dashboard.png" height=auto width=450>

### Upload single image app
<img src="static\img\single.png" height=auto width=450>

### Cropperjs
<img src="static\img\cropperjs.png" height=auto width=450>

### Images uploaded via dropzone.
<img src="static\img\dropzone.png" height=auto width=450>


## Other Python Packages
- django-crispy-forms
- Pillow
- Django-cleanup
- OpenCV

## Task queue manager
- Celery

## Javascript
- Ekko-lightbox: To display images in a lightbox.

- Dropzonejs: To upload multiple images

- Cropperjs: To crop an image at front-end

## Used dependencies

This boilerplate relies on the following plugins, libraries and frameworks:

- [Bootstrap](https://getbootstrap.com/)
- [Django](https://www.djangoproject.com/)
- [django-registration](https://github.com/ubernostrum/django-registration)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Opencv2](https://opencv.org/)
- [Dropzone](https://www.dropzone.dev/js/)
- [CropperJs](https://fengyuanchen.github.io/cropperjs/)
- [Ekko-lightbox-BS5](https://github.com/trvswgnr/bs5-lightbox)
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)

## Requirements
```bash
amqp==5.1.1
asgiref==3.5.2
autopep8==1.6.0
backports.zoneinfo==0.2.1
billiard==3.6.4.0
celery==5.2.7
click==8.1.3
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.2.0
colorama==0.4.5
Django==4.0.6
django-celery-beat==2.3.0
django-celery-results==2.4.0
django-cleanup==6.0.0
django-crispy-forms==1.14.0
django-debug-toolbar==3.5.0
django-timezone-field==5.0
kombu==5.2.4
numpy==1.23.1
opencv-contrib-python==4.6.0.66
Pillow==9.2.0
prompt-toolkit==3.0.30
pycodestyle==2.8.0
python-crontab==2.6.0
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
sqlparse==0.4.2
toml==0.10.2
tzdata==2022.1
vine==5.0.0
wcwidth==0.2.5
```
