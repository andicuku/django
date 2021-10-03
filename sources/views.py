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


class MixViewSource(generic.View):
    def get(self, request):
        allsources = Source.objects.order_by('id')
        form = SourceModelForm
        context = {
            'sources': allsources,
            'form': form
        }
        return  render(request, "sources/source_index.html", context)


def source_delete(request, pk):
    source = Source.objects.get(id=pk)
    source.delete()
    return redirect("/sources")

