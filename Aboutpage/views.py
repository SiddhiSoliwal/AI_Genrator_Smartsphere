# filepath: [views.py](http://_vscodecontentref_/0)
from django.shortcuts import render

def aboutpage(request):
    return render(request, 'Aboutpage.html')