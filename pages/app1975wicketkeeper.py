import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_1975 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name = 'WICKET KEEPER RECORDS',order=5)

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
                    html.H3('WICKET KEEPER - 1975 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST DISMISSALS INVOLVING A WICKET KEEPER',
                                            'MOST DISMISSALS INVOLVING A WICKET KEEPER IN AN INNINGS'], id='request_wk')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_wk'),
                    html.Br(),
                    html.Div([], id='service_2_wk')
                ],xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
    ])

@dash.callback(

        [
            Output('service_1_wk', 'children'),
            Output('service_2_wk', 'children'),
        ],

        [
            # Input('teams', "value"),
            Input('inp-button', "n_clicks")
        ],

        [
            State("request_wk", 'value'),
            State('service_1_wk', 'children'),
            State('service_2_wk', 'children'),
        ],

        prevent_initial_call=True,

    )
def output(n_clicks, need, o1, o2):

    wk = pd.read_excel('assets/1975_World_Cup/most_dissmissals_by_wk_1975.xlsx')
    wk_innings = pd.read_excel('assets/1975_World_Cup/most_dissmissals_in_an_innings_by_wk_1975.xlsx')

    if need == 'MOST DISMISSALS INVOLVING A WICKET KEEPER':
        wk = wk.sort_values(by=['Dismissals'],ascending=False)
        wk = wk[['Player','Match','Catch','Stump','Dismissals']]
        wk = wk.head(6)
        df1_fig = dbc.Table.from_dataframe(wk, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(wk, x='Player', y='Dismissals',
                     hover_data=['Player','Match','Catch','Stump','Dismissals'], color='Dismissals',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST DISMISSALS INVOLVING A WICKET KEEPER IN AN INNINGS':
        wk_innings = wk_innings.sort_values(by=['Dismissals'],ascending=False)
        wk_innings = wk_innings[['Player','Catches','Stumps','Dismissals','Match','Ground']]
        wk_innings_10 = wk_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(wk_innings, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(wk_innings_10, x='Player', y='Dismissals',
                     hover_data=['Catches','Stumps','Match','Ground'], color='Dismissals',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]