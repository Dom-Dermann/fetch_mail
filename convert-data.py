import graph_converter as gc

dataset = gc.data_model('/home/domdom/Desktop/downloads/airtravel.csv')
se = dataset.create_timeseries()
print(se)