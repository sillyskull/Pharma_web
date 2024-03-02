from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from .models import Doctor,Patient,Medical_Report,Extra_Values,Room_doc,Patient_tablets,Remainder,Predict
from django.contrib.auth.models import User
from .models import Medicines

class MedicineCraeteForm(ModelForm):
    class Meta:
        model = Medicines
        fields = '__all__'
        exclude = ["host"]

