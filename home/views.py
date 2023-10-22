from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contacts, event
from .models import snp, forum, prk, trck, alert
from django.contrib import messages
from django.urls import reverse
#from . import populate_prk_data

email1 = "ok"

def book(request, id):
    if id == 1:
        w1 = 'A'
    elif id ==2:
        w1 = 'B'
    elif id ==3:
        w1 = 'C'
    elif id ==4:
        w1 = 'D'
    elif id ==5:
        w1 = 'E'
    elif id ==6:
        w1 = 'F'
    p = prk.objects.filter(wing=w1)

    return render(request, 'book.html',{'p':p})
def forum_index(request):
    post_list = forum.objects.all()
    return render(request, 'forum_index.html',{'post_list':post_list})

def planner(request):
    si = snp.objects.get(email=email1)
    un = si.name
    return render(request, 'planner.html',{'un':un})

def del_post(request, id):
    global email1
    post_dlist = forum.objects.filter(id=id)
    sample_instance = forum.objects.get(id=id)
    f = sample_instance.mail
    if f == email1:
        post_dlist.delete()
        messages.success(request, "Deletion was a success. Please return to see changes.")
    else:
        messages.success(request, "Aukat dekh apni.")
    return HttpResponseRedirect(reverse('forum_index'))



def post_detail(request, id):
    posts = forum.objects.filter(id=id)
    return render(request, 'post_detail.html',{'posts':posts} )

def index(request):
    cont = snp.objects.all()
    global email1
    co = snp.objects.filter(email=email1, priv=1)
    if co.exists():
        a = 1
    hd = alert.objects.get(disp=True)
    return render(request, 'index.html', {'cont': cont, 'a':a, 'hd':hd})

def c_forum(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        topic = request.POST.get('topic')
        cata = request.POST.get('cata')
        body = request.POST.get('body')
        email = email1
        c_forum = forum(topic=topic, name=name,  cata=cata, body=body, mail=email)
        c_forum.save()
        messages.success(request, "Your Forum has been completed Successfully.")
    return render(request, 'c_forum.html')

def d_forum(request):
    f = forum.objects.all()
    return render(request, 'forum.html', {'f':f})


def about(request):

    return render(request, 'about.html')


def profile(request):
    bo = False
    co = snp.objects.filter(email=email1, priv=1)
    if co.exists():
        bo = True
    d = snp.objects.filter(email=email1)
    if d.exists():
        return render(request, 'profile.html', {'d': d, 'bo':bo})
    # return HttpResponse("This is Services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contacts(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")


def singup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        chi = request.POST.get('checks')
        pswd = request.POST.get('pswd')
        singup = snp(name=name, email=email, phno=phno, pswd=pswd, priv=chi)
        singup.save()
        messages.success(request, "Hogaya bro.")
    return render(request, 'singup.html')


def login(request):
    a = 0
    global email1
    if request.method == 'POST':
        email1 = request.POST.get('email')
        pswd1 = request.POST.get('pswd')
        if snp.objects.filter(email=email1, pswd=pswd1).exists():
            messages.success(request, "Login Successful, Welcome.")
            cont = snp.objects.all()
            co = snp.objects.filter(email=email1, priv=1)
            hd = alert.objects.get(disp=True)
            if co.exists():
                a = 1
            return render(request, 'index.html', {'cont': cont,'a':a,'hd':hd})
        else:
            return HttpResponse("You have entered the wrong password")
    return render(request, 'login.html')


def cal(request, id):
    pl = event.objects.filter(month=id, email=email1)
    return render(request, 'cal.html', {'pl':pl})

def plan(request):
    return render(request, 'plan.html')

def c_plan(request):
    if request.method == "POST":
        head = request.POST.get('head')
        mon = request.POST.get('mon')
        day = request.POST.get('day')
        body = request.POST.get('body')
        cpi = event(head=head,email=email1, month=mon, date=day, body=body, created_at=datetime.today())
        cpi.save()
        messages.success(request, "Your event has been created :)")
    return render(request, 'c_plan.html')

def del_plan(request, id):
    pdl = event.objects.filter(id=id)
    pdl.delete()
    messages.success(request, "Deletion was a success. Please return to see changes.")
    return render(request, 'cal.html')

def tem(request):
    alotpark = 0
    if request.method == "POST":
        name = request.POST.get('name')
        fltn = request.POST.get('fltn')
        phno = request.POST.get('phone')
        altp = request.POST.get('altp')
        ch = request.POST.get('checks')
        wi = request.POST.get('inputGroupSelect01')
        res = False
        prka = prk.objects.filter(fltn=str(fltn), wing=str(wi))
        for i in prka:
            a1 = i.prkno
        if ch==1:
            res = True
        if ch==0:
            res = False
        ent = trck(name=name, phno=phno, fltn=fltn, intime=datetime.today(), wi=wi, altp=altp, res=res, alotpark=a1)
        ent.save()
        alotpark = a1
        messages.success(request, "Your alloted parking is {} for duration {}.".format(alotpark,altp))

        return render(request, 'tem.html', {'alotpark':alotpark})
    return render(request, 'tem.html',{'alotpark':alotpark})

def test(request):
    return render(request, 'test.html')

def admin_panel(request):
    if request.method == "POST":
        topic = request.POST.get('heading')
        body = request.POST.get('desc')
        svc = alert(topic=topic,body=body)
        svc.save()
    al = alert.objects.all()
    return render(request, 'admin_panel.html', {'al':al})

def del_alert(request, id):
    Alert = alert.objects.all()
    adl = alert.objects.filter(id=id)
    if adl.exists():
        adl.delete()
        bo = False
        co = snp.objects.filter(email=email1, priv=1)
        if co.exists():
            bo = True
        d = snp.objects.filter(email=email1)
        if d.exists():
            return render(request, 'profile.html', {'d': d, 'bo': bo})
            messages.success(request, "Deletion was a success. Please return to see changes.")
    return render(request, 'admin_panel.html', {'adl': adl, 'Alert':Alert})

def setact(request, id):
    alert.objects.filter(disp=True).update(disp=False)
    alert.objects.filter(id=id).update(disp=True)
    bo = False
    co = snp.objects.filter(email=email1, priv=1)
    if co.exists():
        bo = True
    d = snp.objects.filter(email=email1)
    if d.exists():
        return render(request, 'profile.html', {'d': d, 'bo': bo})

def setinact(request, id):
    cu = alert.objects.get(id=id)
    if cu.disp == True:
        alert.objects.filter(disp=True).update(disp=False)
        alert.objects.filter(id=10).update(disp=True)
    bo = False
    co = snp.objects.filter(email=email1, priv=1)
    if co.exists():
        bo = True
    d = snp.objects.filter(email=email1)
    if d.exists():
        return render(request, 'profile.html', {'d': d, 'bo': bo})