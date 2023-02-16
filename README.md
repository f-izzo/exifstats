# EXIF stats

The data is extracted by using [exif2pandas](https://github.com/Visgean/exif2pandas)
The pip package is currently outdated (1.3 vs latest 1.4)
* Install exif2pandas from source
```
git clone --depth=1 https://github.com/Visgean/exif2pandas.git
cd exif2pandas
python setup.py install --user
pip install pyarrow
```
* Add `/home/fede/.local/bin/` to `$PATH` if not yet done
* Run exif2pandas
```
cd ../exif_stats
time exif2pandas -f home_pictures.feather -p 4 ~/Pictures/
time exif2pandas -f nastor_pictures.feather -p 4 /srv/disk/Photos/
```
