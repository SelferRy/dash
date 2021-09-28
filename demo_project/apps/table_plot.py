import dash
import dash_core_components as dcc
import dash_html_components as html
# from boarder_table import df
# import pandas as pd
# from collections import OrderedDict
#
# data = OrderedDict(
#     [
#         ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
#         ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
#         ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
#         ("Humidity", [10, 20, 30, 40, 50, 60]),
#         ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
#     ]
# )
#
# df = pd.DataFrame(data)


external_stylesheets = ['./z_external_stylesheets.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [ # df
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

# if __name__ == '__main__':
#     app.layout = layout
#     app.run_server(debug=True)
