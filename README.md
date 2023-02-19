# EXIF stats

Federico Amedeo Izzo - 2023

## Usage
The EXIF metadata is gathered using [exif2pandas](https://github.com/Visgean/exif2pandas)
* Install exif2pandas and Apache Arrow dependency
```
pip install exif2pandas pyarrow
```
* Run exif2pandas to collect metadata information
```
time exif2pandas -f pictures.feather ~/Pictures/
```
* Change the following line in the code to match your feather file name
```
exif_data_file = "./pictures.feather"
```
* Run exif_stats
```
pip install streamlit polars plotly
streamlit run exif_stats pictures.feather
```
* Point a web browser to http://localhost:8501

federico@izzo.pro
