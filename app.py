import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Top U.S. Government Web Pages"
mytitle = "People on a single, specific page"
x_values = ['Now', '7 Days Ago', '30 Days Ago']
y1_values = [13202, 14102, 10984]
y2_values = [10831, 22891, 9892]
y3_values = [5731, 6511, 8810]
y4_values = [5275, 8314, 4328]
y5_values = [2281, 9214, 5328]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
color4 = '#32a852'
color5 = '#d13b24'
name1 = 'USPS.com® - USPS Tracking® Results'
name2 = 'National Hurricane Center'
name3 = 'NLM - PubMed Search Results'
name4 = 'USAJOBS - Search'
name5 = 'Atlantic 2-Day Graphical Tropical Weather Outlook'
tabtitle = 'U.S. Website Visits'
sourceurl = 'https://analytics.usa.gov/'
githublink = 'https://github.com/regina-avila/dash-linechart-example/'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)
trace3 = go.Scatter(
    x = x_values,
    y = y4_values,
    mode = 'lines',
    marker = {'color': color4},
    name = name4
)
trace4 = go.Scatter(
    x = x_values,
    y = y5_values,
    mode = 'lines',
    marker = {'color': color5},
    name = name5
)

# assign traces to data
data = [trace0, trace1, trace2, trace3, trace4]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
