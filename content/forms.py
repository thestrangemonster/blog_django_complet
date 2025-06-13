from django import forms

class CommentForm(forms.Form):
  content = forms.CharField(
    label='Votre commentaire',
    widget=forms.Textarea(attrs={
      'rows': 4,
      'placeholder': 'Écrivez votre commentaire ici...'
    })
  )