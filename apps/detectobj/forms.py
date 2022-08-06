from django import forms
from .models import InferencedImage


class InferencedImageForm(forms.ModelForm):
    model_conf = forms.DecimalField(label="Model confidence",
                                    max_value=1,
                                    min_value=0.25,
                                    max_digits=3,
                                    decimal_places=2,
                                    initial=0.45,
                                    help_text="Confidence of the model for prediction.",
                                    )

    class Meta:
        model = InferencedImage
        fields = ('custom_model', 'model_conf')


class YoloModelForm(forms.ModelForm):
    model_conf = forms.DecimalField(label="Model confidence",
                                    max_value=1,
                                    min_value=0.25,
                                    max_digits=3,
                                    decimal_places=2,
                                    initial=0.45,
                                    help_text="Confidence of the model for prediction.",
                                    )

    class Meta:
        model = InferencedImage
        fields = ('yolo_model', 'model_conf')
