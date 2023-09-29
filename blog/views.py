from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView , CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# Create your views here.

# posts = [
#     {
#         "author" : "Yogesh Joshi",
#         "title" : "Blog Post 01",
#         "content" : "First post Content",
#         "date_posted" : "August 29, 2023"
#     },
#     {
#         "author" : "Aman Rautela",
#         "title" : "Blog Post 02",
#         "content" : "Second post Content",
#         "date_posted" : "August 29, 2023"
#     },
#     {
#         "author" : "Harshit Pathak",
#         "title" : "Blog Post 03",
#         "content" : "Third post Content",
#         "date_posted" : "August 29, 2023"
#     }
# ]

def home(request):
    # here we have to actually rendering the function and explicitely pass that information.

    context = {
        "posts" : Post.objects.all()
    }
    return render(request,"blog/home.html",context)

class PostListView(ListView):
    # here with class based view, we just have to set some variable and the work is done 


    #this will tell our ListView,  what model to query to create the list
    # object list is being called by the class for the comvention of "posts" for the looping of data
    model = Post
    # for that we must specify the variable to make th class know about it and direct it to the data.
    context_object_name = "posts"
    # ordering = ["-date_posted"]
    template_name = "blog/home.html" # <app> / <model>_<viewtype>.html
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-date_posted"]
    template_name = "blog/user_posts.html" # <app> / <model>_<viewtype>.html
    paginate_by = 5


    def get_query_set(self):
        user=get_object_or_404(User,username=self.kwargs.get("username"))  # kwargs will be the query parameters
        return Post.objects.filter(author==user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields =["title","content"]
    

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form) #running the form_valid method on the parent class, because we are overriding here

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields =["title","content"]
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # a function that our user passes testMixin will run in order to see if the user passes a certain lest condition
    def test_func(self):
        #give the exact post that we're updating , by using a method of the UpdateView that is get_object
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    # here we require the user to be logged in and the post is belong to the author 
    model = Post
    success_url = "/"
    def test_func(self):
        #give the exact post that we're updating , by using a method of the UpdateView that is get_object
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,"blog/about.html",{"title" : "about"})


