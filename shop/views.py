from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from shop.models import Tidings, TidingsForm, RegisterUserForm, LoginUserForm, TidingsFormEdit


def index(request):
    if request.path_info == '/home/filter':
        filter = True
    else:
        filter = False

    if request.GET.get('search') is not None:
        if filter:
            contact_list = Tidings.objects.filter(title__icontains=request.GET.get('search'),username=request.user.username).order_by('-time_upate')
        else:
         contact_list = Tidings.objects.filter(title__icontains=request.GET.get('search')).order_by('-time_upate')
    else:
        if filter:
            contact_list = Tidings.objects.filter(username=request.user.username).order_by('-time_upate')
        else:
            contact_list = Tidings.objects.all().order_by('-time_upate')
    paginator = Paginator(contact_list, 4)

    if request.GET.get('page') is not None:
        page_number = request.GET.get('page')
    else:
        page_number = 1

    page_obj = paginator.get_page(page_number)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
    return render(request, 'shop/index.html', {'title': 'Главная', 'page_obj': page_obj, 'filter': filter ,
                                               'parament_search':request.GET.get('search')})


class NewsUpdateView(UpdateView):
    form_class = TidingsFormEdit
    model = Tidings
    template_name = 'shop/edit.html'



def modal(request):
    data = {
        'title': 'modal'
    }
    return render(request, 'shop/modal.html', data)


def create(request):
    error = ''
    if request.method == "POST":
        data_form = {
            'title': request.POST['title'],
            'content': request.POST['content'],
            'username': request.user.username,
        }
        form = TidingsForm(data_form, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = form.errors

    form = TidingsForm()
    data = {
        'title': 'Create',
        'form': form,
        "error": error
    }
    return render(request, 'shop/create.html', data)


class DeleteForm(DeleteView):
    model = Tidings
    template_name = 'shop/delete.html'
    success_url = reverse_lazy('home')


def testing(request):
    return render(request, 'shop/testing.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request,'shop/profile.html')