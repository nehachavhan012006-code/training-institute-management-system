from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == 'super_admin':
                return redirect('/')

            elif user.role == 'admin':
                return redirect('/')

            elif user.role == 'trainer':
                return redirect('/trainer-dashboard/')

            elif user.role == 'student':
                return redirect('/student-dashboard/')

    return render(request, 'users/login.html')

def trainer_dashboard(request):
    return render(request, 'users/trainer_dashboard.html')


def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')