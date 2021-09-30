# import dash
# from dash import dash_table
# from dash import html
# from dash import dcc
# import pandas as pd
# from collections import OrderedDict
# import datetime
# import numpy as np
# from dash.dependencies import Input, Output
#
#
# # data = OrderedDict(
# #     [
# #         ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
# #         ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
# #         ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
# #         ("Humidity", [10, 20, 30, 40, 50, 60]),
# #         ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
# #     ]
# # )
#
# # df = pd.DataFrame(data)
#
# def get_date(day):
#     return datetime.date(2021, 9, day)
#
#
# n = 20
# indices = [get_date(day) for day in range(10, 10 + n)]
# df = pd.DataFrame({"A": np.random.rand(n),
#                    "B": np.random.randn(n),
#                    "C": np.ones(n)}, index=indices)
# ind = df.index
#
# app = dash.Dash(__name__)
#
# app.layout = html.Div(children=[
#     html.H1(children='My own page with Dash'),
#     html.Center(html.H3("This is H3")),
#     html.H5("this H5", style={'text-align': 'right'}),
#     dcc.Link("The link", id="link", style={'color': 'green', 'text-align': 'center'}, href="https://google.com"),
#
#     html.Div([
#         dcc.Dropdown(
#             id='select-df',
#             options=[{'label': i, 'value': i} for i in ind],
#             value=
#         )
#     ]),
#
#     dash_table.DataTable(
#         id='df-data',
#         date_start=10,
#         date_stop=20,
#         data=df.to_dict('records'),  # loc[get_date(date_start): get_date(date_stop), :]
#         columns=[{'id': c, 'name': c} for c in df.columns],
#         style_header={'border': '1px solid black'},
#         style_cell={'border': '1px solid grey'},
#         # style_data_conditional=[
#         #     {
#         #         'if': {
#         #             'filter_query': '{Temperature} < 0',
#         #             'column_id': 'Temperature'
#         #         },
#         #         'backgroundColor': 'blue',
#         #         'color': "white"
#         #     }
#         # ]
#     )
# ])
#
#
# @app.callback(
#     Output('df-data', 'data'),
#     Input('select-df', 'date_start'),
#     Input('select', 'date_stop'))
# def select_df(date_start_day, date_stop_day):
#     date_start = datetime.date(2021, 9, date_start_day)
#     date_stop = datetime.date(2021, 9, date_stop_day)
#     dff = df.loc[date_start: date_stop, :]
#     return dff
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
