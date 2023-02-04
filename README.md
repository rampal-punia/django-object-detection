# Django Object Detection With YoloV5

## Demo of the WebApp

<https://user-images.githubusercontent.com/104087274/183131139-6a2c9b6d-2f0e-4f25-83b3-df2281eeb489.mov>

### A project to demonstrate easy integration of YoloV5 in Django WebApp

Note: This is not a full-fledged production ready app though can be scaled to work as one.

## Features of the WebApp

- Create/Edit ImageSets.
- Upload multiple images with dropzonejs to the selected ImageSet.
- Convert uploaded image size to 640 x 640. (For faster detection)
- Upload/update a custom pre-trained model.(If you have offline files of a model)
- YoloV5 models will download upon selection. (Active internet connection required for this step.)
- Detect object on an image with YoloV5/custom pre-trained model.

### Note

An image with the name **default.png** in media folder is required for user-profile. Create media folder and add any image file with this name 'default.png'.

## Steps to use locally

```bash
clone the repo locally

create virtual env 

# install dependencies
pip install django
pip install django-crispy-forms
pip install django-cleanup
pip install django-debug-toolbar
pip install celery
pip install yolov5

# migrate
python manage.py migrate

# create super user
python manage.py createsuperuser # (it may show an error page if no 'default.png' in media folder. See note above.)

# run
python manage.py runserver

login
# Login at the web address 127.0.0.1:8000 using the superuser credentials.

Create ImageSet
# create an ImageSet first and then upload images into the ImageSet from ImageSet detail page.

# On images list page click on detect object.

# select a YoloV5 model
# the YoloV5 dependencies and pre-trained model will start downloading.
```

## Apps

- Detectobj
- images
- modelmanager
- users

## Javascript library

- dropzonejs
- ekko-lightbox

## Django starter template used

[DjangoAdvancedBoilerplate](https://github.com/CodingMantras/DjangoAdvancedBoilerplate)
