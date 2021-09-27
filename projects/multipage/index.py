import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2, page_main, boarder_table, table_plot


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    # print(pathname)
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/table':
        return boarder_table.layout
    elif pathname == '/apps/plot':
        return table_plot.layout
    elif pathname == '/':
        return page_main.layout_main_page()
    else:
        print(pathname)
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)