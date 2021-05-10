from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SubjectCode(models.Model):
    section_name = models.CharField(max_length=500)

    def __str__(self):
        return self.section_name


class Test(models.Model):
    test_Name = models.CharField(max_length=500)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    questions = models.FileField(upload_to='csv/', null=True)
    section = models.ForeignKey(
        SubjectCode, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.test_Name


class TestQuestionAnswer(models.Model):
    test_Name = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=6000)
    answer = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.test_Name} : {self.question}"


class UploadedFiles(models.Model):
    f = models.FileField(upload_to='csv/')


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    marks = models.CharField(max_length=500)
    section = models.ForeignKey(
        SubjectCode, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} : {self.test.test_Name}"


class Section(models.Model):
    sd = models.CharField(max_length=50, null=True, blank=True)
