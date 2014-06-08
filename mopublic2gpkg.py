#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import osgeo.gdal
from osgeo import ogr


# VARS
GPKG_DIR = "/tmp/"

# Enable exceptions
ogr.UseExceptions() 

# ->Logfile
print osgeo.gdal.__version__

# Get all the layer names
layer_list = []
driver = ogr.GetDriverByName('WFS')
ds_mopublic = driver.Open("WFS:http://www.catais.org/wfs/mopublic?")

for i in range(0, ds_mopublic.GetLayerCount()):
    layer = ds_mopublic.GetLayerByIndex(i)
    layer_list.append(layer.GetName())

ds_mopublic.Destroy()

# -> Logfile
print layer_list



#wfs = driver.Open("WFS:http://www.catais.org/wfs/mopublic?TYPENAME=hoheitsgrenzen__gemeindegrenze&FILTER=<PropertyIsEqualTo><PropertyName>bfsnr</PropertyName><Literal>2549</Literal></PropertyIsEqualTo>")
#wfs = driver.Open("WFS:http://www.catais.org/wfs/mopublic?TYPENAME=hoheitsgrenzen__gemeindegrenze&FILTER=%3Cogc:Filter%20xmlns:ogc=%22http://www.opengis.net/ogc%22%3E%0A%20%3Cogc:PropertyIsEqualTo%3E%0A%20%20%3Cogc:PropertyName%3Ebfsnr%3C/ogc:PropertyName%3E%0A%20%20%3Cogc:Literal%3E2549%3C/ogc:Literal%3E%0A%20%3C/ogc:PropertyIsEqualTo%3E%0A%3C/ogc:Filter%3E%0A")
#wfs = driver.Open("WFS:http://www.catais.org/wfs/mopublic?TYPENAME=bodenbedeckung__boflaeche&FILTER=%3Cogc:Filter%20xmlns:ogc=%22http://www.opengis.net/ogc%22%3E%0A%20%3Cogc:PropertyIsEqualTo%3E%0A%20%20%3Cogc:PropertyName%3Ebfsnr%3C/ogc:PropertyName%3E%0A%20%20%3Cogc:Literal%3E2601%3C/ogc:Literal%3E%0A%20%3C/ogc:PropertyIsEqualTo%3E%0A%3C/ogc:Filter%3E%0A")
#ds_lieferungen = driver.Open("WFS:http://www.catais.org/wfs/av_lieferungen?")
#layer_lieferungen = ds_lieferungen.GetLayerByName('lieferungen')
#
#for feature in layer_lieferungen:
#    gem_bfs = feature.GetField('gem_bfs')
#    print gem_bfs
#    
#    out = os.path.join(GPKG_DIR, str(gem_bfs) + ".gpkg")
#    out_driver = ogr.GetDriverByName("GPKG")
#
#    if os.path.exists(out):
#        out_driver.DeleteDataSource(out)
#
#    out_datasource = out_driver.CreateDataSource(out)
#
#    filter = "&FILTER=%3Cogc:Filter%20xmlns:ogc=%22http://www.opengis.net/ogc%22%3E%0A%20%3Cogc:PropertyIsEqualTo%3E%0A%20%20%3Cogc:PropertyName%3Ebfsnr%3C/ogc:PropertyName%3E%0A%20%20%3Cogc:Literal%3E" + str(gem_bfs) + "%3C/ogc:Literal%3E%0A%20%3C/ogc:PropertyIsEqualTo%3E%0A%3C/ogc:Filter%3E%0A"
#
#    for i in range(len(layer_list)):
#        wfs_string = "WFS:http://www.catais.org/wfs/mopublic?TYPENAME" + layer_list[i] + filter
#        ds_mopublic = driver.Open(wfs_string)
#        layer_mopublic = ds_mopublic.GetLayerByName(layer_list[i])
#        out_layer = out_datasource.CopyLayer(layer_mopublic, layer_list[i])
#
#        ds_mopublic.Destroy()
#
#ds_lieferungen.Destroy()


# Export whole canton
ds_mopublic = driver.Open("WFS:http://www.catais.org/wfs/mopublic?")

out = os.path.join(GPKG_DIR,  "kanton.gpkg")
out_driver = ogr.GetDriverByName("GPKG")

if os.path.exists(out):
    out_driver.DeleteDataSource(out)

out_datasource = out_driver.CreateDataSource(out)

for i in range(len(layer_list)):
    layer_mopublic = ds_mopublic.GetLayerByName(layer_list[i])
    out_layer = out_datasource.CopyLayer(layer_mopublic, layer_list[i])

ds_mopublic.Destroy()


#for i in range(0, wfs.GetLayerCount()):
#  layer = wfs.GetLayerByIndex(i)
#  sr = layer.GetSpatialRef()
#  print 'Layer: %s, SR: %s...' % (layer.GetName(), sr.ExportToWkt()[0:50])


#layer = wfs.GetLayerByName('hoheitsgrenzen__gemeindegrenze')
#layer = wfs.GetLayer(0)
#for feature in layer:
    #print 'Json representation for Feature: %s' % feature.GetFID()
    #print feature.ExportToJson()
    
#cnt = ogr.GetDriverCount()
#formatsList = []  # Empty List

#for i in range(cnt):
#    driver = ogr.GetDriver(i)
#    driverName = driver.GetName()
#    if not driverName in formatsList:
#        formatsList.append(driverName)

#formatsList.sort() # Sorting the messy list of ogr drivers

#for i in formatsList:
#    print i    
    
#out = "/home/stefan/Projekte/GeoPackage/test7.gpkg"
#outDriver = ogr.GetDriverByName("GPKG")
#
#if os.path.exists(out):
#    outDriver.DeleteDataSource(out)
#
#outDataSource = outDriver.CreateDataSource(out)
#outLayer = outDataSource.CopyLayer(layer,'test4')

#layer = wfs.GetLayerByName('hoheitsgrenzen__hoheitsgrenzpunkt')
#layer = wfs.ExecuteSQL("select * from hoheitsgrenzen__hoheitsgrenzpunkt WHERE bfsnr = 2601")
#layer.SetAttributeFilter("bfsnr = 2601")
#outLayer = outDataSource.CopyLayer(layer,'test7')


#layer = wfs.GetLayerByName('bodenbedeckung__boflaeche')
#layer.SetAttributeFilter("bfsnr = 2601")
#outLayer = outDataSource.CopyLayer(layer,'foo4')
