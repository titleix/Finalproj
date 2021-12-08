from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import todoform, userProfile, UserRegistrationForm, CommentForm, CreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Todo, Profile, Forum


def User(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login/login.html', context)


def home(request):
    forums = Forum.objects.order_by('date_created')
    discussions = []
    for i in forums:
        discussions.append(i.comment_set.all())
    context = {'forums': forums,
               'discussions': discussions}
    return render(request, 'login/home.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'forms': form}
    return render(request, 'login/sign_up.html', context)


@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def planner(request):
    tasks = Todo.objects.filter(user=request.user)
    form = todoform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('planner')

    context = {'form': form, 'tasks': tasks}
    return render(request, 'login/planner.html', context)


@login_required(login_url='login')
def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'login/create.html', context)


@login_required(login_url='login')
def comment(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'login/comment.html', context)


@login_required(login_url='login')
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('planner')



