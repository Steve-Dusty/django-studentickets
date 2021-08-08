from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from .models import Class, Student


class HomePageView(TemplateView):
    template_name = "home.html"


class ClassListView(ListView):
    model = Class
    template_name = "dashboard.html"


class ClassDetailView(DetailView):
    model = Class
    template_name = "classdetail.html"


class ClassCreateView(CreateView):
    model = Class
    template_name = "createclass.html"
    fields = ['class_name']

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)


class ClassDeleteView(DeleteView):
    model = Class
    success_url = "/dashboard"


class ClassStudentCreateView(CreateView):
    model = Student
    template_name = "addstudent.html"
    fields = ['student_name']

    def form_valid(self, form):
        self.class_name_id = self.kwargs['pk']
        class_name = Class.objects.get(id=self.class_name_id)
        form.instance.class_name = class_name
        form.instance.tickets = 0
        return super().form_valid(form)


class ClassStudentDeleteView(DeleteView):
    model = Student

    def get_success_url(self):
        return reverse('class-student-list', kwargs={'pk': self.object.class_name_id})


class ClassNameEditView(UpdateView):
    model = Class
    template_name = "editclassname.html"
    fields = ['class_name']
    success_url = "/dashboard"


def add_ticket(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    Student.objects.filter(
        pk=student_id).update(tickets=F('tickets')+1)
    return redirect('class-student-list', pk=student.class_name_id)


def delete_ticket(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    Student.objects.filter(
        pk=student_id).update(tickets=F('tickets')-1)
    return redirect('class-student-list', pk=student.class_name_id)
