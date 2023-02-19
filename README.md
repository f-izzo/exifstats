# EXIF stats

Federico Amedeo Izzo - 2023

## Usage
The EXIF metadata is gathered using [exif2pandas](https://github.com/Visgean/exif2pandas)
* Install exif2pandas and other dependencies
```
pip install -r requirements
```
* Run exif2pandas to collect metadata information
```
time exif2pandas -f pictures.feather ~/Pictures/
```
* Change the following line in the code to match your feather file name
```
exif_data_file = "./pictures.feather"
```
* Run `exifstats.py` using streamlit
```
streamlit run exif_stats pictures.feather
```
* Point a web browser to http://localhost:8501

federico@izzo.pro
