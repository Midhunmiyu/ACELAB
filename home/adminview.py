from django.shortcuts import redirect, render
from home.forms import departmentform
from home.models import department


def admindashboard(request):
    return render(request, 'admin1/admindashboard.html')


def add_department(request):
    form = departmentform()
    if request.method == 'POST':
        form = departmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_department')
    return render(request, 'admin1/adddepartments.html', {'form': form})


def view_department(request):
    data = department.objects.all()
    return render(request, 'admin1/viewdepartments.html', {'data': data})


def delete(request, id):
    data = department.objects.get(id=id)
    data.delete()

    return redirect('view_department')
