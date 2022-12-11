from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#En el formulario tener una seccion para confimar que ambos password sean iguales
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        """ Vamos a indicar que este formulario pertenece a un modelo """
        model = User
        """ Podemos definir que campos seran los que mostremos usando el atributo fields """
        fields = ("username", "first_name", "last_name", "email","password1", "password2")
    
    """ Vamos a sobreescribir el metodo save """
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False) #El super sirve para poder heredar 
        #aumentar el email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
