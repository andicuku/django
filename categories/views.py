from django.shortcuts import render, reverse, redirect
from django.views import generic
from .forms import CategoryModelForm
from .models import Category


class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = "categories/category_create.html"
    form_class = CategoryModelForm

    def get_success_url(self):
       return reverse("categories:category-index")


class CategoryUpdateView(generic.UpdateView):
   model = Category
   template_name = "categories/category_update.html"
   form_class = CategoryModelForm
    
   def get_success_url(self):
     return reverse("categories:category-index")


class CategoryIndexView(generic.ListView):
   queryset = Category.objects.order_by('id')
   paginate_by = 25
   template_name = "categories/category_index.html"


def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect("/categories")
