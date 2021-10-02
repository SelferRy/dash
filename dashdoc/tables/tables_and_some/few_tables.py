import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os
from dash.dependencies import Input, Output
import numpy as np

names = ['Player','Pos','Games','Rush Mkt Shr','Yds/Rush','Rush TD Rate','Tgt Mkt Shr','Yds/Rec','Rec TD Rate','Catch Rate','Int Rate','QB Snaps']
team_entries = pd.DataFrame(np.zeros((11,len(names))),columns = names)
team_entries['Pos']=['QB','RB','RB','RB','WR','WR','WR','WR','TE','TE','TEAM']
team_entries['Games'] = 16
app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div(id='div1', children=[dash_table.DataTable(
        id='table-editing-simple',
        columns=([{'id': p, 'name': p} for p in team_entries.columns]),
        data=team_entries.to_dict('records'),
        editable=True
    )]),
    html.Div(id = 'div2', children=[dash_table.DataTable(id='table-editing-simple-output')])
])


@app.callback(
    Output('div2', 'children'),
    [Input('table-editing-simple', 'data'),
     Input('table-editing-simple', 'columns')])
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    df['Games'] = df['Games']*2
    return dash_table.DataTable(
        id='table-output',
        columns=columns,
        data=rows,
    )


if __name__ == '__main__':
    app.run_server(debug=True)