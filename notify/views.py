from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TabletForm, UserTabletForm
from .models import Tablet, UserTablet
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


@login_required
def add_tablet(request):
    tablet_form = TabletForm()
    if request.method == 'POST':
        form = TabletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a success page or list of tablets
    else:
        form = TabletForm()
    return render(request, 'notify/add_tablet.html', {'tablet_form': tablet_form})

@login_required
def record_user_tablet(request):
    user_tablet_form = UserTabletForm()
    if request.method == 'POST':
        form = UserTabletForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user  # Set the current user
            form.save()
            return redirect('dashboard')  # Redirect to a success page or list of user-tablets
    else:
        form = UserTabletForm()
    return render(request, 'notify/record_tablet.html', {'user_tablet_form': user_tablet_form})

@login_required
def dashboard(request):
    tablets = Tablet.objects.all()
    user_tablets = UserTablet.objects.filter(user=request.user)
    
    tablet_form = TabletForm()
    user_tablet_form = UserTabletForm()

    context = {
        'tablets': tablets,
        'user_tablets': user_tablets,
        'tablet_form': tablet_form,
        'user_tablet_form': user_tablet_form,
        'user': request.user
    }
    return render(request, 'notify/dashboard.html', context)