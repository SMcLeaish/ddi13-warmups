import polars as pl


def clean_mpg(csv: str):
    ldf = pl.scan_csv(csv, infer_schema_length=200)
    ldf = ldf.with_columns(pl.col('horsepower').cast(pl.Float64, strict=False))
    df = ldf.collect()
    df = df.with_columns(pl.col('horsepower').fill_null(pl.col('horsepower').median()))
    return df['mpg'].mean(), df['horsepower'].max()


print(clean_mpg('data/cars.csv'))
