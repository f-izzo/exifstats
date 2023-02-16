import streamlit as st
import polars as pl
import plotly.express as px

exif_data_file = "./home_pictures.feather"

def chart_make_model(df):
    st.subheader("Camera Makes and Models")
    df_make_count = df.groupby("image-make").count()
    df_model_count = df.groupby("image-model").count()
    c1,c2 = st.columns(2)
    make_pie = px.pie(df_make_count.to_pandas(), 
                      values="count", 
                      names="image-make", 
                      title='Camera Makes', 
                      color_discrete_sequence=px.colors.qualitative.Pastel)
    model_pie = px.pie(df_model_count.to_pandas(), 
                       values="count", 
                       names="image-model", 
                       title='Camera Models', 
                       color_discrete_sequence=px.colors.qualitative.Pastel)
    make_pie.update_traces(textposition='inside', textinfo='percent+label')
    model_pie.update_traces(textposition='inside', textinfo='percent+label')
    with c1:
        st.plotly_chart(make_pie, use_container_width=True)
    with c2:
        st.plotly_chart(model_pie, use_container_width=True)

st.set_page_config(
    page_title="EXIF Statistics",
    layout="wide")
st.header("EXIF Statistics")
st.write("2023 - Federico Amedeo Izzo federico@izzo.pro")
df = pl.read_ipc(exif_data_file)
with st.expander("Full data"):
    st.write(df.to_pandas())
chart_make_model(df)
