from django.shortcuts import render, reverse, redirect
from django.views import generic
from .forms import LeadModelForm, LeadModifyForm
from .models import Lead, User
from django.db.models import Q
from .filters import LeadFilter
from django_filters.views import FilterView
from users.views import staff, sudo
from django.core.exceptions import PermissionDenied



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
    
   def get_success_url(self):
     return reverse("leads:lead-index")


class LeadIndexView(generic.ListView):
    model = Lead
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


# def search(request):
#     lead_list = Lead.objects.all()
#     lead_filter = LeadFilter(request.GET, queryset=lead_list)
#     return render(request, 'leads/search_index.html', {'filter': lead_filter})
# 
# def status(request):
#     lead_list = Lead.objects.all()
#     lead_filter = LeadFilter(request.GET, queryset=lead_list)
#     return render(request, 'leads/status_index.html', {'filter': lead_filter})


class LeadAdvancedSearch(FilterView):
    filterset_class = LeadFilter
    paginate_by = 100
    template_name = 'leads/search_index.html'

class LeadAdvancedStatus(FilterView):
    filterset_class = LeadFilter
    paginate_by = 100
    template_name = 'leads/lead_index.html'


class ModifyView(staff, generic.View):

    def get(self, request, **kwargs):
        allleads = Lead.objects.all()
        form = LeadModifyForm

        context = {
            'leads': allleads,
            'form': form
        }
        return  render(request, "leads/lead_index.html", context)

    def post(self, request, *args, **kwargs):
      if request.method=="POST":
        lead_ids=request.POST.getlist('id[]')
        form = LeadModifyForm
        for id in lead_ids:
         lead = Lead.objects.get(pk=id)
         lead.user = form.user
         lead.category = form.category
         lead.save()
        return redirect("/leads/modify")

