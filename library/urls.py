from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('add-books/', views.AddBooksView.as_view(), name="add_books"),
    path('student-books/', views.BookForStudentView.as_view(), name="student_books"),
    path('teacher-books/', views.BookForTeacherView.as_view(), name="teacher_books"),
    path('return-books/', views.ReturnBookView.as_view(), name="return_books"),
    path('view-books/', views.BookListView.as_view(), name="view_books"),
    path('issue-book/', views.IssueBookView.as_view(), name="issue_book"),
    path('delete-books/<int:pk>', views.delete_book, name="delete_book"),
]
