from django.http.response import HttpResponse
from django.shortcuts import render

from .models import User, Prac_icf
from .models import Prac_MMT_shoulder_right, Prac_MMT_shoulder_left
from .forms import NewUserForm, NewInputIcf
from .forms import PracMmtShoulderRight, PracMmtShoulderLeft


def users(request):

    user_model=User()
    icf_model=Prac_icf()
    user_form=NewUserForm()
    mmt_shoulder_right_form=PracMmtShoulderRight()
    mmt_shoulder_left_form=PracMmtShoulderLeft()
    icf_form=NewInputIcf()
    progress=1



    if request.method == 'POST' and progress == 0:

        user_form = NewUserForm(request.POST)

        if user_form.is_valid():
            user_model=User(diagnosis_name=user_form.cleaned_data['diagnosis_name'], filler=user_form.cleaned_data['filler'], date=user_form.cleaned_data['date'])
            user_model.save()
            progress+=1
            #Prac_icf.objects.create(id=user_model.id)
            icf_model=Prac_icf(id=user_model.id)
        else:
            print('ERROR FORM INVALID')


    if request.method == 'POST' and progress == 1:

        if 'mmt_shoulder_right_button' in request.POST:

            mmt_shoulder_right_form = PracMmtShoulderRight(request.POST)

            if mmt_shoulder_right_form.is_valid():
                Prac_MMT_shoulder_right.objects.create(id=user_model.id)
                model=Prac_MMT_shoulder_right(**mmt_shoulder_right_form.cleaned_data)
                model=Prac_MMT_shoulder_right.objects.get(id=user_model.id)
                model.save()
            else:
                print('ERROR FORM INVALID')

        if 'mmt_shoulder_left_button' in request.POST:

            mmt_shoulder_left_form = PracMmtShoulderLeft(request.POST)

            if mmt_shoulder_right_form.is_valid():
                Prac_MMT_shoulder_left.objects.create(id=user_model.id)
                model=Prac_MMT_shoulder_left(**mmt_shoulder_left_form.cleaned_data)
                model=Prac_MMT_shoulder_left.objects.get(id=user_model.id)
                model.save()
            else:
                print('ERROR FORM INVALID')

    if request.method == 'POST' and progress == 2:

        #icf_model=Prac_icf.objects.get(id=id)
        icf_form=NewInputIcf(request.POST)

        if icf_form.is_valid():

            icf_model=Prac_icf(body=icf_form.cleaned_data['body'], activity=icf_form.cleaned_data['activity'])
            icf_model.save()
            progress+=1
        else:
            print('ERROR FORM INVALID')




    d = {
      'user_form': user_form,
      'icf_form': icf_form,
      'mmt_shoulder_right_form': mmt_shoulder_right_form,
      'mmt_shoulder_left_form': mmt_shoulder_left_form,
      'progress': progress,
    }

    return render(request,'prac.html',d)
