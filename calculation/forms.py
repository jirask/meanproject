from django import forms
 
class CalculateForm(forms.Form):

    def validate_type(value):
        if(isinstance(value,int) or (isinstance(value,list)  and all([isinstance(item, int) for item in value]))):
            pass
        else:
            
            raise forms.ValidationError(code='invalid_type',
            message='Input type is invalid. Accepted values are single numbers or a list of numbers. Example: [1,5,6].')

    input_numbers= forms.JSONField(label='',required=True, initial=list,validators=[validate_type])

