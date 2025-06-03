from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def login_view(request):
    if request.user.is_authenticated:
        return redirect("login:home")
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.headers.get("x-requested-with") == "XMLHttpRequest":
                    return JsonResponse({"success": f"{user.username}Authenticated success"})
            else:
                if request.headers.get("x-requested-with") == "XMLHttpRequest":
                    return HttpResponseForbidden("Login not allowed. Account is inactive.")
                return render(request, "login.html", {"error": "Login not allowed. Account is inactive."})
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": "Invalid credentials."})
            return render(request, "login.html", {"error": "Invalid credentials."})
    return render(request, "login.html")


def home_view(request):
    if request.user.is_authenticated:
        return render(request, "home.html", {"user": request.user})
    return redirect("login:login")
    
    
    
def logout_view(request):
    logout(request)
    return redirect("login:login")