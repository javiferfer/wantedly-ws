from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from profiles.forms import UserForm

# Temporal
from profiles.models import Person

def index(request):
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}

    if(request.user.is_authenticated):
        context_dict['username'] = request.user.username
        # if 'gameID' in request.session:
        #     context_dict['myTurn'] = status_turn(request)

    return render(request, 'webUser/index.html', context=context_dict)

# Register the user
def register_user(request):
    context_dict = {}
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=True)

            # Temporal
            person = Person()
            person.username = user.username
            # person.age = 23
            person.email = user.email
            person.save()

            user.set_password(user.password)
            user.save()
            registered = True
            context_dict = {'boldmessage' : "User createlly correctly"}


        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request, 'webUser/register.html', {'user_form' : user_form, 'registered' : registered})

# Logout the user
def logout_user(request):
    if not request.user.is_authenticated():
        return render(request, 'webUser/nologged.html')
    else :
        username = request.session["uname"]
        logout(request)
        return render(request, 'webUser/logout.html', {'username' : username})


def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        #It is used the django's system in order to check the user and the password
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session["uid"] = user.id
                request.session["uname"] = user.username
                return render(request, 'webUser/login.html',
                              {'user.username': user.username, 'user.id' : user.id})

            else:
                return HttpResponse ("The user {0} is not active or it does not exist.". format(username))
        else:
            return HttpResponse("User or password incorrect.")
    else:
        return render(request, 'webUser/login.html', {})
