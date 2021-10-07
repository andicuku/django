from typing import ContextManager
from django.shortcuts import render, reverse, redirect
from django.views import generic
from .forms import LeadModelForm, LeadModifyForm, CommentForm
from .models import Comment, Lead, User
from django.db.models import Q
from .filters import LeadFilter
from django_filters.views import FilterView
from users.views import staff, sudo
from django.core.exceptions import PermissionDenied
from django.http import Http404



# Create your views here.

class LeadCreateView(generic.CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
       return reverse("leads:lead-index")


class LeadUpdateView(generic.UpdateView):
   model = Lead
   template_name = "leads/lead_update.html"
   form_class = LeadModelForm

   def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['commentform'] = CommentForm()
     return context

   def get_success_url(self, **kwargs):
        pk = self.kwargs.get('pk')
        lead = Lead.objects.get(id=pk)
        return reverse("leads:lead-update", kwargs={'pk': lead.pk})


class LeadIndexView(generic.ListView):
    model = Lead
    ordering = ['-updated_at']
    template_name = 'leads/lead_index.html'
    paginate_by = 100

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.user.is_superuser:
     lead.delete()
    else:
        raise PermissionDenied("Access forbidden 403. Are you root?")
    return redirect("/leads")



class LeadView(sudo, generic.View):
    def get(self, request):
        allleads = Lead.objects.all()
        context = {
            'leads': allleads
        }
        return  render(request, "leads/lead_index.html", context)

    def post(self, request, *args, **kwargs):
      if request.method=="POST":
        lead_ids=request.POST.getlist('id[]')
        for id in lead_ids:
            lead = Lead.objects.get(pk=id)
            lead.delete()
        return redirect("/leads")


class SearchResultsView(generic.ListView):
    model = Lead
    template_name = 'leads/lead_index.html'
    paginate_by = 100

    def get_queryset(self): # new
       query = self.request.GET.get('q')
       q_list = Lead.objects.filter(
           Q(name__icontains=query) | Q(phone__icontains=query) | Q(id__icontains=query) | 
           Q(email__icontains=query) | Q(category__category__icontains=query) |
           Q(source__source__icontains=query) | Q(created_at__icontains=query)| Q(user__username__icontains=query)
       )
       return q_list



class LeadAdvancedSearch(FilterView):
    filterset_class = LeadFilter
    paginate_by = 100
    template_name = 'leads/search_index.html'



class ModifyView(sudo, generic.View):
    def get(self, request):
        leads = Lead.objects.all()
        form = LeadModifyForm
        context = {
            'leads': leads,
            'form': form
        }
        return  render(request, "leads/lead_modify.html", context)

    def post(self, request):
        if request.method=="POST":
          form = LeadModifyForm(request.POST)
          lead_ids=request.POST.getlist('id[]')
          for id in lead_ids:
            lead = Lead.objects.get(pk=id)
            if form.is_valid(self, form):
                user = form.cleaned_data['user']
                category = form.cleaned_data['category']
                lead.user = user
                lead.category = category
                lead.save()
          return redirect("leads:modify")


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'leads/lead_comment.html'

    def form_valid(self, form):
        form.instance.lead_id = self.kwargs['pk']
        form.instance.user_id =self.request.user.id
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        pk = self.kwargs.get('pk')
        lead = Lead.objects.get(id=pk)
        return reverse("leads:lead-update", kwargs={'pk': lead.pk})



