from django.http import HttpResponse


def index(request):
	return HttpResponse("Hey there hot stuff..")
