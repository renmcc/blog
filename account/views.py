from django.contrib.auth import authenticate,login
from django.shortcuts import render,HttpResponse

# Create your views here.
from account.forms import RegistrationForm
from .forms import *

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            #不写入到数据库，生成用户对象
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('successfully')
        else:
            return HttpResponse('sorry, your can not register.')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {'form': user_form, 'profile':userprofile_form})
