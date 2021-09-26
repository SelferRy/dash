import dash_html_components as html
import dash_core_components as dcc


def layout_main_page():
    layout = html.Div([
        html.Div([
            html.H1('Оперативный мониторинг моделей РКК'),
        ], className='banner_header'),
        html.Div([
            html.Div([
                dcc.Link(id='oper_monitoring_link', children='Ежедневные тесты качества моделей', href='\oper_monitoring',
                         className="basic_link")
            ], className='buttons_holder_custom')
        ],
            className='centering_menu'
        ),
        # а не сделать ли этот блок скрытым для некомпозитных моделей?
        # loading включить можно, но от этого почему-то меняются размеры dcc.Graph (надо разбираться)
        # и по-моему так субъективно больше ощущения "этот сайт тормозит"
        # dcc.Loading(id="loading", children=[html.Div(id='tabs-content')], fullscreen=False, type="circle"),
        html.Div([
            html.H1('Аналитический мониторинг бизнес моделей'),
        ], className='banner_header'),
        html.Div([
            html.Div([
                dcc.Link(id='app1', children='app1', href='/apps/app1',
                         className="app1"),
                html.Br(),
                dcc.Link(id='app2', children='app2', href='/apps/app2',
                         className="app2"),
                html.Br(),
                dcc.Link(id='boarder_table', children='table', href='/apps/table',
                         className="table"),
                # dcc.Link(id='oper_monitoring_link', children='Мониторинг PD моделей', href='\model_pd',
                #          className="basic_link"),
                # dcc.Link(id='dq-link_main', children='Мониторинг качества данных PD моделей', href='\dataquality',
                #          className="basic_link"),
                # dcc.Link(id='ext_services_link', children='Мониторинг внешних сервисов PD моделей', href='\external',
                #          className="basic_link"),
                # dcc.Link(id='income_link', children='Мониторинг модели дохода', href='\model_income',
                #          className="basic_link"),
                # dcc.Link(id='income_link_quality', children='Мониторинг качества данных модели дохода',
                #          href='/dataquality_income',
                #          className="basic_link")
            ], className='buttons_holder_custom')
        ],
            className='centering_menu',
        )
        # а не сделать ли этот блок скрытым для некомпозитных моделей?
        # loading включить можно, но от этого почему-то меняются размеры dcc.Graph (надо разбираться)
        # и по-моему так субъективно больше ощущения "этот сайт тормозит"
        # dcc.Loading(id="loading", children=[html.Div(id='tabs-content')], fullscreen=False, type="circle"),

    ]
    )
    return layout
