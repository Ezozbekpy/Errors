from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from base.models import Main
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')

class MainList(ListView):
    model = Main
    context_object_name = 'tasks'
    template_name = 'base/main.html'
class MainDetail(DetailView):
    model = Main
    context_object_name = 'tasks'

class TaskCreater(LoginRequiredMixin,CreateView):
    model = Main
    fields = '__all__'

    success_url = reverse_lazy('main')

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Main
    fields = '__all__'

    success_url = reverse_lazy('main')

class DeleteW(LoginRequiredMixin,DeleteView):
    model = Main
    context_object_name = 'taskss'
    success_url = reverse_lazy('main')