from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.forms.models import model_to_dict
from mir.forms import *
from mir.models import *
from django.http import HttpResponse, Http404
import json

def home(request):
    return render(request, 'mir/home.html', {})

