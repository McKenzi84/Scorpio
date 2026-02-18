import dash 
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input, State
import os
import numpy as np
# import plotly.graph_objects as go
# import pandas as pd
import math
from dash.exceptions import PreventUpdate

dash.register_page(__name__,name='1. Parametry ', order=1)

border = {  'border': '1px outset black',  'border-radius': '5px'}

layout = html.Div([
    html.H5("Parametry szlifowania"), 
    dbc.Row([
    dbc.Col([
                html.H5('Ściernica'),
                dbc.InputGroup([dbc.InputGroupText("Średnica ściernicy [mm]"), dbc.Input(id='wheel_d',type='number', value=350)],size='sm'),
                dbc.InputGroup([dbc.InputGroupText("Szerkość ściernicy [mm]"), dbc.Input(id='wheel_width',type='number', value=5)],size='sm'),
                dbc.InputGroup([dbc.InputGroupText("Obroty: R.P.M"), dbc.Input(id='wheel_rpm',type='number', value=5200)],size='sm'),
                dbc.InputGroup([dbc.InputGroupText("Prędkość: Vc [ m/s] "), dbc.Input(id='wheel_speed',type='number', value=95.3)],size='sm'),
                dcc.Dropdown(id='wheel_dir',
                             options=[{'label': f'  Kierunek rotacji: {x}', 'value': (x)} for x in ['LEWY', 'PRAWY']],
                             style={'color':'black', 'width': '100%'},placeholder="Kierunek obrotu", value='LEWY'),
                html.Br(),
                html.H5('Materiał'),
                dbc.InputGroup([dbc.InputGroupText("Średnica materiału [mm]"), dbc.Input(id='material_d',type='number', value=10)],size='sm'),
                dbc.InputGroup([dbc.InputGroupText("Obroty: R.P.M"), dbc.Input(id='material_rpm',type='number', value=823, style={"font-weight": "bold", "color": "blue"})],size='sm',),
                dbc.InputGroup([dbc.InputGroupText("Prędkość: Vw [ m/s] "), dbc.Input(id='material_speed',type='number', value=0.43)],size='sm'),
                dcc.Dropdown(id='material_dir',
                             options=[{'label': f'  Kierunek rotacji: {x}', 'value': (x)} for x in ['LEWY', 'PRAWY']],
                             style={'color':'black', 'width': '100%'},placeholder="Kierunek obrotu", value='PRAWY'),
                html.Br(),
                dbc.InputGroup([dbc.InputGroupText("Posuw [mm/min]"), dbc.Input(id='traverse_feed',type='number', value=50)],size='sm'),
                html.Br(),
                html.Div(id = 'grinding_type'),
                html.Div(id = 'direction_preview'),
                # dbc.InputGroup([dbc.InputGroupText("Feedrate [mm/min]"), dbc.Input(id='traverse_feed',type='number', value=762)]),
                # dbc.InputGroup([dbc.InputGroupText("ae [mm]"), dbc.Input(id='ae',type='number', value=0.038)]),
                html.Br(),
                # dbc.InputGroup([dbc.InputGroupText("Speed ratio / Współczynnik prędkośći [qs]"), dbc.InputGroupText(id='speed_ratio'),]),
                # dbc.InputGroup([dbc.InputGroupText("RPM ratio / Współczynnik obrotów [revs/rev]"), dbc.InputGroupText(id='rpm_ratio'),]),
                #dbc.InputGroup([dbc.InputGroupText("Overlap / Ud "), dbc.InputGroupText(id='ud_factor'),]),

                # dbc.InputGroup([dbc.InputGroupText("Specific MRR , Q-Prime"), dbc.InputGroupText(id='q_prime'),]),
                # dbc.InputGroup([dbc.InputGroupText("Aggressiveness number"), dbc.InputGroupText(id='aggresivness'),]),


                ]
                ,className="mb-3", width=3, 
                #style=border) ##757896
                style={'border': '1px outset black',  'border-radius': '5px','background-color': '#757896'}
                ),
    dbc.Col([   
                html.Br(),
                dbc.InputGroup([dbc.InputGroupText("Speed ratio / Współczynnik prędkości [qs]"), dbc.InputGroupText(id='speed_ratio',style={"font-weight": "bold",})],size='sm'),
                html.H6('* utrzymywać w zakresie: 200~280', style={"font-weight": "bold", "color": "green"}),
                html.Div(html.Img(src=f'assets/ulmer/calculations/speed_ratio.png', style={'width':'100%'})),
                html.Br(),
                dbc.InputGroup([dbc.InputGroupText("RPM ratio / Współczynnik obrotów [revs/rev]"), dbc.InputGroupText(id='rpm_ratio', style={"font-weight": "bold"}),],size='sm'),
                html.Div(html.Img(src=f'assets/ulmer/calculations/rpm_ratio1.png', style={'width':'100%'})),
    
                ],className="mb-3", width=4, 

                style={'border': '1px outset black',  'border-radius': '5px','background-color': '#97a8ad'}),
    dbc.Col([
                html.Br(),
                dbc.InputGroup([dbc.InputGroupText("Overlap / Nakładanie [Ud] "), dbc.InputGroupText(id='ud_factor', style={"font-weight": "bold"})], size='sm'),
                html.H6('* utrzymywać w zakresie: 70~130', style={"font-weight": "bold", "color": "green"}),
                html.Div(html.Img(src=f'assets/ulmer/calculations/ud_factor.png', style={'width':'100%'})),    
    
    ],className="mb-3", width=4, 
    # style=border, 
    style={'border': '1px outset black',  'border-radius': '5px','background-color': '#7aa191'}
    ),# End of column



    ]) # End of row 
])


# Wheel speed / RPM  calculation
@callback(
    Output("wheel_speed", "value"),
    Output("wheel_rpm", "value"),
    Input("wheel_rpm", "value"),
    Input("wheel_speed", "value"),
    Input("wheel_d", "value"),
    prevent_initial_call=True
)
def wheel_sync_input(wheel_rpm, wheel_speed, wheel_d):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "wheel_rpm":
        wheel_speed = round((wheel_d * np.pi  * wheel_rpm) / (60 * 1000),1)
        # wheel_speed = np.pi*wheel_d / np.tan(np.radians(wheel_rpm)) # obliczenie skoku helisy
    elif input_id == 'wheel_d':
        wheel_speed = round((wheel_d * np.pi  * wheel_rpm) / (60 * 1000),1)
    elif input_id == 'wheel_speed':
        wheel_rpm = round((wheel_speed * 60 * 1000) / ( wheel_d * np.pi),0)
        #wheel_rpm = np.atan((np.pi * wheel_d) / wheel_speed)
    return wheel_speed, wheel_rpm


# Material speed / RPM  calculation
@callback(
    Output("material_speed", "value"),
    Output("material_rpm", "value"),
    Input("material_rpm", "value"),
    Input("material_speed", "value"),
    Input("material_d", "value"),
    prevent_initial_call=True
)

def wheel_sync_input(material_rpm, material_speed, material_d):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "material_rpm":
        material_speed = round((material_d * np.pi  * material_rpm) / (60 * 1000),2)
        # wheel_speed = np.pi*wheel_d / np.tan(np.radians(wheel_rpm)) # obliczenie skoku helisy 
    elif input_id == 'material_d':
        material_speed = round((material_d * np.pi  * material_rpm) / (60 * 1000),2)
    
    elif input_id == 'material_speed':
        material_rpm = round((material_speed * 60 * 1000) / ( material_d * np.pi),0)
        #wheel_rpm = np.atan((np.pi * wheel_d) / wheel_speed)
    return material_speed, material_rpm

@callback(
    Output("speed_ratio", "children"),
    Input("wheel_speed", "value"),
    Input("material_speed", "value"),
    #prevent_initial_call=True
)
def wheel_sync_input(wheel_speed, material_speed):
    return round((wheel_speed / material_speed),2)

@callback(
    Output('rpm_ratio', 'children'),
    Input('wheel_rpm', 'value'),
    Input('material_rpm', 'value')
)
def check_rpm_ratio(wheel_rpm, material_rpm):

    return wheel_rpm/material_rpm

@callback(
    Output('direction_preview', 'children'),
    Output('grinding_type', 'children'),
    Input('wheel_dir', 'value'),
    Input('material_dir', 'value')
)
def direction_preview(wheel_dir, material_dir):
    if wheel_dir == 'LEWY' and material_dir == 'LEWY': 
        picture = 'LL.png'
        grinding_type = 'Szlifowanie współbieżne'
    elif wheel_dir == 'LEWY' and material_dir == 'PRAWY': 
        picture = 'LP.png' 
        grinding_type = 'Szlifowanie przeciwbieżne'
    elif wheel_dir == 'PRAWY' and material_dir == 'LEWY': 
        picture = 'PL.png' 
        grinding_type = 'Szlifowanie przeciwbieżne'
    elif wheel_dir == 'PRAWY' and material_dir == 'PRAWY': 
        picture = 'PP.png' 
        grinding_type = 'Szlifowanie współbieżne'
    return html.Img(src=f'assets/ulmer/calculations/{picture}', style={'width':'100%'}), html.H5(grinding_type)


# Check whether material RPM is prime number. 

@callback(
    Output('material_rpm', 'style'),   
    Input('material_rpm', 'value'),
)

def isprime(num):
        for n in range(2,int(num**0.5)+1):
            if num%n==0:
                return {"font-weight": "bold", "color": "black"}
        return {"font-weight": "bold", "color": "green"}


#Calculate UD factor
@callback(
    Output("ud_factor", "children"),
    Input("material_rpm", "value"),
    Input("wheel_width", "value"),
    Input("traverse_feed", "value"),

    #prevent_initial_call=True
)
def wheel_sync_input(material_rpm, wheel_width, traverse_feed):

    ud = (material_rpm*wheel_width) / traverse_feed
    return ud