import csv
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('height vs weight.csv')

fig  = ff.create_distplot([df['Weight(Pounds)'].tolist()],['Result'],show_hist= False)

fig.show()