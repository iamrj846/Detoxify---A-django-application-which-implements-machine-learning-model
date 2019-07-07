from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from . import forms
from django.shortcuts import render
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from . import model

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

@login_required
def form_name_view(request):
    form = forms.FormName()
    
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():

            # Do comething code
            """ print("Validation success!!")
            print("Education: " + form.cleaned_data['education']) """
            # load the model from disk
            loaded_model = pickle.load(open('C:\\Users\\Raunak Jain\\Desktop\\My_Django_Stuff\\proj1\\proj1\\finalized_model.sav', 'rb'))
            X = [form.cleaned_data.get('gender', None),
                form.cleaned_data.get('age', None),
                form.cleaned_data.get('education', None),
                form.cleaned_data.get('currentSmoker', None),
                form.cleaned_data.get('cigsPerDay', None),
                form.cleaned_data.get('BPMeds', None),
                form.cleaned_data.get('prevalentStroke', None),
                form.cleaned_data.get('prevalentHyp', None),
                form.cleaned_data.get('diabetes', None),
                form.cleaned_data.get('cholestrol', None),
                form.cleaned_data.get('sysBP', None),
                form.cleaned_data.get('diaBP', None),
                form.cleaned_data.get('BMI', None),
                form.cleaned_data.get('heartrate', None),
                form.cleaned_data.get('glucose', None)]
            data = pd.DataFrame([X])
            X = data.iloc[:, :].values
            y_pred = loaded_model.predict(X)
            if y_pred[0]==1:
                value="You have a risk of 10 year coronary heart disease"
            else:
                value="You don't have a risk of 10 year coronary heart disease"
            return render(request, 'result.html', {'value':value})
    
    return render(request, 'form_page.html', {'form': form})