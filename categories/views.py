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

class MixViewCategory(generic.View):
    def get(self, request):
        allcategories = Category.objects.order_by('id')
        form = CategoryModelForm
        context = {
            'categories': allcategories,
            'form': form
        }
        return  render(request, "categories/category_index.html", context)



class CategoryUpdateView(generic.UpdateView):
   model = Category
   template_name = "categories/category_update.html"
   form_class = CategoryModelForm
    
   def get_success_url(self):
     return reverse("categories:category-index")


def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect("/categories")
