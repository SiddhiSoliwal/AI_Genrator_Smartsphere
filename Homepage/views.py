from django.shortcuts import render, redirect
from .forms import ContactForm

from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_thank_you')  # Optional: redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Create your views here.
def nav(request):
     return render(request, 'nav.html')

def Home(request):
     return render(request, 'Homepage.html')
def About(request):
     return render(request, 'Aboutpage.html')

def Chat(request):
     return render(request, 'Chatpage.html')
def Contact(request):
     return render(request, 'Contactpage.html')

# Removed duplicate contact_view function to avoid conflicts.

from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                messages.success(request, "Login successful!")
                return redirect('home')  # Replace 'home' with your homepage URL name
            else:
                messages.error(request, "Invalid password.")
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
    return render(request, 'Login.html')

def register_view(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        username = request.POST['username']
        password = make_password(request.POST['password'])
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            User.objects.create(full_name=full_name, email=email, username=username, password=password)
            messages.success(request, "Registration successful!")
            return redirect('login')  # Replace 'login' with your login URL name
    return render(request, 'Login.html')