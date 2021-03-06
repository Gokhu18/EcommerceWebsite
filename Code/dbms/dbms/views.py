import logging
import app1
from app1.models import *
from django.template import Context, loader
from django.db.models import Max
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext,loader
from dbms.forms import *
from django.shortcuts import render_to_response
from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import Http404
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg
import collections

logged_id=-1

def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			check=Customer.objects.all().aggregate(Max('custid'))
			
			if check['custid__max']!=None:
                                id_count=check['custid__max']+1
                        else:
                                id_count=0
			account = Customer(custid=id_count, name=form.cleaned_data['name'],username = form.cleaned_data['username'],pwd=form.cleaned_data['pwd'],email=form.cleaned_data['email'],address=form.cleaned_data['address'],phoneno=form.cleaned_data['phone'])
                        account.save()
                        return HttpResponseRedirect('http://127.0.0.1:8000/login')
                       		
			 
	else:
		form=UserForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response ('signup.html',variables)

def login(request):
        global account
        global logged_id
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			account=Customer.objects.get(username=form.cleaned_data['username'],pwd=form.cleaned_data['pwd'])
                        if account:
                         global logged_id
			 logged_id=account.custid				
                         
                         return HttpResponseRedirect('http://127.0.0.1:8000/customer_home')  		
        else:
	            
		form=LoginForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response ('login.html',variables)


def customer_home(request):
	global logged_id
	

        try:
                account=Customer.objects.get(custid=logged_id)
                username=account.username
                context=RequestContext(request,{'username':username})
		return render(request,'customer_home.html',None)

        except Customer.DoesNotExist:
                #404
                return HttpResponseNotFound('<h1>Session has expired login again.</h1>')
        #account=Account.objects.get(user_id=logged_id)

                
def goods(request):

	global logged_id

	if request.method=='GET':
		if 'q' in request.GET and request.GET['q']:
			q = request.GET['q']
			#categories
			if q == 'BOOKS' or q == 'FASHION' or q == 'MEDIA' or q == 'TV' or q == 'MOBILES' or q == 'LAPTOPS' :
				q=q.upper()
				goods = Good.objects.filter(category=q).distinct()
			#search		 	
			else:
				goods = Good.objects.filter(Q(product_name__icontains=q)|Q(brand__icontains=q))
			t=loader.get_template('goods.html')
			c=Context({'goods':goods,})
			return HttpResponse(t.render(c)) 
		#display all products       		
		else:
   			try:
        	        	account=Customer.objects.get(custid=logged_id)
        	        	goods=Good.objects.all()
				t=loader.get_template('goods.html')	
				c=Context({'goods':goods,})
				return HttpResponse(t.render(c))   
        		except Customer.DoesNotExist:
        	        #404
        	        	return HttpResponseNotFound('<h1>Session has expired login again</h1>')
        #account=Account.objects.get(user_id=logged_id)'''


def index(request):
    global logged_id
    logged_id=-1
    context=None
    return render(request,'index.html',context)

def add_order(request):
      global logged_id
      gid = request.GET['pid']
      goods = Good.objects.filter(pid=gid)
      products = Product.objects.filter(goodsid=gid)
      sellers = Seller.objects.filter(product__goodsid=gid)

      for good in goods:
	category=good.category

	if category == 'BOOKS' :
	 books=Book.objects.filter(pid=gid)
	 t=loader.get_template('order_books.html')
	 c=Context({'products':products,'goods':goods,'books':books,'sellers':sellers,})
	
        elif category == 'FASHION' :
         fashion=Fashion.objects.filter(pid=gid)
	 t=loader.get_template('order_fashion.html')
	 c=Context({'products':products,'goods':goods,'fashion':fashion,'sellers':sellers,})

	elif category == 'MEDIA' :
	 media=Media.objects.filter(pid=gid)
	 t=loader.get_template('order_media.html')
	 c=Context({'products':products,'goods':goods,'media':media,'sellers':sellers,})
	
	
	elif category == 'TV' :
	 tvs=TV.objects.filter(pid=gid)
	 t=loader.get_template('order_tv.html')
	 c=Context({'products':products,'goods':goods,'tvs':tvs,'sellers':sellers,})

      	elif category == 'LAPTOPS' :
	 laptops=Laptop.objects.filter(pid=gid)
	 t=loader.get_template('order_laptop.html')
	 c=Context({'products':products,'goods':goods,'laptops':laptops,'sellers':sellers,})


        elif category == 'MOBILES' :
	 mobiles=Mobile.objects.filter(pid=gid)
	 t=loader.get_template('order_mobile.html')
	 c=Context({'products':products,'goods':goods,'mobiles':mobiles,'sellers':sellers})



      return HttpResponse(t.render(c))

def add_to_cart(request):
      global logged_id
      try:
      		account=Customer.objects.get(custid=logged_id)
      		p = request.GET['pid']
      		product=Product.objects.get(pid=p)

		try:
			cart_entry = CustomerItems.objects.get(pid=product,custid=account)
			cart_entry.qty = cart_entry.qty + 1
			cart_entry.save()
		except CustomerItems.DoesNotExist:
      			cart_entry = CustomerItems(pid=product,custid=account,qty=1)
      			cart_entry.save()
      		t=loader.get_template('add_to_cart.html')
      		c=Context({'customer':account,'p':p,})
      		return HttpResponse(t.render(c))
      except Customer.DoesNotExist:
        	        #404
              	return HttpResponseNotFound('<h1>Session Has Expired Login Again.</h1>')

def view_cart(request):
      global logged_id
      sum1 = 0
      try:
      		account=Customer.objects.get(custid=logged_id)
		customerId=account.custid
		customerItems=CustomerItems.objects.filter(custid=account)
		for ci in customerItems:
			sum1 = sum1 + ci.qty * ci.pid.price	
		products=Product.objects.filter(customeritems__custid=account)
		
		t=loader.get_template('view_cart.html')
      		c=Context({'customerId':customerId,'customerItems':customerItems,'sum1':sum1})
      		return HttpResponse(t.render(c))
      except Customer.DoesNotExist:
        	        #404
              	return HttpResponseNotFound('<h1>Session Has Expired Login Again.</h1>')

def remove_from_cart(request):
     global logged_id
     sum1 = 0
     try:
		p=request.GET['pid']
      		account=Customer.objects.get(custid=logged_id)
		
		toDelete=Product.objects.get(pid=p)
                CustomerItems.objects.filter(pid=toDelete,custid=logged_id).delete()
				
		customerId=account.custid
                customerItems=CustomerItems.objects.filter(custid=account)
		for ci in customerItems:
			sum1 = sum1 + ci.qty * ci.pid.price	
		products=Product.objects.filter(customeritems__custid=account)
				
		t=loader.get_template('remove_from_cart.html')
      		c=Context({'customerId':customerId,'customerItems':customerItems,'sum1':sum1,})
      		return HttpResponse(t.render(c))

     except Customer.DoesNotExist:
        	        #404
              	return HttpResponseNotFound('<h1>Session Has Expired Login Again.</h1>')

def buy(request):
     global logged_id

     p = request.GET['pid']

     products = Product.objects.get(pid=p)
     goods = Good.objects.filter(product__goodsid=products.goodsid)
     sellers = Seller.objects.get(product__pid=p)

     final_price = (products.price-(products.price*(products.discount/100.0)))
     t=loader.get_template('buy.html')
     c=Context({'goods':goods,'sellers':sellers,'products':products,'final_price':final_price,})
     return HttpResponse(t.render(c))


def confirmOrder(request):
     global logged_id
     p = request.GET['pid']
     qty = request.GET['qty']

     products = Product.objects.get(pid=p)

     try:
     	qty = int(qty)
     	if qty <= products.qty_left :
     		goods = Good.objects.filter(product__goodsid=products.goodsid).distinct()
     		sellers = Seller.objects.get(product__pid=p)
     		products.qty_left = products.qty_left - qty
     		products.save()
     		final_price = (products.price-(products.price*(products.discount/100.0)))*qty
     		try:
		  account=Customer.objects.get(custid=logged_id)
     		  t=loader.get_template('confirmOrder.html')
        	  c=Context({'goods':goods,'sellers':sellers,'final_price':final_price,'account':account,'qty':qty,})
        	  return HttpResponse(t.render(c))
     		except Customer.DoesNotExist:
		  return HttpResponseNotFound('<h1>Session Has Expired Login Again.</h1>')
     	else :
		t=loader.get_template('confirmOrder.html')
		c=Context({})
		return HttpResponse(t.render(c))
     except ValueError:
		t=loader.get_template('confirmOrder.html')
		c=Context({})
		return HttpResponse(t.render(c))

def buy_from_cart(request):
     global logged_id

     p = request.GET['pid']
     q = request.GET['qty']
     q = int(q)
     products = Product.objects.get(pid=p)
     goods = Good.objects.filter(product__goodsid=products.goodsid)
     sellers = Seller.objects.get(product__pid=p)
     toDelete = Product.objects.get(pid=p)
     CustomerItems.objects.filter(pid=toDelete,custid=logged_id).delete()
     qty=q
     final_price = (products.price-(products.price*(products.discount/100.0)))*q
     t=loader.get_template('buy_from_cart.html')
     c=Context({'goods':goods,'sellers':sellers,'products':products,'final_price':final_price,'qty':qty,})
     return HttpResponse(t.render(c))
