# Django Object Detection With YoloV5

## Demo of the WebApp
https://user-images.githubusercontent.com/104087274/183131139-6a2c9b6d-2f0e-4f25-83b3-df2281eeb489.mov


## Features of the WebApp:

- Create/Edit imagesets.
- Upload multiple images with dropzonejs to the selected imageset.
- Convert uploaded image size to 640 x 640. (For faster detection)
- Upload/update a custom pre-trained model.(If you have offline files of a model)
- Yolov5 models will download upon selection. (Active internet connection required for this step.)
- Detect object on an image with yolov5/custom pre-trained model.

### Note
a default.png in media is required for user-profile. Create media folder and add a  'default.png' file here.

## Steps to use locally.
```bash
clone the repo locally

create virtual env

# install dependencies
pip install -r requirements.txt

# migrate
python manage.py migrate

# create super user
python manage.py createsuperuser # (it may show an error page if no 'default.png' in media folder. See note above.)

# run
python manage.py runserver

login
# Login at the web address 127.0.0.1:8000 using the superuser credentials.

Create imageset
# create an imageset first and then upload images into the imageset from imageset detail page.

# On images list page click on detect object.

# select a yolo model
# the yolo dependencies and pre-trained model will start downloading.
```

## Apps:
- Detectobj
- images
- modelmanager
- users

## Main dependencies

- Django
- Yolov5
- Pytorch
- Torchvision
- Tensorboard
- Pillow
- django-crispy-forms
- django-cleanup

## Javascript library
- dropzonejs
- ekko-lightbox

## Django starter template used
[DjangoAdvancedBoilerplate](https://github.com/CodingMantras/DjangoAdvancedBoilerplate)




