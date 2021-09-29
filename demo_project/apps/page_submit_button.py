import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Submit button'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Br(),
    dcc.Link('Main page', href='/'),
    html.Br(),
    dcc.Link('Dropdown', href='/apps/dropdown'),
])


@app.callback(
    Output('app-2-display-value', 'children'),
    Input('page_dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)