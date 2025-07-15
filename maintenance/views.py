from django.shortcuts import render, redirect
from .models import MaintenanceRequest
from .forms import MaintenanceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('submit')
    else:
        form = MaintenanceRequestForm()
    return render(request, 'maintenance/form.html', {'form': form})


def view_requests(request):
    requests = MaintenanceRequest.objects.all().order_by('-timestamp')
    return render(request, 'maintenance/view_requests.html', {'requests': requests})
