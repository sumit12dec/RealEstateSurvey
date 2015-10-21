from django import forms
from .models import Question

class SurveyForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SurveyForm, self).__init__(*args, **kwargs)
		self.fields['apartment'].label = "Area/Apartment"
		CHOICES = (('1', '1 BHK',), ('2', '2 BHK',), ('3', '3 BHK'), ('4', '4 BHK'), ('5', '2.5 BHK'))
		self.fields['bhk'] = forms.ChoiceField(choices=CHOICES)
		self.fields['bhk'].label = "Room Type"
		# self.fields['flat_no'].label = "Flat No."
		# self.fields['flat_no'].help_text = "Flat No."
		self.fields['flat_no'] = forms.CharField(label='Flat No.', 
                    widget=forms.TextInput(attrs={'placeholder': 'Optional'}), required=False)
		self.fields['name'] = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder':'Optional'}), required=False)
		self.fields['block'].label = "Block/Floor"


	class Meta:
		model = Question
		print model , "++++++++"
		exclude = []