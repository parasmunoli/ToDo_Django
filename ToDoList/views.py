from django.shortcuts import render, redirect
from .models import User, Task
from .forms import SignupForm, LoginForm, TaskForm
from django.http import JsonResponse

def status(request):
    return JsonResponse({'success': True, 'code': 200})
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'todolist/signup.html', {'form': form})

def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                request.session['user_id'] = user.userID
                return redirect('dashboard')
            except User.DoesNotExist:
                error = "Invalid username or password."
    else:
        form = LoginForm()
    return render(request, 'todolist/login.html', {'form': form, 'error': error})

def logout_view(request):
    request.session.flush()
    return redirect('login')

def dashboard_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = User.objects.get(pk=user_id)
    tasks = Task.objects.filter(user=user)

    if request.method == 'POST':
        if 'add_task' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = user
                task.save()
                return redirect('dashboard')
        elif 'toggle_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = Task.objects.get(taskID=task_id, user=user)
            task.completed = not task.completed
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'todolist/dashboard.html', {'user': user, 'tasks': tasks, 'form': form})

