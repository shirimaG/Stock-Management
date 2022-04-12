from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from .models import Stock
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
	title = 'Welcome: This is the home Page'
	form = 'A key component of a tree to grow is WATER.'
	context = {
		"title":title,
		"test":form,
	}
	return render(request,"home.html",context)


def list_items(request):
	header = 'List Of Items'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"form":form,
		"header":header,
		"queryset":queryset,
	}
	if request.method == 'POST':
		queryset = Stock.objects.filter(category = form['category'].value(),
		 item_name__icontains =form['item_name'].value())

#This piece of code exports to csv file

		if form['export_to_CSV'].value == True:
			response = HttpResponse(content_type = 'text/csv')
			response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
			writer = csv.writer(response)
			writer.writerow(['CATEGORY','ITEM NAME','QUANTITY'])
			instance = queryset
			for stock in instance:
				writer.writerow([stock.category, stock.item_name, stock.quuantity])
			return response

		context = {
			"form":form,			
			"header":header,
			"queryset":queryset,
		}

	return render(request,"list_items.html",context)

def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Item added successful')
		return redirect('/list')
	context= {
		"form":form,
		"title":"Add Item",
	}
	return render(request,"add_items.html",context)

def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance = queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance = queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Item updated successful')
			return redirect('/list')

	context = {
		"form":form,
		"title":"Update Item"
	}
	return render(request, "add_items.html", context)

def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method== 'POST':
		queryset.delete()
		messages.success(request, 'Item deleted successful')
		return redirect('/list')
	return render(request, 'delete_items.html')


def stock_details(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"header":queryset.item_name,
		"queryset":queryset,
	}
	return render (request, "stock_details.html", context)


def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance = queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quuantity -= instance.issue_quuantity
		instance.issue_by = str(request.user)
		messages.success(request, "Issued successful. "+ str(instance.quuantity) + " " + str(instance.item_name) + "s left")
		instance.save()

		return redirect('/details/'+str(instance.id))
	context={
		"title":"Issue "+ str(queryset.item_name),
		"form":form,
		"queryset":queryset,
		"username":"issued By: "+str(request.user),
	}
	return render(request, 'add_items.html', context)


def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance = queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quuantity += instance.receive_quuantity
		instance.receive_by = str(request.user)
		messages.success(request, "Received successful. "+ str(instance.quuantity) + " " + str(instance.item_name) + "s now in store")
		instance.save()

		return redirect('/details/'+str(instance.id))
	context={
		"title":"Receive "+ str(queryset.item_name),
		"form":form,
		"queryset":queryset,
		"username":"Received By: "+str(request.user),
	}
	return render(request, 'add_items.html', context)



def reorder_level(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance = queryset)
	if form.is_valid():
		instance=form.save(commit = False)
		instance.save()
		messages.success(request, 'Reorder level for '+ instance.item_name+' is set successfull')
		return redirect('/list')
	context= {
		"form":form,
		"instance":queryset,
	}
	return render(request,"add_items.html",context)
