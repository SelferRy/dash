import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from proj.app import app

layout = html.Div([
    html.H3('App 2'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Br(),
    dcc.Link('Main page', href='/'),
    html.Br(),
    dcc.Link('App 1', href='/apps/app1'),
    # dcc.Dropdown(
    #     id='app-2-dropdown',
    #     options=[
    #         {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
    #             'NYC', 'MTL', 'LA'
    #         ]
    #     ]
    # ),
    # html.Div(id='app-2-display-value'),
    # dcc.Link('Go to App 1', href='/apps/app1')
])


@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)