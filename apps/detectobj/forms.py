from django import forms
from .models import ImageDetection


class ImageDetectionForm(forms.ModelForm):
    class Meta:
        model = ImageDetection
        fields = ('detectionmodel',)


class ModelConfidenceForm(forms.Form):
    confidence = forms.DecimalField(max_value=1,
                                    min_value=0.25,
                                    max_digits=3,
                                    decimal_places=2,
                                    initial=0.45,
                                    help_text="Confidence of the model for prediction.",
                                    )
