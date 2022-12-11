from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import Group
from home_page.views import BaseTemplatePageMixin
from django.urls import reverse_lazy
from django.views import generic
from . import models
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from .forms import UserEditMultiForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birthday_date= form.cleaned_data.get('birthday_date')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.zip_code = form.cleaned_data.get('zip_code')
            user.profile.address1 = form.cleaned_data.get('address1')
            user.profile.address2 = form.cleaned_data.get('address2')
            user.profile.information = form.cleaned_data.get('information')
            user.save()
            user_group = Group.objects.get(name='Customers')
            user.groups.add(user_group)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home-page')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class ShowProfiles(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = models.Profile
    permission_required = ("accounts.view_profile")
    login_url = reverse_lazy('login')
    template_name = 'accounts/list_profiles.html'
class ShowProfile(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.DetailView):
    model = models.User
    permission_required = ("auth.view_user")
    login_url = reverse_lazy('login')
    template_name = 'accounts/detail_profile.html'    

class ShowCustomers(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = models.Profile
    permission_required = ("accounts.view_profile")
    login_url = reverse_lazy('login')
    template_name = 'accounts/list_profiles_cust.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['customers'] = models.Profile.objects.filter(user__groups__name='Customers')
        return context

class ShowManagers(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = models.Profile
    permission_required = ("accounts.view_profile")
    login_url = reverse_lazy('login')
    template_name = 'accounts/list_profiles_man.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['managers'] = models.Profile.objects.filter(user__groups__name='Managers')
        return context        

class ShowProfile(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, generic.DetailView):
    model = models.Profile
    template_name = 'accounts/detail_profile.html'
    permission_required = ("accounts.view_profile")
    login_url = reverse_lazy('login')


User = get_user_model()

class UpdateProfiles(BaseTemplatePageMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditMultiForm
    template_name = 'accounts/update_profile.html'
    context_object_name='form_user'
    model = models.User
    permission_required = ("auth.view_user")
    def get_success_url(self):
        cur_user=self.get_object().profile.pk
        return reverse_lazy('accounts:profile-detail', kwargs={'pk': cur_user})
    def get_form_kwargs(self):
        kwargs = super(UpdateProfiles, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object,
            'profile': self.object.profile,
        })
        kwargs.update({'active_user': self.request.user})
        return kwargs


     