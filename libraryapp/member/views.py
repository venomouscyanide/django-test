from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Member
from .forms import MemberForm

# Create your views here.
class MemberListView(ListView):
    model = Member
    
    queryset = Member.objects.all()
    template_name = 'member_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_active_records'] = self.queryset.count()
        return context

class MemberCreateView(CreateView):
    model = Member
    template_name = 'member_create.html'
    form_class = MemberForm
    success_url = '/member'

class MemberUpdateView(UpdateView):
    model = Member
    template_name = 'member_edit.html'
    form_class = MemberForm
    success_url = '/member'

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'member_delete.html'
    success_url = '/member'
