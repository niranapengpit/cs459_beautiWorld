from django.shortcuts import render
from django.http import HttpResponse
from .models import BeautyProduct
from django.views import generic
from django.shortcuts import render, redirect
# Create your views here.

def home(request,filter = 0):
	
	cate = "ALL PRODUCTS"
	data = []
	if filter == '1':
		cate = 'SKINCARE'
	if filter == '2':
		cate = 'CLEANSING'
	if filter == '3':
		cate = 'MAKEUP'
	if filter == '4':
		cate = 'VITAMIN'
	
		
	products_list = BeautyProduct.objects.filter()
	for p in products_list:
		if p.category == cate or cate == 'ALL PRODUCTS' or filter == '':
			data.append(p)
	
	context = {
		'data': data,
		'filter': filter,
		'cate': cate
	}
	return render(request, "home.html",context)
   
def login(request):
	# context = {'items' : Item.objects.all()}
    return render(request, 'login.html')

def signup(request):
	# context = {'items' : Item.objects.all()}
    return render(request, 'signup.html')

def cartpage(request):
	# context = {'items' : Item.objects.all()}
    return render(request, 'cartpage.html')
