from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm): #Quiero un formulario
    class Meta:
        model = Employee #Que rellene este modelo
        fields = ['name', 'last_name', 'email']#Con estos campos
        #fields = '__all__' Atajo para introducir todos los campos del modelo
        #extra_fields = ['salary']
        #exclude = ('email, )