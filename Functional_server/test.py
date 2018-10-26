import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='test', api_key='test')
labels = ['Tests OK','Tests NOK']
values = [200,10]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart')