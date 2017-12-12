from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>This is the users section</h1>")
