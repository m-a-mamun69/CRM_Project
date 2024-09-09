from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm

# Create your views here.

def home(request):
    # return HttpResponse("Hello World!!")

    return render(request, 'webapp/index.html')


# - Registration

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            # return redirect('')
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)



# - Login

def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                # return redirect('')
    
    context = {'form':form}
    return render(request, 'webapp/my-login.html', context=context)
