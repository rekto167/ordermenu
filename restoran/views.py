from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView, CreateView, UpdateView, RedirectView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout

from .models import MenuModel
from .forms import MenuForm
# Create your views here.


class TambahMenuView(CreateView):
    model = MenuModel
    form_class = MenuForm
    template_name = "add_menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Tambah Menu'
        return context


class HapusMenuView(DeleteView):
    model = MenuModel
    template_name = 'delete.html'
    success_url = reverse_lazy('restoran:managemenu')


class IndexCustomerView(TemplateView):
    template_name = "index_customer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "HALAMAN CUSTOMER"
        return context


class IndexView(TemplateView):
    template_name = 'index_restoran.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'page_title': 'Home Restoran'
        }
        return context


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login,
                            password=password_login)
        if user.groups.filter(name='chef').exists() is True:
            login(request, user)
            return redirect('restoran:managemenu')
        elif user.groups.filter(name='customer').exists() is True:
            login(request, user)
            return redirect('restoran:ordermenu')
        else:
            return redirect('restoran:login')
        return render(request, 'login.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "LOGIN"
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('homepage')


class ManageMenuView(ListView):
    model = MenuModel
    context_object_name = 'ObjectMenuManage'
    template_name = "restoran/manage_menu.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Manage Menu"
        kwargs = self.kwargs
        return context


class OrderMenuView(ListView):
    model = MenuModel
    context_object_name = "ObjectListMenu"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Menu Orderan'
        kwargs = self.kwargs
        return context


class TambahMenuView(CreateView):
    form_class = MenuForm
    template_name = 'create.html'
