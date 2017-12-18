from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from profiles.forms import UserForm
from profiles.models import Person, Skill
from array import *

# Index and default web interface.
def index(request):
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}
    if(request.user.is_authenticated):context_dict['username'] = request.user.username
    return render(request, 'webUser/index.html', context=context_dict)

# Main web page when you are logged in.
def main_page(request):
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}

    return render(request,'webUser/main.html')

# Web page that shows your profile.
def profile_page(request):
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}

    current_user = request.user.username

    people = Person.objects.all()
    for person in people:
        if person.username == current_user:
            user = person

    if request.POST:
        if request.POST.get('name') and request.POST.get('age'):
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()

    skill_objects = Skill.objects.all()

    if request.POST.get('skill'):
        newSkill = Skill()
        newSkill.person = current_user
        newSkill.skill = request.POST.get('skill')
        newSkill.save()

    return render(request,'webUser/profile.html',{'person': user, 'skill_objects': skill_objects})

# Web page that shows the skills of the users.
def users_page(request):
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}

    current_user = request.user.username

    people = Person.objects.all()
    for person in people:
        if person.username == current_user:
            user = person

    skill_objects = Skill.objects.all()
    skillChecked = None

    if request.POST.get('checkbox'):
        skillChecked = request.POST.get('checkbox')

        for skill in skill_objects:
            if skill.skill == skillChecked:
                skill.number_of_likes = skill.number_of_likes + 1
                skill.save()
    return render(request,'webUser/users.html', {'person': user, 'people': people, 'skill_objects': skill_objects})

# Register the user.
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


# Logout the user.
def logout_user(request):
    username = request.session["uname"]
    logout(request)
    return render(request, 'webUser/logout.html', {'username' : username})

# Login the user.
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
                return render(request, 'webUser/login.html', {'user.username': user.username, 'user.id' : user.id})
            else:
                return HttpResponse ("The user {0} is not active or it does not exist.". format(username))
        else:
            return HttpResponse("User or password incorrect.")
    else:
        return render(request, 'webUser/login.html', {})
