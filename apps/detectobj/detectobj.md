# This app is to detect object on a given image

## Model

    name -- imagename
    image -- imagefile
    description -- image file description
    inference image -- detected image
    detectionmodel -- foreign key to the trained models
    detectioninfo -- json field storing detection information with keys.

## View

    Form
        - Upload image
        - Select model
        - Display the inference image
