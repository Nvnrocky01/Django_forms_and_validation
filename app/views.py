from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *

def schoolform(request):
    esfo=School_form()
    d={'esfo':esfo}
    if request.method=='POST':
        sfdo=School_form(request.POST)
        if sfdo.is_valid():
            sn=sfdo.cleaned_data['Sname']
            sp=sfdo.cleaned_data['Sprinciple']
            sl=sfdo.cleaned_data['Slocation']
            se=sfdo.cleaned_data['semail']
            re=sfdo.cleaned_data['remail']
            so=School.objects.get_or_create(Sname=sn,Sprinciple=sp,Slocation=sl,semail=se,remail=re)[0]
            so.save()
            qlso=School.objects.all()
            d1={'school':qlso}
            return render(request,'display_school_details.html',d1)
    return render(request,'djforms.html',d)


