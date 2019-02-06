from django.forms import ModelForm
from django import forms
from models import Custommer, Application

class CustommerForms(ModelForm):
    class Meta():
        model=Custommer

        fields=[
            "name",
            "edge",
            "birth",
            "document",
            "email",
        ]

        labels={
            "name"     : "Name",
            "edge"     : "Edge",
            "birth"    : "Birth",
            "document" :"Document",
            "email"    :"Email",

        }

        widgets={
            "name" : forms.TextInput(
                        attrs={
                            'type' : 'text',
                            'class' : 'your_class',
                            'hidden':False,
                            'max_length':100
                        })
                    ,
            "edge" : forms.TextInput(
                        attrs={
                            'type' : 'number',
                            'class' : 'your_class',
                            'hidden':False,
                            'max_length':100
                        })
                    ,
            "birth" : forms.TextInput(
                        attrs={
                            'type' : 'text',
                            'class' : 'your_class',
                            'hidden':False,
                            'max_length':100
                        })
                    ,
            "document" : forms.TextInput(
                        attrs={
                            'type' : 'text',
                            'class' : 'your_class',
                            'hidden':False,
                            'max_length':100
                        })
                    ,
            "email" :  forms.TextInput(
                        attrs={
                            'type' : 'text',
                            'class' : 'your_class',
                            'hidden':False,
                            'max_length':100
                        })
                    ,
        }


class ApplicationForms(ModelForm):
    class Meta():
        model=Application

        fields=[
            
            "custommer_code",
            "reazon",
        ]

        labels={
            "custommer_code" :"Custommer Code",
            "reazon": "Reazon",

        }

        widgets={
            "custommer_code" : forms.Select(attrs={'class':'forms-control'}),
            "reazon" : forms.TextInput(),
        }

