from django.shortcuts import render
from .models import detail

def submit(request):
    name = request.GET.get('name')
    fname = request.GET.get('fname')
    course = request.GET.get('Course')
    phone = request.GET.get('telephone')
    detailed = detail()
    detailed.cname = name
    detailed.cfname = fname
    detailed.ccourse = course
    detailed.cphone = phone
    detailed.save()
    sno = detailed.sno
    param = {'name': name, 'fname': fname, 'course':course, 'phone':phone, 'sno': sno}
    print(param)
    return render(request, 'thakyou.html', param)
def update(request):
    sno = request.GET.get('sno')
    name = request.GET.get('name')
    fname = request.GET.get('fname')
    course = request.GET.get('Course')
    phone = request.GET.get('telephone')
    upd = detail.objects.get(pk = sno)
    upd.cname = name
    upd.cfname = fname
    upd.ccourse = course
    upd.cphone = phone
    upd.save()
    param = {'name': name, 'fname': fname, 'course':course, 'phone':phone}
    return render(request, 'thakyou.html', param)