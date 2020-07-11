from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from .filters import PostFilter

""" decorator(@login_required) cant be used in class based view so mixin is used """
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


""" function based view """
""" both function and class based view is used """

""" function for home page """
# def index(request):
#     posts = Post.objects.all().order_by('-id')
#     context = {
#         'posts': posts,
#         'title':'home'
#     }
#     return render(request, 'blog/home.html', context)



""" function for about page view """
def about(request):
    return render(request, 'blog/about.html')



""" search page """
def search(request):
    blog = Post.objects.all()
    blog_filter = PostFilter(request.GET, queryset=blog)
    posts = blog_filter.qs
    return render(request, 'blog/search.html', {'blog_filter':blog_filter,'posts':posts})


""" filter old post to show first """
def oldPost(request):
    posts = Post.objects.all().order_by('id')
    context = {
        'posts': posts,
        'title': 'home'
    }
    return render(request, 'blog/home.html', context)




""" 
   ----------------------------------------------------------
   class based view --- naming convention for class based view 
   <app> / <model>_<viewtype>.html eg - blog/post_list.html
"""

""" home page view """
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-id']

""" template naming convention is used no need to give template name (<app>/<model>_<viewtype>.html)"""

""" classbased view for single post detail """
class PostDetailView(DetailView):
    model = Post



""" classbased view for new post create """
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    """ function for automatically adding the instance author(foreign key) value """
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



""" classbased view for updating old post """
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    """ After importing UserPassesTestMixin, function to forbid current authenticated user from deleting other users post  """
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


""" classbased view for deleting old post """
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
