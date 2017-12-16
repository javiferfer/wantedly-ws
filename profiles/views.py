from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from profiles.forms import UserForm
from profiles.models import Person, Skill
from array import *


def index(request):
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}
    if(request.user.is_authenticated):context_dict['username'] = request.user.username
    return render(request, 'webUser/index.html', context=context_dict)


def main_page(request):
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}

    current_user = request.user.username

    try:
       user = Person.objects.get(username="Prueba")
    except Person.DoesNotExist:
       user = None

    people = Person.objects.all()
    for p in people:
        if p.username == current_user:
            persona = p
        else:
            persona = None

    skills = Skill.objects.all()

    return render(request,'webUser/main_page.html',{'person': persona, 'skill_array' : skills})

    # skills = Skill.objects.all()
    # i = 0
    # my_array = "No skills"
    # for s in skills:
    #     # if s.person == current_user:
    #     skillName = s.person
    #     if s.person == current_user:
    #         probar = 5
    #         my_array = s.skill
    #         i += 1
    #     else:
    #         probar = 0

    # for s in skills:
    #     if s.skill == "Japanese":
    #         skill = s
    #     else:
    #         skill = None

    # return render(request,'webUser/main_page.html',{'person': persona, 'skill_array' : my_array, 'probar' : probar, 'skill' : skillName})


def method1_object_property(request):
    people = Person.objects.all()
    for p in people:
        p.age = p.getAge()
    return render_to_response('template.htm', {'people': people})


# Register the user
def register_user(request):
    context_dict = {}
    registered = False
    if request.method == 'POST':
        # user_form = UserForm(data=request.POST)
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=True)

            person = Person()
            person.username = user.username
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
