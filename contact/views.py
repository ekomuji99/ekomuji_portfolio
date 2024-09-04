from django.shortcuts import render

# Create your views here.
def contact(request):
    context = {
        'name':'Halaman Contact'
    }
    return render(request, 'contact/contact.html', context)