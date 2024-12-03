from django.shortcuts import render,redirect
from .models import Blogs,Category

from django.shortcuts import get_object_or_404

from django.db.models import Q
# Create your views here.


def posts_by_category(request,category_id):
    # fetch posts by category
    posts = Blogs.objects.filter(status ='published',category=category_id)
    # use try/except when we want to do some custom action if the category does not exist
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
       
    #use get_objects_or_040 when we 
    #category = get_object_or_404(Category,pk=category_id)
    
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'category':category
        
    }
    return render(request,'posts_by_category.html', context)





# blogs
def blogs(request, slug):
    #return HttpResponse("single blog")
    
    single_post = get_object_or_404(Blogs, slug=slug, status = 'published')
    
    context = {
       'single_post': single_post
    }
    return render(request,'blogs.html', context)




    
#search functionality
def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) ,status = 'published')
    content ={
        'blogs':blogs,
        'keyword':keyword
    }
    
    #print("value :",blogs)
    return render(request,'search.html',content)