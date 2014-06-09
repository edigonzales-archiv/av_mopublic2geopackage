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

cronjob
-------
Für den Cronjob wurde noch ein kleines Shellskript `mopublic2gpkg.sh` geschrieben und die erste Zeile (`#!/usr/bin/env python`) gelöscht. Das Shellskript selbst wird momentan im Importskript (Bundesmodell) ausgeführt. Falls Cronjob nicht läuft:

1. Cronjob jede Minute ausführen, dh. `* * * * * ....` (Achtung falls er dann funktioniert!!)
2. `* * * * * /home/avdpool/Apps/av_avdpool_ch/mopublic2gpkg.sh >> /tmp/out.txt 2>&1`
3. Output in der Datei out.txt anschauen.
