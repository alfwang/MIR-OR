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
sys.path.append(sys.path[0] + '/mir/mirsrc')
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
    context['utilization'], context['jobList'], binList, fullJobList = MainBatch(dataset)
    
    context['binNum'] = len(binList)
    context['binW'], context['binH'] = binList[0].dimension[0], binList[0].dimension[1]
    binIndex = [i * (context['binH'] + 20) + 500 for i in range(len(binList))]
    jobReady = parseJobList(fullJobList, context['binNum'], context['binH'])
    context['bins'] = [[x] + [y] for x, y in zip(binIndex, jobReady)]
    # print "############", context['bins']



    return render(request, 'mir/result.html', context)

def parseJobList(fullJobList, binNum, H):
    jobReady = [[] for i in range(binNum)]
    for x in fullJobList:
        # print x.index, x.coord
        jobCoord, jobCat, w, h = x.coord[:2], x.coord[2], x.dimension[0], x.dimension[1]
        if jobCat == 1:
            jobCoord = [H - jobCoord[1] - h, jobCoord[0]]
        elif jobCat == 2:
            jobCoord = [H - jobCoord[1], jobCoord[0]]
        elif jobCat == 3:
            jobCoord = [H - jobCoord[1], jobCoord[0] - w]
        elif jobCat == 4:
            jobCoord = [H - jobCoord[1] - h, jobCoord[0] - w]
        jobReady[x.bin - 1].append([x.index, jobCoord[0], jobCoord[1], w, h])
        # print jobCoord
    # return [[[jobs[i] for jobs in oneBin] for i in range(5)] for oneBin in jobReady]
    return jobReady
