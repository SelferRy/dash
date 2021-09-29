import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from collections import OrderedDict

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(data)

layout = html.Div(children=[
    html.H1(children='Table demonstration page'),
    html.Center(html.H3("This table has negative value in column temperature.")),
    html.H5("We can fill it to some colors.", style={'text-align': 'right'}),
    dcc.Link("Go to main-page", id="link", style={'color': 'green', 'text-align': 'center'}, href="/"),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_header={'border': '1px solid black'},
        style_cell={'border': '1px solid grey'},
        style_data_conditional=[
            {
                'if': {
                    'filter_query': '{Temperature} < 0',
                    'column_id': 'Temperature'
                },
                'backgroundColor': 'blue',
                'color': "white"
            }
        ]
    )
])