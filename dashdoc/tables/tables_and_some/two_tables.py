# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/66037052/update-data-table-using-date-picker-range-on-dash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_table import DataTable

from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

from datetime import date, datetime, timedelta


# ====================== data =====================
n = 20
indices = [date(2021, 9, day) for day in range(10, 10 + n)]
df = pd.DataFrame({"A": np.random.rand(n),
                   "B": np.random.randn(n),
                   "C": np.ones(n)}, index=indices)
# ==================================================

app = dash.Dash()
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
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
            html.Div(
                DataTable(
                    id='datatable-weapons',
                    columns=[{"name": i, "id": i, "type": "numeric",
                              'format': {'locale':
                                         {'group': '.', 'decimal': ','}
                                         }
                              }
                             for i in df.columns]
                    )
            ),
            html.Div(
                DataTable(
                    id='datatable-weapons-2',
                    columns=[{"name": i, "id": i, "type": "numeric",
                              'format': {'locale':
                                         {'group': '.', 'decimal': ','}
                                         }
                              }
                             for i in df.columns]
                    )
            )
        ]
    )
])


@app.callback(
    Output('datatable-weapons', 'data'),
    Output('datatable-weapons-2', 'data'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_graph(begin_dt, end_dt):
    begin_date = datetime.strptime(begin_dt, '%Y-%m-%d')
    end_date = datetime.strptime(end_dt, '%Y-%m-%d')
    days = (end_date - begin_date).days

    df_slice = df[0:days]
    df_slice = df_slice.to_dict("rows")

    # time.sleep(5)

    return df_slice[:3], df_slice[3:]


if __name__ == "__main__":
    app.run_server(debug=True)
