from django.shortcuts import render

from django.http import HttpResponse



class Art:  
  def __init__(self, title, artist, style, year):
    self.title = title
    self.artist = artist
    self.style = style
    self.year = year

art = [
  Art('Sunflowers', 'Van Gogh', 'impressionist', 1888),
  Art('The Dance Class', 'Edgar Degas', 'impressionist', 1870),
  Art('Water Lilies', 'Claude Monet', 'impressionist', 1895),
]



# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def art_index(request):
    return render(request, 'art/index.html', { 'art': art })