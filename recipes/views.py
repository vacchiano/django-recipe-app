from django.shortcuts import render

recipes = [
  {
    'author': 'Dom V.',
    'title': 'Meatballs',
    'content': 'Combine ingredients, form into balls, brown, then place in oven.',
    'date_posted': 'May 18th, 2022'
  },
  {
    'author': 'Gina R.',
    'title': 'Chicken Cutlets',
    'content': 'Bread chicken, cook on each side for 8 min',
    'date_posted': 'May 18th, 2022'
  },
  {
    'author': 'Bella O.',
    'title': 'Sub',
    'content': 'Combine ingredients.',
    'date_posted': 'May 18th, 2022'
  }
]

# Create your views here.
def home(request):
  context = {
    'recipes': recipes
  }
  return render(request, 'recipes/home.html', context)

def about(request):
  return render(request, 'recipes/about.html', {'title': 'about page'})