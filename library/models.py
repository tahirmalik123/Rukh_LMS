from django.db import models


# Create your models here.

class AddBooks(models.Model):
    book_number = models.IntegerField(null=True, blank=True)
    version = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    book = models.ForeignKey(AddBooks, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    book = models.ForeignKey(AddBooks, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name
