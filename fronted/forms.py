from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Imagen','Algoritmo', 'Vecinos')

        widget = {
            'Imagen': forms.FileField(attrs={'class':'form-control'}),
            'Algoritmo': forms.Select(attrs={'class':'form-control'}),
            'Vecinos': forms.IntegerField(attrs={'class':'form-control'})
        }

        