from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def home(request):
    userlist = User.objects.all()
    context = {
        'userlist': userlist
    }
    return render(request, 'base/home.html', context)

def about(request, id):
    userlist = User.objects.get(id=id)
    context = {
        'userlist': userlist
    }
    return render(request, 'base/about.html', context)

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(name=name, email=email, password=password)
        user.save()
        return redirect('home')

    return render(request, 'base/register.html')

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('home')

def update(request, id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(id=id)
        user.name = name
        user.email = email
        user.password = password
        user.save()

        return redirect('home')
    stud = User.objects.get(id=id)
    context = {'stud': stud}

    return render(request, 'base/update.html', context)