from django.contrib import admin
from . import models
from django.shortcuts import redirect
from django import forms
from django.urls import path
import os
from django.contrib import messages
import io
# from .views import CsvUploader
from django.contrib.auth.models import Group
from .models import TestQuestionAnswer
from django.db.utils import IntegrityError
from django.core.exceptions import FieldDoesNotExist
from django.db import transaction
# Register your models here.
admin.site.register(models.Test)
admin.site.register(models.SubjectCode)
admin.site.register(models.Result)
admin.site.site_header = "Faculty Panel"
admin.site.unregister(Group)
# admin.site.unregister()
