import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_5000 import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import lr_match_prediction
from plotly.subplots import make_subplots


dash.register_page(__name__,name = 'MATCH 1 ENG VS NZ')

teams_values = {'England' : 1,
                'New Zealand':2}

team1 = 'England'
team2 = 'New Zealand'

toss_won = 'Won'
toss_lost = 'Lost'

toss_action_set_target = 'Set Target'
toss_action_chase = 'Chase'

runs_scored = 270
wickets_taken = 10


team1_win_toss,team1_loss_toss = lr_match_prediction.match_prediction_after_toss(team1,toss_won)
team2_win_toss,team2_loss_toss = lr_match_prediction.match_prediction_after_toss(team2,toss_lost)

team1_action_win,team1_action_loss = lr_match_prediction.match_prediction_after_action(team1,toss_action_chase)
team2_action_win,team2_action_loss = lr_match_prediction.match_prediction_after_action(team2,toss_action_set_target)

first_innings_runs_win,first_innings_runs_loss = lr_match_prediction.match_prediction_after_first_batting(team2,runs_scored)
first_innings_wickets_win,first_innings_wickets_loss = lr_match_prediction.match_prediction_after_bowling_first(team1,wickets_taken)

data = {
    'TEAM':[team1,team2,team1,team2,team2,team1],
    'OPTION':[toss_won,toss_lost,toss_action_set_target,toss_action_chase,runs_scored,wickets_taken],
    'WIN PROBABILITY':[team1_win_toss,team2_win_toss,team1_action_win,team2_action_win,first_innings_runs_win,first_innings_runs_win],
    'LOSS PROBABILITY':[team1_loss_toss,team2_loss_toss,team1_action_loss,team2_action_loss,first_innings_runs_loss,first_innings_wickets_loss]
}

df = pd.DataFrame(data)

'''df1 = df['TEAM'] = team1
df2 = df['TEAM'] = team2

df1 = df1.replace({'TEAM': teams_values})
df2 = df2.replace({'TEAM': teams_values})

fig_1 = make_subplots(rows=1, cols=2,subplot_titles=('ENGLAND WIN PREDICTION',"NEW ZEALAND WIN PREDICTION",))#, shared_yaxes=True))

fig_1.add_trace(go.Bar(x=df1['TEAM'], y=df1['WIN PROBABILITY'],
                           text = df1['OPTION'],
                           hovertext=df1['TEAM']
                           ,name=""),#, coloraxis="coloraxis")),
                    1, 1)

fig_1.add_trace(go.Bar(x=df2['TEAM'], y=df2['WIN PROBABILITY'],
                           text=df2['OPTION'],
                           hovertext=df2['TEAM']
                           ,name=""),#, coloraxis="coloraxis")),
                    1, 2)
'''

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
                    html.H2('ENGLAND VS NEW ZEALAND', style={'textAlign':'center'}),
                    html.Br(),
                    html.Br(),
                    #dcc.Graph(figure=fig_1),
                    html.Br(),
                    html.H4('AFTER TOSS RESULT PREDICTIONS', style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of England winning the game after winning the toss : "+str((team1_win_toss))+" %", style={'textAlign':'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of New Zealand winning the game after winning the toss : " + str((team2_loss_toss)) + " %", style={'textAlign':'center'}),
                    html.Br(),
                    html.H3('AFTER CHOICE RESULTS PREDICTION', style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of England winning the game after Bowling First : " + str((team1_action_win)) + " %", style={'textAlign':'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of New Zealand winning the game after Batting First : " + str((team2_action_win)) + " %", style={'textAlign':'center'}),
                    html.Br(),
                    html.H3('AFTER FIRST INNINGS RESULTS PREDICTION', style={'textAlign': 'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of England winning the game after taking "+str((wickets_taken))+" wickets Bowling first: " + str((first_innings_wickets_win)) + " %", style={'textAlign':'center'}),
                    html.Br(),
                    html.H5("The Probability prediction of New Zealand winning the game after scoring "+str((runs_scored))+" Batting First : " + str((first_innings_runs_win)) + " %", style={'textAlign':'center'}),
                ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10
            ),

        ]
    )
    ])
