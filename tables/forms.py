from django import forms
from django.core import validators

class Cropform(forms.Form):
    
    location = forms.CharField(error_messages={'required':'Enter location '})
    fieldcropid = forms.CharField(error_messages={'required':'Enter field'})
    croptype = forms.CharField(error_messages={'required':'Enter farm'})
    cropvariety = forms.CharField(error_messages={'required':'Enter farmer'})
    name = forms.CharField(error_messages={'required':'Enter plot'})
    expecyieldpeh = forms.CharField(error_messages={'required':'Enter rows'})
    avgplanthei = forms.CharField(error_messages={'required':'Enter columns'})
    expecperi = forms.CharField(error_messages={'required':'Enter plants'})

class Plotform(forms.Form):
    
    location = forms.CharField(error_messages={'required':'Enter location '})
    field = forms.CharField(error_messages={'required':'Enter field '})
    farm = forms.CharField(error_messages={'required':'Enter farm '})
    farmer = forms.CharField(error_messages={'required':'Enter farmer '})
    plot = forms.CharField(error_messages={'required':'Enter plot '})
    rows = forms.CharField(error_messages={'required':'Enter rows '})
    columns = forms.CharField(error_messages={'required':'Enter columns '})
    plants = forms.CharField(error_messages={'required':'Enter plants '})

class Soilform(forms.Form):
    # user = forms.ForeignKey(User, on_delete=models.CASCADE)
    # datetime = forms.DateTimeField(auto_now_add=True)
    location = forms.CharField(error_messages={'required':'Enter location '})
    dailyweat = forms.CharField(error_messages={'required':'Enter location '})
    mintemp = forms.CharField(error_messages={'required':'Enter location '})
    maxtemp = forms.CharField(error_messages={'required':'Enter location '})
    windspeed = forms.CharField(error_messages={'required':'Enter location '})
    humidity = forms.CharField(error_messages={'required':'Enter location '})
    sunshinehrs = forms.CharField(error_messages={'required':'Enter location '})

class Issueform(forms.Form):
    
    location = forms.CharField(error_messages={'required':'Enter location '})
    issueid = forms.CharField(error_messages={'required':'Enter location '})
    solution = forms.CharField(error_messages={'required':'Enter location '})



class Toolform(forms.Form):
    location = forms.CharField(error_messages={'required':'Enter location '})
    toolid = forms.CharField(error_messages={'required':'Enter location '})
    toolname = forms.CharField(error_messages={'required':'Enter location '})
    rate = forms.CharField(error_messages={'required':'Enter location '})