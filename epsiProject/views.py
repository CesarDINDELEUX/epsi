from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, projet_id):
	return HttpResponse("Projet n° : %s." % projet_id)
