from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, View, TemplateView, UpdateView,ListView
from django.urls import reverse
from .models import TeacherRegister, Help, ContactUs
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        institute = request.POST['institute']
        email = request.POST['email']
        phone = request.POST['phone']

        if name =='' or email =='' or len(phone)<11 or institute =='':
            messages.error(request, "Please fill the form correctly")
        else:
            home = TeacherRegister(name=name, institute=institute, email=email, phone=phone)
            home.save()
            messages.success(request, "Your request has been sent successfully. You will get a confirmation mail in 24hours")
    return render(request, 'users/home.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'users/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TermsConditions(TemplateView):
    template_name = 'users/terms_conditions.html'


class Privacy(TemplateView):
    template_name = 'users/privacy.html'


class HelpView(ListView):
    context_object_name = 'help_view'
    model = Help
    template_name = 'users/help.html'


class HelpDescribe(TemplateView):
    template_name = 'users/helpdescribe.html'


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        describe = request.POST.get('describe', "")

        if name =='' or email =='' or describe =='':
            messages.error(request, "Please fill the form correctly")
        else:
            contact = ContactUs(name=name, email=email, describe=describe)
            contact.save()
            messages.success(request, "Your message has been sent successfully. You will get reply through a mail")
    return render(request, 'users/contact.html')
