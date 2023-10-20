from django import forms
from .models import Bug

'''Class For Form Registeration'''


class BugForm(forms.ModelForm):
    '''Form for creating and updating Bug objects.'''
    class Meta:
        '''Form for creating and updating Bug objects and it specifies the model to be used'''
        model = Bug
        fields = ['description', 'bug_type', 'report_date', 'status']
        
        # Adding Widget for styling the feilds
        widgets = {
                'description': forms.Textarea(attrs={'class': 'form-control shadow'}),
                'bug_type': forms.Select(attrs={'class': 'form-control shadow'}),
                'report_date': forms.DateInput(attrs={'class': 'form-control shadow', 'type': 'date'}),
                'status': forms.Select(attrs={'class': 'form-control shadow'}),

                }