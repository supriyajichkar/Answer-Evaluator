from django.db import models
from django.contrib.auth.models import User
from evaluatorApp import models as ea_models


# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=500)
    college_name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    semester = models.CharField(max_length=500)
    dob = models.DateField(max_length=500)
    subject_code = models.ForeignKey(
        ea_models.SubjectCode, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
