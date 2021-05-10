from django.shortcuts import render

from django.db import reset_queries
from django.db.models.fields import CharField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http.response import StreamingHttpResponse, HttpResponse
from django.contrib.auth.models import Group
from . import models
from evaluatorApp import models as ea_models
# from django.contrib.auth import logout

# Create your views here.


def register(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        roll_no = request.POST.get('roll_no')
        college_name = request.POST.get('college_name')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        dob = request.POST.get('dob')
        subject_code = request.POST.get('subject_code')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()

                userDetail = models.UserDetails(user=user, roll_no=roll_no, college_name=college_name,
                                                branch=branch, semester=semester, dob=dob, subject_code=ea_models.SubjectCode.objects.get(section_name=subject_code))
                userDetail.save()

                print('user created')
        else:
            messages.info(request, "Password is not matching")
            return redirect('register')

        return redirect('login')
    else:
        sections = list(ea_models.SubjectCode.objects.all())
        return render(request, 'register.html', context={'sections': sections})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['section'] = models.UserDetails.objects.get(
                user=user).subject_code.section_name
            print(request.session['section'])
            return redirect('open-test')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
