from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'name':'Halaman Login'
    }
    return render(request, 'login/login.html', context)