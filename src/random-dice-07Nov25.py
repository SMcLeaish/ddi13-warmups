import numpy as np
import polars as pl
import altair as alt

rand = np.random.randint(1, 7, size=1000)
df = pl.DataFrame({"rolls": rand})
alt.theme.enable("dark")
alt.renderers.enable("browser")

chart = (
    alt.Chart(df)
    .mark_bar(color="purple")
    .encode(
        alt.X("rolls:O", bin=True),
        y="count()",
    )
    .properties(height=400, width=400)
)
# chart.show()
# Real world: 60 out of 100 people said "yes"
real_yes = 60

# Null idea: people are 50/50 on "yes" vs "no"
simulated_yes = np.random.binomial(n=100, p=0.5, size=10000)

# How often did chance alone give us 60 or more "yes" votes?
p_value = np.mean(simulated_yes >= real_yes)
# print("P-value:", p_value)

np.random.binomial(n=10, p=0.5)
import finnhub
import time
import sys

finnhub_client = finnhub.Client(api_key="d4744cpr01qh8nnb1ragd4744cpr01qh8nnb1rb0")
# print(finnhub_client.quote("AAPL"))
news = pl.DataFrame(finnhub_client.general_news("general", min_id=0))
news.head()

for row in news.iter_rows(named=True):
    print(
        f"""{row["source"]} -

    {row["headline"]}

    {row["summary"]}\n"""
    )
    time.sleep(5)


import pandas as pd
import yfinance as yf

df = yf.download("NVDA", period="3mo", interval="1d", group_by="ticker")

df.columns = [
    "_".join(col).strip() if isinstance(col, tuple) else col
    for col in df.columns.values
]

df = df.reset_index()

df = df.rename(
    columns={
        "Date": "Date",
        "NVDA_Close": "Close",
        "NVDA_High": "High",
        "NVDA_Low": "Low",
        "NVDA_Open": "Open",
        "NVDA_Volume": "Volume",
    }
)

print(df.columns)
import altair as alt

alt.theme.enable("dark")
alt.renderers.enable("browser")
chart = (
    alt.Chart(df)
    .mark_rule()
    .encode(
        x="Date:T",
        y="Low:Q",
        y2="High:Q",
        color=alt.condition(
            "datum.Open < datum.Close", alt.value("green"), alt.value("red")
        ),
    )
    + alt.Chart(df)
    .mark_bar()
    .encode(
        x="Date:T",
        y="Open:Q",
        y2="Close:Q",
        color=alt.condition(
            "datum.Open < datum.Close", alt.value("green"), alt.value("red")
        ),
    )
).properties(width=700, height=400, title="NVIDIA Daily Candlestick (3mo)")
ymin = df["Low"].min()
ymax = df["High"].max()

buffer = (ymax - ymin) * 0.02
chart = chart.encode(
    y=alt.Y("Low:Q", scale=alt.Scale(domain=[ymin - buffer, ymax + buffer]))
)


chart.show()
