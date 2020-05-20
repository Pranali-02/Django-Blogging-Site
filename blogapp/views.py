from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blogapp.forms import SignUpForm,postform
from blogapp.models import blogtable
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail


def blogstart(request):
    return render(request,'blogapp/logout.html')

@login_required
def bloghome(request):
    return render(request,'blogapp/home.html')


def postblog(request):
    form=postform()
    mydict={'form':form}
    if request.method=="POST":
        form=postform(request.POST,request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.Author=request.user
            data.save()
            mydict.update({'msg':'Post Registered Successfully'})

    return render(request,'blogapp/postblog.html',context=mydict)

def viewblog(request):
    blog=blogtable.objects.all().order_by('-upload_date')
    return render(request,'blogapp/viewblog.html',{'blog':blog})

def detailview(request,id):
    detail=blogtable.objects.get(id=id)
    mydict={'detail':detail}
    return render(request,'blogapp/detailview.html',context=mydict)

def deleteblog(request,id):
    detail=blogtable.objects.get(id=id)
    detail.delete()
    blog=blogtable.objects.all().order_by('-upload_date')
    return render(request,'blogapp/viewblog.html',{'blog':blog,'msg':'Blog Deleted Successfully'})









def SignUpPage(request):
    form=SignUpForm()
    mydict={'form':form}
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            subject="Blogging Site Mail"
            message="Welcome "+user.first_name+",You are register"
            recipient=[user.email]
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient)
            print('Registered Successfully')
            mydict.update({'msg':'SignedUp Successfully'})
    return render(request,'blogapp/signupform.html',context=mydict)
