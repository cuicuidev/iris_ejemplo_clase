import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from functools import reduce

PAGE_CONFIG = {"page_title"            : "Iris Dashboard",
               "layout"                : "wide"}

def main():
    st.set_page_config(**PAGE_CONFIG)
    df = sns.load_dataset("iris")

    # User input
    species = st.multiselect("Especie", options=list(df.species.unique()), default=list(df.species.unique()))

    max_sepal_length = st.slider("Max largo de sépalo", min_value=0.0, max_value=10.0, value=10.0, step=0.1)
    min_sepal_length = st.slider("Min largo de sépalo", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

    max_sepal_width= st.slider("Max ancho de sépalo", min_value=0.0, max_value=10.0, value=10.0, step=0.1)
    min_sepal_width = st.slider("Min ancho de sépalo", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

    max_petal_length = st.slider("Max largo de pétalo", min_value=0.0, max_value=10.0, value=10.0, step=0.1)
    min_petal_length = st.slider("Min largo de pétalo", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

    max_petal_width = st.slider("Max ancho de pétalo", min_value=0.0, max_value=10.0, value=10.0, step=0.1)
    min_petal_width = st.slider("Min ancho de pétalo", min_value=0.0, max_value=10.0, value=0.0, step=0.1)


    # Filtrado
    masks = [
        df["sepal_length"].between(min_sepal_length, max_sepal_length),
        df["sepal_width"].between(min_sepal_width, max_sepal_width),
        df["petal_length"].between(min_petal_length, max_petal_length),
        df["petal_width"].between(min_petal_width, max_petal_width),
        df["species"].isin(species)
    ]

    mask = reduce(lambda x, y: x & y, masks)

    df_filtrado = df[mask]

    # Dataframe
    with st.expander("Dataframe"):
        st.dataframe(df_filtrado)

    # Histogramas

    cols = st.columns(3)

    fig_1 = plt.figure()
    sns.histplot(df_filtrado["sepal_length"])
    fig_2 = plt.figure()
    sns.histplot(df_filtrado["sepal_width"])
    fig_3 = plt.figure()
    sns.histplot(df_filtrado["petal_length"])
    fig_4 = plt.figure()
    sns.histplot(df_filtrado["petal_width"])

    cols[0].pyplot(fig_1)
    cols[0].pyplot(fig_2)
    cols[1].pyplot(fig_3)
    cols[1].pyplot(fig_4)

    # Frecuencias
    fig_pie = plt.figure(figsize=(12,12))
    plt.pie(df_filtrado["species"].value_counts().values, labels=df_filtrado["species"].value_counts().index, autopct="%1.1f%%")

    cols[2].pyplot(fig_pie)




if __name__ == "__main__":
    main()
