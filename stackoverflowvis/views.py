from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic




def indexViews(request): 
      
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "index.html")


def heatMapView(request):

    return render(request, "heatmap.html")


def graphView(request):

    return render(request, "controls.html")

def chartView(request):

    return render(request, "temp.html")

def chartTempView(request):
    return render(request, "chart.html")

def chart2TempView(request):
    return render(request, "chart2.html")

def aboutView(request):
    return render(request, "about.html")

def worldmapView(request):
    return render(request, 'worldmap.html')

def tableTitleView(request):
    return render(request, 'table-titles.html')

def tableFeatureView(request):
    return render(request, 'table-features.html')

def tagCloudView(request):
    return render(request, 'tag-cloud.html')

def pieChartView(request):
    return render(request, 'piechart.html')

def clusterView(request):
    return render(request, 'cluster.html')