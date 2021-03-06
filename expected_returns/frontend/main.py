import altair as alt
import pandas as pd
import requests
import streamlit as st

sidebar = st.sidebar.selectbox(
    label="Navigation", options=("Home", "Update Database", "World", "By Country")
)

if sidebar == "Home":
    st.title("Expected Returns Front End")
    st.markdown("---")


elif sidebar == "Update Database":
    st.title("Update Database")
    st.markdown("---")

    scope = st.selectbox(label="scope", options=("World", "Country"))
    if st.button("Update Database"):
        try:
            res = requests.post(url=f"http://backend:8000/update/{scope}")
        except Exception as e:
            res = requests.post(url=f"http://127.0.0.1:8000/update/{scope}")
        st.success(res.json()["Message"])

elif sidebar == "World":
    st.title("World Expected Returns")
    st.markdown("---")
    if st.button("Request World Expected Returns"):

        try:
            res = requests.post(url="http://backend:8000/expected-returns/World")
        except Exception as e:
            res = requests.post(url="http://127.0.0.1:8000/expected-returns/World")

        res_df = pd.read_json(res.text)

        c = (
            alt.Chart(res_df)
            .mark_area(
                line={"color": "#74c476"},
                color=alt.Gradient(
                    gradient="linear",
                    stops=[
                        alt.GradientStop(color="white", offset=0),
                        alt.GradientStop(color="#c7e9c0", offset=1),
                    ],
                    x1=1,
                    x2=1,
                    y1=1,
                    y2=0,
                ),
            )
            .encode(x="date", y="cape")
        )

        st.altair_chart(c, use_container_width=True)

        with st.expander("See Response DataFrame"):
            st.dataframe(res_df)

        with st.expander("See JSON response"):
            st.json(res.json())


elif sidebar == "By Country":
    st.title("Expected Returns By Country")
    st.markdown("---")
    if st.button("Request Expected Returns By Country"):

        try:
            res = requests.post(url="http://backend:8000/expected-returns/Country")
        except Exception as e:
            res = res = requests.post(
                url="http://127.0.0.1:8000/expected-returns/Country"
            )

        res_df = pd.read_json(res.text)

        highlight = alt.selection(
            type="single", on="mouseover", fields=["country"], nearest=True
        )

        base = alt.Chart(res_df).encode(x="date:T", y="cape:Q", color="country:N")

        points = (
            base.mark_circle()
            .encode(opacity=alt.value(0))
            .add_selection(highlight)
            .properties(width=600)
        )

        lines = base.mark_line().encode(
            size=alt.condition(~highlight, alt.value(1), alt.value(3))
        )

        st.altair_chart(points + lines, use_container_width=True)

        with st.expander("See Response DataFrame"):
            st.dataframe(res_df)

        with st.expander("See JSON response"):
            st.json(res.json())
