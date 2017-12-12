from django.http import HttpResponse
from django.shortcuts import render
from profiles.forms import UserForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 

# def index(request):
# 	return HttpResponse("<h1>Welcome to the Wantedly Coding Challenge</h1>")

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Wantedly Coding Challenge"}

    if(request.user.is_authenticated):
        context_dict['username'] = request.user.username
        if 'gameID' in request.session:
            context_dict['myTurn'] = status_turn(request)

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'webUser/game.html', context=context_dict)

# Sessions

# Funcion: Formulario necesario para a~nadir un nuevo usuario.
# Entrada: dos cadenas con el nombre del usuario y la clave
# Salida: Mensaje acusando la creacion del nuevo usuario.

def register_user(request):
    context_dict = {}
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()
            registered = True
            context_dict = {'boldmessage' : "Usuario creado correctamente"}
        #Invalid form?
        else:
            print user_form.errors
    # Blank forms, ready for user input
    else:
        user_form = UserForm()
    return render(request, 'webUser/register.html', {'user_form' : user_form, 'registered' : registered})


# def logout(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")

# Funcion: Desconexion  del usuario.
# Esta funcion debe borrar todas las variables de sesion.
# Entrada: Se hace uso de las funciones de Django para gestionar usuarios
def logout_user(request):
    if not request.user.is_authenticated():
        return render(request, 'webUser/nologged.html')
    else :
        username = request.session["uname"]
        logout(request)
        #logout limpia TODA la sesion la linea de abajo no es necesaria
        #if 'counter' in request.session:
            #del request.session
        return render(request, 'webUser/logout.html', {'username' : username})

# def login(request):
#     m = Member.objects.get(username=request.POST['username'])
#     if m.password == request.POST['password']:
#         request.session['member_id'] = m.id
#         return HttpResponse("You're logged in.")
#     else:
#         return HttpResponse("Your username and password didn't match.")

#Funcion: Usando el sistema de verificacion de Django, comprueba que la pareja (usuario,clave) es correcta.
#Entrada: dos cadenas con el nombre del usuario y la clave
#Salida: Mensaje dando la bienvenida al usuario al sistema. Incluid el nombre del usuario y su id en el mensaje.
#Nota: No hagais una consulta a la base de datos para comprobar que el nombre
#de usuario y la clave son correcto. Usad el sistema de autenticacion provisto por Django.

def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        #usamos el sistema de django para comprobar la clave y el usuario
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session["uid"] = user.id #nos guardamos esto para futuras referencias
                request.session["uname"] = user.username
                return render(request, 'webUser/login.html',
                              {'user.username': user.username, 'user.id' : user.id})

            else:
                return HttpResponse ("El usuario {0} no esta activo o no existe.". format(username))
        else:
            return HttpResponse("Usuario o password incorrectos.")
    else:
        return render(request, 'webUser/login.html', {})
