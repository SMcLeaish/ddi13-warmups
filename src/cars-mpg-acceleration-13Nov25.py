import altair as alt
import polars as pl
from scipy import stats

df = pl.read_csv('data/cars.csv', ignore_errors=True)


def get_avg(df: pl.DataFrame, col: str):
    return df.select(pl.col(col).mean()).item(0, 0)


mpgs = []
accels = []
origins = [
    df.filter(pl.col('origin') == 1),
    df.filter(pl.col('origin') == 2),
    df.filter(pl.col('origin') == 3),
]
for origin in origins:
    mpgs.append(get_avg(origin, 'mpg'))
for origin in origins:
    accels.append(get_avg(origin, 'acceleration'))
avg_mpg_1, avg_mpg_2, avg_mpg_3 = mpgs
avg_accel_1, avg_accel_2, avg_accel_3 = accels
for mpg in mpgs:
    print(mpg)
for accel in accels:
    print(accel)
