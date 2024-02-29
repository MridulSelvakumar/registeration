from django.shortcuts import render

# Create your views here.

from app.form import *

from django.http import HttpResponse

def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('regsistration',
            ' Thank U ur Registration is scuccessfull',
            'mridul07adih@gmail.com',
            [MUFDO.email],
            fail_silently=False,
            )
            return HttpResponse('Registartion Is Successfull')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'register.html',d)
