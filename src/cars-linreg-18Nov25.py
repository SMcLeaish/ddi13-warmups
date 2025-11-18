import altair as alt
import polars as pl
from sklearn.linear_model import LinearRegression

df = pl.read_csv('data/cars.csv', ignore_errors=True)
ldf = pl.scan_csv('data/cars.csv', infer_schema_length=200)
ldf = ldf.with_columns(pl.col('horsepower').cast(pl.Float64, strict=False))
ldf = ldf.with_columns(pl.col('horsepower').fill_null(strategy='mean'))
df = ldf.collect()

def lin_reg(df:pl.DataFrame) -> pl.DataFrame:
    X = df[["horsepower"]]
    y = df['mpg']

    lin_model = LinearRegression()

    lin_model.fit(X, y)

    y_predictions = lin_model.predict(X)

    return df.with_columns(
        pl.Series("y_pred", y_predictions)
    )

def plots(df: pl.DataFrame) -> None:
    alt.renderers.enable('browser')
    bar = df.plot.bar(x=alt.X('horsepower:Q', bin=True), y='count()')
    lin_df = lin_reg(df)
    scatter = lin_df.plot.point(x='horsepower', y='mpg')
    line = lin_df.plot.line(
        x="horsepower",
        y="y_pred",
    )

    (scatter + line | bar).configure_line(color='red').show()

plots(df)