from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre")
    url = forms.URLField(label="Tu sitio web", required=False, initial="http://")
    comment = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=10, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean_name(self):
        name = self.cleaned_data.get("name") #Para que comience a partir de las validaciones generales
        #A partir de aquí comenzamos con las validaciones personalizadas

        if name != "Open":
            raise forms.ValidationError("Tan solo el valor Open está permitido para este campo")
        
        else:
            return name