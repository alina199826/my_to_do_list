
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from accounts.models import Profile
from accounts.forms import MyUserCreationForm, ProfileChangeForm, UserChangeForm
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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


class UserList(PermissionRequiredMixin, ListView):
    template_name = 'user_list.html'
    context_object_name = 'users'
    model = get_user_model()
    paginate_by = 5
    permission_required = 'webapp.сan_see_list_user'


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'
    form_profile_class = ProfileChangeForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'profile_form' not in kwargs:
            context['profile_form'] = self.form_profile_class(instance=self.get_object().profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.form_profile_class(instance=self.get_object().profile, data=request.POST,
                                               files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        return self.render_to_response(self.get_context_data(form=form, profile_form=profile_form))

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.get_object().pk})


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.request.user.pk})