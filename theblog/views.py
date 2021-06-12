from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditPost, CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data( *args, **kwargs)
        context['cat_menu'] =cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_detail.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data( *args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html'
    # fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    template_name = 'theblog/update_post.html'
    form_class = EditPost


class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'theblog/add_category.html'
    fields = '__all__'

def categoryView(request,cats):
    cats1 = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'theblog/categories.html', {'cats': cats.title().replace('-', ' '), 'cats1': cats1})

def categoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'theblog/categories_list.html', { 'cat_menu_list': cat_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'theblog/add_comment.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)