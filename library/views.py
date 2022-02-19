from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, TemplateView
from .models import AddBooks, Student, Teacher


class HomeView(TemplateView):
    template_name = 'library/home.html'


class AddBooksView(CreateView):
    template_name = 'library/index.html'
    model = AddBooks
    fields = ['book_number', 'version', 'title', 'auther']

    def get_success_url(self):
        return reverse('view_books')


class BookListView(ListView):
    template_name = 'library/viewbooks.html'
    model = AddBooks

    def get_queryset(self):
        return self.model.objects.all()


class DeleteBookView(DeleteView):
    template_name = 'library/viewbooks.html'
    model = AddBooks

    def get_success_url(self):
        return reverse("view_books")


def delete_book(request, pk):
    book = AddBooks.objects.get(id=pk)
    book.delete()
    return redirect("view_books")

class IssueBookView(TemplateView):
    template_name = 'library/issue.html'


class BookForStudentView(CreateView):
    template_name = 'library/student.html'
    model = Student
    fields = ['book', 'name', 'department', 'semester', 'contact']

    def get_success_url(self):
        return reverse('home_page')


class BookForTeacherView(CreateView):
    template_name = 'library/teacher.html'
    model = Teacher
    fields = ['book', 'name', 'designation', 'faculty', 'contact']

    def get_success_url(self):
        return reverse('home_page')


class ReturnBookView(TemplateView):
    template_name = 'library/return_books.html'

    def post(self, return_book=None, **kwargs):
        book_name = self.request.POST.get("book_name")
        recepient_type = self.request.POST.get("recepient")
        if recepient_type.lower() == "teacher":
            return_book = Teacher.objects.filter(book__title=book_name)
        elif recepient_type.lower() == "student":
            return_book = Student.objects.filter(book__title=book_name)
        return_book.delete()
        return redirect("return_books")

