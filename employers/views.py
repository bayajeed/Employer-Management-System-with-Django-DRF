from rest_framework import generics, permissions
from .models import Employer
from .serializers import EmployerSerializer
from .permissions import IsOwner

class EmployerListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    lookup_field = 'id'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)
    


from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employer
from .forms import EmployerForm

class EmployerListView(LoginRequiredMixin, ListView):
    model = Employer
    template_name = 'employers/employer_list.html'
    context_object_name = 'employers'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

class EmployerCreateView(LoginRequiredMixin, CreateView):
    model = Employer
    form_class = EmployerForm
    template_name = 'employers/employer_form.html'
    success_url = reverse_lazy('employer-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EmployerUpdateView(LoginRequiredMixin, UpdateView):
    model = Employer
    form_class = EmployerForm
    template_name = 'employers/employer_form.html'
    success_url = reverse_lazy('employer-list')

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

class EmployerDetailView(LoginRequiredMixin, DetailView):
    model = Employer
    template_name = 'employers/employer_detail.html'
    context_object_name = 'employer'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

class EmployerDeleteView(LoginRequiredMixin, DeleteView):
    model = Employer
    template_name = 'employers/employer_confirm_delete.html'
    success_url = reverse_lazy('employer-list')
    context_object_name = 'employer'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)