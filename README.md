av_mopublic2geopackage
======================

gdal-dev
--------
Falls ein selber kompiliertes gdal/ogr verwendet wird, folgende Befehle sind in der Konsole auszuführen:

```
# catais.org (Ubuntu 10.04)
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/gdal/gdal-dev/lib
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.6/dist-packages/GDAL-2.0.0-py2.6-linux-x86_64.egg
```

```
# Virtualbox (Ubuntu 12.04)
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/stefan/Apps/gdal-dev/lib
export PYTHONPATH=$PYTHONPATH:/home/stefan/Apps/gdal-dev/lib/python2.7/site-packages
```
