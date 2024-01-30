import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_1999 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name = 'LARGEST VICTORIES',order=8)

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
                    html.H3('LARGEST VICTORIES - 1999 WORLD CUP', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['LARGEST VICTORY BY RUNS', 'LARGEST VICTORY BY WICKETS'], id='request_victory_1999')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_victory_1999'),
                    html.Br(),
                    html.Div([], id='service_2_victory_1999')
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_1_victory_1999','children'),
        Output('service_2_victory_1999','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_victory_1999", 'value'),
        State('service_1_victory_1999','children'),
        State('service_2_victory_1999','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    victory_by_wickets = pd.read_excel('assets/1999_World_Cup/largest_victories_by_wickets_1999.xlsx')
    victory_by_runs = pd.read_excel('assets/1999_World_Cup/largest_victories_by_runs_1999.xlsx')

    if need == 'LARGEST VICTORY BY RUNS':

        victory_by_runs = victory_by_runs[['Winner','Target','Margin','Match','Ground']]
        df1_fig = dbc.Table.from_dataframe(victory_by_runs, striped=True, bordered=True, hover=True)

        victory_by_runs = victory_by_runs.iloc[::-1]
        #victory_by_runs = victory_by_runs

        fig_1 = px.scatter(victory_by_runs, x='Match', y='Margin',
                     hover_data=['Winner','Target','Margin','Match','Ground'], color='Match',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_traces(marker=dict(size=50))
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    if need == 'LARGEST VICTORY BY WICKETS':

        victory_by_wickets = victory_by_wickets[['Winner','Balls Rem','Margin','Target','Match','Ground']]
        df1_fig = dbc.Table.from_dataframe(victory_by_wickets, striped=True, bordered=True, hover=True)

        victory_by_wickets = victory_by_wickets.iloc[::-1]
        #victory_by_runs = victory_by_runs

        fig_1 = px.scatter(victory_by_wickets, x='Match', y='Margin',
                     hover_data=['Winner','Balls Rem','Margin','Target','Match','Ground'], color='Match',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_traces(marker=dict(size=50))
        fig_1.update_layout(width=1200, height=500)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]