from django.shortcuts import render, reverse, redirect
from django.views import generic
from .forms import SourceModelForm
from .models import Source


class SourceCreateView(generic.CreateView):
    model = Source
    template_name = "sources/source_create.html"
    form_class = SourceModelForm

    def get_success_url(self):
       return reverse("sources:source-index")


class SourceUpdateView(generic.UpdateView):
   model = Source
   template_name = "sources/source_update.html"
   form_class = SourceModelForm
    
   def get_success_url(self):
     return reverse("sources:source-index")


class SourceIndexView(generic.ListView):
   queryset = Source.objects.order_by('id')
   paginate_by = 25
   template_name = "sources/source_index.html"


def source_delete(request, pk):
    source = Source.objects.get(id=pk)
    source.delete()
    return redirect("/sources")

