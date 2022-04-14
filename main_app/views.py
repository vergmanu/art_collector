from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Art, Gallery
from .forms import CommentForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def art_index(request):
    art = Art.objects.all()
    return render(request, 'art/index.html', { 'art': art })

def art_detail(request, a_id):
  art = Art.objects.get(id=a_id)
  comment_form = CommentForm()
  return render(request, 'art/detail.html', { 
    'art': art, 'comment_form': comment_form 
    })

class ArtCreate(CreateView):
  model = Art
  fields = '__all__'

class ArtUpdate(UpdateView):
  model = Art
  fields = ['artist', 'style', 'year']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/art/'

def add_comment(request, a_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.a_id = a_id
    new_comment.save()
  return redirect('detail', a_id=a_id)  

class GalleryList(ListView):
  model = Gallery

class GalleryDetail(DetailView):
  model = Gallery

class GalleryCreate(CreateView):
  model = Gallery
  fields = '__all__'

class GalleryUpdate(UpdateView):
  model = Gallery
  fields = ['name', 'location']

class GalleryDelete(DeleteView):
  model = Gallery
  success_url = '/galleries/'



