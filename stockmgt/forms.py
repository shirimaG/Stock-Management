from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category','item_name','quuantity','receive_quuantity','receive_by']

#FORM VALIDATION TO REMOVE DUPLICATES IN DB
	def clean_category(self):
		category = self.cleaned_data.get('category')
		if not category:
			raise forms.ValidationError('This Field Is Required')

		#for instance in Stock.objects.all():
		#	if instance.category == category
				#raise forms.ValidationError(category +' is already created, please add new category')
		return category

	def clean_item_name(self):
		category = self.cleaned_data.get('category')
		item_name = self.cleaned_data.get('item_name')
		if not item_name:
			raise forms.ValidationError('This Field Is Required')

		for instance in Stock.objects.all():
			if (instance.category == category and  instance.item_name == item_name):
				raise forms.ValidationError(item_name +' '+ category +' is already created, please add new Item')
		return item_name




class StockSearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required = False)
	class Meta:
		model = Stock
		fields = ['category','item_name']


class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category','item_name','quuantity']

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quuantity','issue_by']

class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quuantity','receive_by']

class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']