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
import sys
sys.path.append(sys.path[0] + '\\mir\\mirsrc')
from MIR_Dict_MainBatch import MainBatch

def home(request):
    context = {}
    context['datasetnames'] = readFile('mir/static/datasetnames')
    return render(request, 'mir/home.html', context)

def readFile(filename):
    datafile = open(filename, "r")
    data_raw = datafile.readlines()
    datafile.close()
    datasetnames = [x.strip().split('.')[0] for x in data_raw]
    return datasetnames

def parseResult(request):
    context = {}
    if 'dataset' not in request.GET or not request.GET['dataset']:
        context['err_msg'] = 'Choose a dataset!'
        context['datasetnames'] = readFile('mir/static/datasetnames')
        return render(request, 'mir/home.html', context)
    dataset = 'mir/static/datasets/' + request.GET['dataset'] + '.txt'
    context['dataset'] = request.GET['dataset'] + '.txt'
    context['totalNumBin'], context['utilization'], context['jobList'], context['binList'], context['fullJobList'] = MainBatch(dataset)
    return render(request, 'mir/result.html', context)
