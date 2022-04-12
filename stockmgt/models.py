from django.db import models

# Create your models here.

category_choice = (
		('Microwave','Microwave'),
		('TV Set','TV Set'),
		('Washing Machine','Washing Machine'),
		)

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name

class Stock(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=True)
	item_name = models.CharField(max_length=50, blank=True, null = True)
	quuantity = models.IntegerField(default='0', blank=True, null = True, verbose_name="Quantity")
	receive_quuantity = models.IntegerField(default='0', blank=True, null = True, verbose_name="Received Quantity")
	receive_by = models.CharField(max_length=50, blank=True, null = True, verbose_name="Received By")
	issue_quuantity = models.IntegerField(default='0', blank=True, null = True)
	issue_by = models.CharField(max_length=50, blank=True, null = True)
	issue_to = models.CharField(max_length=50, blank=True, null = True)
	phone_number = models.CharField(max_length=50, blank=True, null = True)
	created_by = models.CharField(max_length=50, blank=True, null = True)
	reorder_level = models.IntegerField(default='0', blank=True, null = True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	export_to_CSV = models.BooleanField(default= True)


	def __str__(self):
		return self.item_name +' '+ self.category +' '+ str(self.quuantity)
		

