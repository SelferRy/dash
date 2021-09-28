import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Dropdown page'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='dropdown-display-value'),
    dcc.Link('Go to main page', href='/'),
    dcc.Link('Go to \"Submit button page\"', href='/apps/submit_button')
])


@app.callback(
    Output('dropdown-display-value', 'children'),
    Input('dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)