import plotly
import plotly.plotly as py
import plotly.graph_objs as go

try:
    plotly.tools.set_credentials_file(username='cardosoluke', api_key='LvwswFk0puyRUEPt3mvK')
    labels = ['Tests OK','Tests NOK']
    values = [200,10]

    trace = go.Pie(labels=labels, values=values)

    py.iplot([trace], filename='Tests_OK')

except:
    print('end 0')
try:
    labels = ['login','cpf','voucher', 'password','wpa2','wpa','without password']
    values = ['ok','nok','nok','ok','ok','ok','nok']

    trace = go.Pie(labels=labels, values=values)

    py.iplot([trace], filename='Tests_Cases')
except:
    print ('end 1')