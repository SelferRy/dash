# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/66037052/update-data-table-using-date-picker-range-on-dash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_table import DataTable

from dash.dependencies import Input, Output, State
from app import app

import pandas as pd
import numpy as np

from datetime import date, datetime, timedelta
import time


# ====================== data =====================
def get_date(day):
    return date(2021, 9, day)


n = 20
indices = [get_date(day) for day in range(10, 10 + n)]
rawDf = pd.DataFrame({"A": np.random.rand(n),
                      "B": np.random.randn(n),
                      "C": np.ones(n)}, index=indices)

df = rawDf.to_dict("rows")
# ==================================================

# app = dash.Dash()
# app.scripts.config.serve_locally = True

layout = html.Div(children=[
    html.Button(
        id='button-update',
        children=['Update']
    ),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(2021, 9, 10),
        max_date_allowed=date.today(),
        start_date=date.today() - timedelta(days=7),
        end_date=date.today(),
        display_format='D.M.Y'
    ),
    dcc.Loading(
        id="loading-1",
        children=[
            DataTable(
                id='datatable-weapons',
                columns=[{"name": i, "id": i, "type": "numeric", 'format': {'locale': {'group': '.', 'decimal': ','}}}
                         for i in rawDf.columns],
                data=[]
            )
        ]
    )])

# @app.callback(
#     [Output('my-date-picker-range', 'start_date'), Output('my-date-picker-range', 'end_date')],
#     [Input('button-update', 'n_clicks')])
# def update_output(n_clicks):
#     if n_clicks is not None and n_clicks > 0:
#         start_date = date(2021, 9, 10)
#         end_date = date.today()
#         return start_date, end_date
#
#     return date(2021, 9, 10), date(2021, 9, 17)

@app.callback(
    [Output('datatable-weapons', 'data')],
    [Input('my-date-picker-range', 'start_date'), Input('my-date-picker-range', 'end_date')])
def update_graph(begin_dt, end_dt):
    begin_date = datetime.strptime(begin_dt, '%Y-%m-%d')
    end_date = datetime.strptime(end_dt, '%Y-%m-%d')
    days = (end_date - begin_date).days

    rawDfSlice = rawDf[0:days]
    dfSlice = rawDfSlice.to_dict("rows")

    # time.sleep(5)

    return (dfSlice,) # This value needs to be wrapped to be accepted by Dash

# if __name__ == "__main__":
#     app.run_server(debug=True)