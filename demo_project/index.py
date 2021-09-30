import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import page_dropdown, page_submit_button, page_main, boarder_table, table_plot, page_data,\
    page_mult_inputs  # page_data_oracle, page_slider


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
    elif pathname == '/apps/page_data':
        return page_data.layout
    elif pathname == '/apps/page_multi_inputs':
        print("Here")
        return page_mult_inputs.layout
    # elif pathname == '/apps/data_oracle':
    #     return page_data_oracle
    # elif pathname == '/apps/slider':
    #     return page_slider.layout
    elif pathname == '/':
        return page_main.layout_main_page()
    else:
        print(pathname)
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)