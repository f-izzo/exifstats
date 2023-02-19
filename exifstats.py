import streamlit as st
import polars as pl
import plotly.express as px

exif_data_file = "./pictures.feather"

def piechart(pie_df, column, title, categorical=True):
    if categorical:
        colors = px.colors.qualitative.Pastel
    else:
        colors = px.colors.sequential.Turbo
    pie_chart = px.pie(pie_df.to_pandas(),
                      values="count",
                      names=column,
                      title=title,
                      color_discrete_sequence=colors)
    pie_chart.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(pie_chart, use_container_width=True)

def chart_make_model(df):
    st.subheader("Camera Makes and Models")
    df_make_count = df.groupby("image-make").count().drop_nulls()
    df_model_count = df.groupby("image-model").count().drop_nulls()
    c1,c2 = st.columns(2)
    with c1:
        piechart(df_make_count, "image-make", "Camera Makes")
    with c2:
        piechart(df_model_count, "image-model", "Camera Models")

def chart_iso(df):
    st.subheader("Shoot ISO")
    df_iso_count = df.groupby("exif-isospeedratings"
        ).count(
        ).drop_nulls(
        ).sort("exif-isospeedratings")   
    st.write(df_iso_count.to_pandas())
    piechart(df_iso_count, "exif-isospeedratings", "Shoot ISO", categorical=False)

st.set_page_config(
    page_title="EXIF Statistics",
    layout="wide")
st.header("EXIF Statistics")
st.write("2023 - Federico Amedeo Izzo federico@izzo.pro")
df = pl.read_ipc(exif_data_file)
with st.expander("Full data"):
    st.write(df.to_pandas())
chart_make_model(df)
chart_iso(df)
