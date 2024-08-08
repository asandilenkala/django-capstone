from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

def home(request):
    """
    Renders the home page of the portfolio website.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'portfolio/home.html')


# @login_required
def projects(request):
    """
    Renders the projects page with a list of all projects.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered projects page with the list of projects.
    """
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def about(request):
    """
    Renders the about page of the portfolio website.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered about page.
    """
    return render(request, 'portfolio/about.html')


def user_login(request):
    """
    Handles user login functionality. Authenticates the user and logs them in.

    Args:
        request: The HTTP request object. It should contain the username and password if it's a POST request.

    Returns:
        HttpResponse: Redirects to the home page if login is successful, otherwise renders the login page again.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'portfolio/login.html')


def user_logout(request):
    """
    Logs out the current user and redirects to the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Redirects to the home page after logout.
    """
    logout(request)
    # return render(request, 'portfolio/login.html')
    return redirect('home')
