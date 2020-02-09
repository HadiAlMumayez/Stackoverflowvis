from django.contrib import admin 
from django.urls import path 

# importing views from views..py 
from .views import indexViews, heatMapView, graphView, chartView, chartTempView, aboutView, worldmapView, \
    tableTitleView, tableFeatureView, tagCloudView, pieChartView,clusterView,chart2TempView

urlpatterns = [ 
	path('', indexViews),
    path('heatmap', heatMapView),
    path('graph', graphView),
    path('chart', chart2TempView),
    path('chartTemp', chartTempView),
    path('chart-2', chartView),
    path('about', aboutView),
    path('worldmap', worldmapView),
    path('table-titles', tableTitleView),
    path('table-features', tableFeatureView),
    path('tag-cloud', tagCloudView),
    path('piechart', pieChartView),
    path('cluster', clusterView),


]
