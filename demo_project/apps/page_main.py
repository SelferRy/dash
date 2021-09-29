import dash_html_components as html
import dash_core_components as dcc
# from ..app import app


def layout_main_page():
    layout = html.Div([
        # ================================================
        # html.Div([
        #     html.H1('Оперативный мониторинг моделей РКК'),
        # ], className='banner_header'),
        # ================================================
        # html.Div([
        #     html.Div([
        #         dcc.Link(id='oper_monitoring_link', children='Ежедневные тесты качества моделей', href='\oper_monitoring',
        #                  className="basic_link")
        #     ], className='buttons_holder_custom')
        # ],
        #     className='centering_menu'
        # ),
        # ================================================
        html.Div([
            html.H1('Analytical monitoring of business models'),
            # html.H1('Аналитический мониторинг бизнес моделей'),
        ], className='banner_header'),
        # ================================================
        html.Div([
            html.Div([
                dcc.Link(id='dropdown', children='Dropdown page', href='/apps/dropdown',
                         className="dropdown"),
                html.Br(),
                dcc.Link(id='submit_button', children='Submit_button page', href='/apps/submit_button',
                         className="submit_button"),
                html.Br(),
                dcc.Link(id='boarder_table', children='Table', href='/apps/table',
                         className="table"),
                html.Br(),
                dcc.Link(id='data_table', children='Data from oracle', href='/apps/data_oracle'),
                html.Br(),
                html.Img(src="../assets/csm_data-science-ansatz_4b4a12f844.jpg")
            ], className='buttons_holder_custom')
        ],
            className='centering_menu',
        )
        # ================================================
    ]
    )
    return layout
