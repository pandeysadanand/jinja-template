from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SignupForm


#
# def index(request):
#     member = User.objects.all().values()
#     template = loader.get_template('index.html')
#     context = {
#         'member': member,
#     }
#     return HttpResponse(template.render(context, request))


# def add(request):
#     template = loader.get_template('add.html')
#     return HttpResponse(template.render({}, request))
#
#
# def addrecord(request):
#     a = request.POST['first']
#     b = request.POST['last']
#     c = request.POST['email']
#     d = request.POST['password']
#     e = request.POST['address']
#     f = request.POST['zip']
#     g = request.POST['city']
#     h = request.POST['state']
#     i = request.POST['country']
#
#     member = User(first_name=a,
#                   last_name=b,
#                   email=c,
#                   password=d,
#                   address=e,
#                   zip=f,
#                   city=g,
#                   state=h,
#                   country=i)
#     member.save()
#     return HttpResponseRedirect(reverse('index'))
#
#
# def delete(request, id):
#     member = User.objects.get(id=id)
#     member.delete()
#     return HttpResponseRedirect(reverse('index'))
#
#
# def update(request, id):
#     member = User.objects.get(id=id)
#     template = loader.get_template('update.html')
#     context = {
#         'member': member,
#     }
#     return HttpResponse(template.render(context, request))
#
#
# def updaterecord(request, id):
#     first = request.POST['first']
#     last = request.POST['last']
#     email = request.POST['email']
#     password = request.POST['password']
#     address = request.POST['address']
#     zip = request.POST['zip']
#     city = request.POST['city']
#     state = request.POST['state']
#     country = request.POST['country']
#
#     member = User.objects.get(id=id)
#     member.first_name = first
#     member.last_name = last
#     member.email = email
#     member.password = password
#     member.address = address
#     member.zip = zip
#     member.city = city
#     member.state = state
#     member.country = country
#
#     member.save()
#     return HttpResponseRedirect(reverse('index'))
#
#
# def testing(request):
#     template = loader.get_template('template.html')
#     context = {
#         'first_name': 'Sadanand',
#     }
#     return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully !!")
            fm.save()
    else:
        fm = SignupForm()
    return render(request, '../templates/signup.html', {'form': fm})


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                upassword = fm.cleaned_data['password']
                user = authenticate(username=username, password=upassword)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, '../templates/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        return render(request, '../templates/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
