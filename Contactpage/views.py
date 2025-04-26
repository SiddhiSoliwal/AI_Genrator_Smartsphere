# filepath: [views.py](http://_vscodecontentref_/0)
from django.shortcuts import render

def Contactpage(request):
    return render(request, 'Contact.html')
