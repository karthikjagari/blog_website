from django.shortcuts import render,redirect
from blogs.models import Category,Blogs
from .forms import RegisterForm
#from django.contrib.auth import auth 
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.forms import AuthenticationForm


def home(request):
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True, status ='published')
    posts = Blogs.objects.filter(is_featured = False, status = 'published')
    
    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts
        }
    
    return render(request, 'home.html',context)



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Register')
    else:
        form = RegisterForm()
   
    context = {
        'form': form
    }
    return render(request, 'register.html',context)



# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Correctly calling the login function
                return redirect('dashboard')  # Redirect to your homepage or desired URL
            else:
                # Optional: Add error message for invalid credentials
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)




#logout
def logout_view(request):
    logout(request)
    return redirect('home')

