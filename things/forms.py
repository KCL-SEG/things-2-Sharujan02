"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import RegexValidator

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description' : forms.Textarea(), 
            'quantity' : forms.NumberInput(),
            }
        validators = {
            'name' : [RegexValidator(
                regex=r'^[A-Za-z ]{1,35}$',
                message='Name cannot be blank and must be less than 35 characters',
            )],
            'quantity' : [RegexValidator(
                regex=r'^(?:[0-9]|[1-4][0-9]|50)$',
                message='Quantity must be between 0 and 50.',
            )],
        }
        
    # quantity = forms.IntegerField(
    #     widget = forms.NumberInput(),
    #     validators=[
    #         RegexValidator(
    #             regex=r'^(?:[0-9]|[1-4][0-9]|50)$',
    #             message='New Password must contain an uppercase character, ' 
    #                     'a lowercase character and a number.',
    #         ),
    #     ],
    # )

    

