from django.http import HttpResponse

def tasks_home(request):
    return HttpResponse("Tasks app is connected successfully!")
