# filepath: 
from django.shortcuts import render
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

# ✅ Configure your Gemini API key
genai.configure(api_key="AIzaSyBEg6FY6RfxtK0q9C0gL9ib7T0KFP7v9Yo")

model = genai.GenerativeModel("models/gemini-1.5-pro")

# 🔹 Main chat UI
def chat_page(request):
    return render(request, 'Chatpage.html')

# 🔹 POST endpoint for chat messages
@csrf_exempt
def gemini_chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get("message", "")
        try:
            response = model.generate_content(prompt)
            return JsonResponse({"reply": response.text})
        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"})

# 🔹 Optional: View supported models
@csrf_exempt
def list_models(request):
    try:
        models = genai.list_models()
        model_list = [
            {
                "name": model.name,
                "methods": model.supported_generation_methods
            }
            for model in models
        ]
        return JsonResponse({"models": model_list})
    except Exception as e:
        return JsonResponse({"error": f"Error: {str(e)}"})

def home(request):
    return render(request, 'index.html')

def Nav(request):
    return render(request, 'nav.html')

def About(request):
    return render(request, 'About.html')

def chat(request):
    return render(request, 'chat.html')

def Contact(request):
    return render(request, 'Contact.html')