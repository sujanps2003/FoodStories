import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def addreceipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_category = data.get('receipe_category')
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_category=receipe_category
        )

        return redirect('/receipes/')
    return render(request, 'addreceipe.html')

def landing(request):
    return render(request, 'landing.html')

def category_recipes(request, category):
    recipes = Receipe.objects.filter(receipe_category=category)

    context = {
        'receipes': recipes,
        'category':category,
    }
    return render(request, 'categories.html', context)

def receipes(request):
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))


    context = {'receipes':queryset}
    return render(request,'receipes.html', context)


def delete_receipe(request, id):
    query_set = Receipe.objects.get(id = id)
    query_set.delete()
    return redirect('/receipes/')

def update_receipe(request,id):
    query_set = Receipe.objects.get(id = id)
    context = {'receipe':query_set}
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        query_set.receipe_name = receipe_name
        query_set.receipe_description = receipe_description
        if receipe_image:
            query_set.receipe_image = receipe_image
        query_set.save()
        return redirect('/receipes/')
    return render(request,'update_receipes.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid username")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.info(request, "Invalid password")
            return redirect('/login/')
        else:
            login(request ,user)
            return redirect('/receipes')

    return render(request ,'login.html')

@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "user name already exits")
            return redirect('/register/')

        user = User.objects.create(
            username =username ,
        )
        user.set_password(password)
        user.save()

        messages.info(request, "account created sucessfully")
        return redirect('/')
    return render(request,'register.html')





