from django.shortcuts import render, redirect

from home.forms import doctorlogin
from home.models import doctor


def doctordashboard(request):
    return render(request,'doctor/doctorbase.html')

def doc_view(request):
    data = doctor.objects.all()
    return render(request, 'admin1/doc_list.html', {'data': data})


def doc_delete(request,id):
    data = doctor.objects.get(id=id)
    data.delete()

    return redirect('doc_view')


def update(request, id):
    data = doctor.objects.get(id=id)
    form = doctorlogin(instance=data)
    if request.method == 'POST':
        form = doctorlogin(request, instance=id)
        if form.is_valid():
            form.save()
            return redirect(doc_view)
    return render(request, 'admin1/doc_update.html', {'form': form})