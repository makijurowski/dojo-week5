from django import forms
from .models import Form


class PostSurvey(forms.ModelForm):
    opt_comment = forms.CharField(required=False)
    dojo_location = forms.MultipleChoiceField(required=True)
    language_options = forms.MultipleChoiceField(required=True)

    class Meta:
        model = Form
        fields = ('fname',
                  'lname',
                  'dojo_location',
                  'language_options',
                  'opt_comment')
