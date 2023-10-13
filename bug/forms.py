from django import forms
from .models import Bug

'''Class For Form Registeration'''


class BugForm(forms.ModelForm):
    '''Form for creating and updating Bug objects.'''
    class Meta:
        '''Form for creating and updating Bug objects and it specifies the model to be used'''
        model = Bug
        fields = ['description', 'bug_type', 'report_date', 'status']


