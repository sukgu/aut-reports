'''
Created on 03-Mar-2019

@author: sushil
'''
from django.views.generic import TemplateView
from auth.models import TokenModel
from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from allauth.socialaccount.models import SocialAccount

class Home(TemplateView):
    template_name = 'home.html'

@method_decorator(login_required, name="dispatch")   
class App(TemplateView):
    models = TokenModel
    template_name = 'app/home.html'
    
    def get(self, request, *args, **kwargs):
        data=SocialAccount.objects.get(user=request.user)
        provider=data.provider
        return render(request,self.template_name,{'user_data':data.extra_data,'provider':provider})
        
        
    
    
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(label='Email')  
    comment = forms.CharField(widget=forms.Textarea)
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
    
class ContactView(FormView):
    template_name = 'about/contact.html'
    form_class = ContactForm
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    