import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_5000 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name = 'MATCH 2 PAK VS NETH')

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('PAKISTAN VS NETHERLANDS', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST DISMISSALS INVOLVING A WICKET KEEPER','MOST STUMPS BY A WICKET KEEPER',
                                            'MOST CATCHES BY A WICKET KEEPER',
                                            'MOST DISMISSALS INVOLVING A WICKET KEEPER IN AN INNINGS','MOST STUMPS BY A WICKET KEEPER IN AN INNINGS',
                                            'MOST CATCHES BY A WICKET KEEPER IN AN INNINGS'], id='request_wk_all')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_wk_all'),
                    html.Br(),
                    html.Div([], id='service_2_wk_all')
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
    ])
