from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import reverse, redirect
from django.views import generic
from .models import User
from .forms import SignUpForm

class SignupView(generic.CreateView):
    model = User
    template_name = "auth/signup.html"
    form_class = SignUpForm

    def get_success_url(self):
       return reverse("login")

class UserCreateAsAdminView(generic.CreateView):
    model = User
    template_name = "users/user_create.html"
    form_class = SignUpForm

    def get_success_url(self):
       return reverse("users:user-index")

class UserPasswordView(generic.UpdateView):
    model = User
    template_name = "users/user_password.html"
    form_class = SignUpForm

    def get_success_url(self):
     return reverse("users:user-index")

class UserUpdateView(generic.UpdateView):
   model = User
   template_name = "users/user_update.html"
   form_class = UserChangeForm
    
   def get_success_url(self):
     return reverse("users:user-index")


class UserIndexView(generic.ListView):
   queryset = User.objects.order_by('id')
   paginate_by = 100
   template_name = "users/user_index.html"


def user_delete(pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect("/users")

