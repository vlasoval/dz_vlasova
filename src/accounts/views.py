from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import Group


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


from django.urls import reverse_lazy
from django.views import generic
from . import models
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
class ShowProfiles(generic.ListView):
    model = models.Profile
    # permission_required = ("accounts.view_book_genre")
    # login_url = reverse_lazy('login')
    template_name = 'accounts/list_profiles.html'

class ShowCustomers(generic.ListView):
    model = models.Profile
    # permission_required = ("accounts.view_book_genre")
    # login_url = reverse_lazy('login')
    template_name = 'accounts/list_profiles_cust.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['customers'] = models.Profile.objects.filter(user__groups__name='Customers')
        return context

class ShowManagers(generic.ListView):
    model = models.Profile
    # permission_required = ("accounts.view_book_genre")
    # login_url = reverse_lazy('login')
    template_name = 'accounts/list_profiles_man.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['managers'] = models.Profile.objects.filter(user__groups__name='Managers')
        return context        

class ShowProfile(generic.DetailView):
    model = models.Profile
    template_name = 'accounts/detail_profile.html'

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from .forms import UserEditMultiForm

User = get_user_model()

class UpdateProfiles(UpdateView):
    model = User
    form_class = UserEditMultiForm
    template_name = 'accounts/update_profile.html'
    success_url = reverse_lazy('all-profiles')
    context_object_name='form_user'

    def get_form_kwargs(self):
        kwargs = super(UpdateProfiles, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object,
            'profile': self.object.profile,
        })
        kwargs.update({'active_user': self.request.user})
        return kwargs


     