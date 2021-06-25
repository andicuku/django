from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import reverse, redirect
from django.views import generic
from .models import User
from .forms import SignUpForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class sudo(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        if not self.request.user.is_superuser:
         raise PermissionDenied("Access forbidden 403. Are you root?")
        else:
            return self.request.user.is_superuser


class staff(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        if not self.request.user.is_staff:
         raise PermissionDenied("Restricted action. Staff members only.")
        else:
             return self.request.user.is_staff


class SignupView(generic.CreateView):
    model = User
    template_name = "auth/signup.html"
    form_class = SignUpForm

    def get_success_url(self):
       return reverse("login")

class UserCreateAsAdminView(sudo, generic.CreateView):
    model = User
    template_name = "users/user_create.html"
    form_class = SignUpForm

    def get_success_url(self):
       return reverse("users:user-index")

class UserPasswordView(sudo, generic.UpdateView):
    model = User
    template_name = "users/user_password.html"
    form_class = SignUpForm

    def get_success_url(self):
     return reverse("users:user-index")

class UserUpdateView(sudo, generic.UpdateView):
   model = User
   template_name = "users/user_update.html"
   form_class = UserChangeForm
    
   def get_success_url(self):
     return reverse("users:user-index")


class UserIndexView(sudo, generic.ListView):
   queryset = User.objects.order_by('id')
   paginate_by = 100
   template_name = "users/user_index.html"

def user_delete(request, pk):
    user = User.objects.get(id=pk)
    if request.user.is_superuser:
     user.delete()
    else:
        raise PermissionDenied("Access forbidden 403. Are you root?")
    return redirect("/users")

