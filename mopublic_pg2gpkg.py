#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import osgeo.gdal
from osgeo import ogr

# VARS
GPKG_DIR_LV03 = "/opt/Geodaten/ch/so/kva/av/mopublic/gpkg/lv03/d/"
GPKG_DIR_LV95 = "/opt/Geodaten/ch/so/kva/av/mopublic/gpkg/lv95/d/"
#GPKG_DIR_LV03 = "/home/stefan/tmp/"
#GPKG_DIR_LV95 = "/home/stefan/tmp/"
DB_HOST = "localhost"
DB_NAME_LV03 = "xanadu2"
DB_NAME_LV95 = "strelnikow"
DB_USER = "mspublic"
DB_PWD = "mspublic"
DB_SCHEMA = "av_mopublic"
GEM_GRE = "av_avdpool_ch.gemeindegrenzen_gemeindegrenze"

# Enable exceptions
ogr.UseExceptions() 

# ->Logfile
print osgeo.gdal.__version__


def export_communities(connString, outputDir):
    conn = ogr.Open(connString)
    for gem_bfs in gem_bfs_list:
        out = os.path.join(outputDir, str(gem_bfs) + ".gpkg")
        out_driver = ogr.GetDriverByName("GPKG")

        if os.path.exists(out):
            out_driver.DeleteDataSource(out)
            
        out_datasource = out_driver.CreateDataSource(out)
            
        for i in conn:
            daLayer = i.GetName()
            schema = daLayer.split(".")[0]
            layerName = daLayer.split(".")[1]
            if schema == DB_SCHEMA:
                lyr = conn.GetLayer(daLayer)
                lyr.SetAttributeFilter("bfsnr = " + str(gem_bfs))
                out_layer = out_datasource.CopyLayer(lyr, layerName)
                
        out_datasource.Destroy()
    conn.Destroy()


def export_canton(connString, outputDir):
    conn = ogr.Open(connString)

    out = os.path.join(outputDir,  "kanton.gpkg")
    out_driver = ogr.GetDriverByName("GPKG")

    if os.path.exists(out):
        out_driver.DeleteDataSource(out)

    out_datasource = out_driver.CreateDataSource(out)

    for i in conn:
        daLayer = i.GetName()
        schema = daLayer.split(".")[0]
        layerName = daLayer.split(".")[1]
        if schema == DB_SCHEMA:
            lyr = conn.GetLayer(daLayer)        
            out_layer = out_datasource.CopyLayer(lyr, layerName)

    out_datasource.Destroy()
    conn.Destroy()


# Get the new ones
connString = "PG: host=%s dbname=%s user=%s password=%s" %(DB_HOST, DB_NAME_LV03, DB_USER, DB_PWD)

conn = ogr.Open(connString)

gem_bfs_list = []
for i in conn:
    daLayer = i.GetName()
    if daLayer == GEM_GRE:
        lyr = conn.GetLayer(daLayer)
        lyr.SetAttributeFilter("lieferdatum = current_date")
        for feature in lyr:
            gem_bfs_list.append(feature.GetField("gem_bfs"))
        break
conn.Destroy()
    
connStringLV03 = "PG: host=%s dbname=%s user=%s password=%s" %(DB_HOST, DB_NAME_LV03, DB_USER, DB_PWD)
connStringLV95 = "PG: host=%s dbname=%s user=%s password=%s" %(DB_HOST, DB_NAME_LV95, DB_USER, DB_PWD)
    
export_communities(connStringLV03, GPKG_DIR_LV03)
export_communities(connStringLV95, GPKG_DIR_LV95)

export_canton(connStringLV03, GPKG_DIR_LV03)
export_canton(connStringLV95, GPKG_DIR_LV95)


# use "GetLayerByName" for geometryless tables (metadata)

