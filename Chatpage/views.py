# filepath: [views.py](http://_vscodecontentref_/0)
from django.shortcuts import render

def Chatpage(request):
    return render(request, 'Chatpage.html')