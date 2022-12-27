from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.urls import reverse

from accounts.models import Profile
from accounts.forms import MyUserCreationForm
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'create_user.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url

        next_url = self.request.POST.get('next')
        if next_url:
            return next_url

        return reverse('webapp:index')


class UserDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 3


    def get_context_data(self, **kwargs):
        projects = self.get_object().users.all()
        return super().get_context_data(object_list=projects, **kwargs)

class UserList(ListView):
    template_name = 'user_list.html'
    context_object_name = 'users'
    model = Profile
    paginate_by = 5
