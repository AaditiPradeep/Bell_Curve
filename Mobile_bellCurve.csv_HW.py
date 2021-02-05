import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("MobileBrands_bellCurve.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"] , show_hist = False)
fig.show()
