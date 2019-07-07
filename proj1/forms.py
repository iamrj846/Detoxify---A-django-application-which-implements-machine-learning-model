from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators


class FormName(forms.Form):
    gender = forms.ChoiceField(label="Gender", choices=[(1, "Male"), (0, "Female")])
    age = forms.IntegerField(label="Age")
    education = forms.ChoiceField(label="Education", choices=[(1, "Some High School"), (2, "High School or GED"), (3, "Some college or vocational school"), (4, "College")])
    currentSmoker = forms.ChoiceField(label="Smoking", choices=[(0, "Non smoker"), (1, "Smoker")])
    cigsPerDay = forms.IntegerField(label="Number of cigarettes per day")
    BPMeds = forms.ChoiceField(choices=[(0, "Not on BP Medicines"), (1, "On BP Medicines")], label="On BP Meds")
    prevalentStroke = forms.ChoiceField(choices=[(1, "Previously had a stroke"), (0, "No prevalent strokes")], label="Prevalent Stroke")
    prevalentHyp = forms.ChoiceField(choices=[(1, "Hypertensive"), (0, "Not hypertensive")], label="Prevalent hypertensive")
    diabetes = forms.ChoiceField(choices=[(1, "Having Diabetes"), (0, "No diabetes")])
    cholestrol = forms.DecimalField(label="Total cholestrol")
    sysBP = forms.DecimalField(label="Systolic BP")
    diaBP = forms.DecimalField(label="Diastolic BP")
    BMI = forms.DecimalField(label="BMI")
    heartrate = forms.IntegerField(label="Heart Rate")
    glucose = forms.IntegerField(label="Glucose")
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])
"""     def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("Make sure that emails match")
 """
