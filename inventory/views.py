from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Sum, F
from .models import Drug,Order
from .forms import AddDrugForm,AddOrderform
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import plot


# Create your views here.

def home_view(request):
  drugs = Drug.objects.all()
  total_drugs = Drug.objects.all().count()
  orders = Order.objects.all()
  total_orders = Order.objects.all().count()
  total_payment = sum(order.get_total_price() for order in orders )
  total_company_payment =  sum(order.get_company_price() for order in orders)
  profit = total_payment - total_company_payment
  total_debt = sum(order.balance_due() for order in orders )
  form = AddOrderform

  
#   if is_debtor:
#     return True

  
   
  context = {'drugs':drugs,
            'orders':orders,
            'total_drugs':total_drugs, 
            'total_payment':total_payment,
            'total_orders':total_orders,
            'total_company_payment':total_company_payment,
            'profit':profit,
            'total_debt':total_debt,
            'form': form,
            

            
            }

  return render(request, 'inventory/home.html', context)


def customer_total_price(request, customer_name):
    total_price = Order.objects.filter(
        customer_name=customer_name
    ).annotate(
         total = Sum(F('quantity') * F('drug__price'))
    )
    context = {'customer_name':customer_name,
    'total_price':total_price}

    return render(request,'inventory/home.html', context)


def chart(request):
    pass


def add_drug(request):
    if request.method == 'POST':
        form = AddDrugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddDrugForm()
    return render(request, 'inventory/add_drug.html', {'form':form})

def edit_drug(request, pk):
    drug = get_object_or_404(Drug, pk=pk)

    if request.method == 'POST':
        form = AddDrugForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddDrugForm(instance=drug)
    
    return render(request, 'inventory/add_drug.html', {'form':form})

def delete_drug(request,pk):
     drug = get_object_or_404(Drug, pk=pk)
     drug.delete()
     return redirect('home')
    

def add_order(request):
 
    form = AddOrderform(request.POST)
    if not form.is_valid():
        # on validation errors, re-render form (you can also send status=400)
        return render(request, 'includes/signup_modal.html', {'form': form}, status=400)

    # save and grab the instance
    order = form.save()

    # render just the new row
    return render(request, 'partials/order_row.html', {'order': order})

def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = AddOrderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddOrderform(instance=order)
    
    return render(request, 'inventory/add_drug.html', {'form':form})

