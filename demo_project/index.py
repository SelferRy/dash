import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import page_dropdown, page_submit_button, page_main, boarder_table, table_plot


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    # print(pathname)
    if pathname == '/apps/dropdown':
        return page_dropdown.layout
    elif pathname == '/apps/submit_button':
        return page_submit_button.layout
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