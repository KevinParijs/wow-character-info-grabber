import dash
from dash import dcc, html, dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

data_list = [
    {'level': '80', 'Player name': 'Seeddy', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '584', 'Race': 'Blood Elf', 'Class': 'Mage', 'Specc': 'Arcane', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Cordulá', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '583', 'Race': 'Night Elf', 'Class': 'Death Knight', 'Specc': 'Frost', 'Faction': 'Alliance'},
    {'level': '80', 'Player name': 'Khaelitha', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '579', 'Race': 'Orc', 'Class': 'Warlock', 'Specc': 'Affliction', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Màzè', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '577', 'Race': "Mag'har Orc", 'Class': 'Warrior', 'Specc': 'Fury', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Grenm', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '575', 'Race': 'Undead', 'Class': 'Rogue', 'Specc': 'Assassination', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Mattdeamon', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '575', 'Race': 'Orc', 'Class': 'Warlock', 'Specc': 'Demonology', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Salmena', 'Player realm': 'Twilights-Hammer', 'Role': 'DPS', 'Total ilvl': '575', 'Race': 'Night Elf', 'Class': 'Hunter', 'Specc': 'Marksmanship', 'Faction': 'Alliance'},
    {'level': '80', 'Player name': 'Spekkies', 'Player realm': 'Stormscale', 'Role': 'Healer', 'Total ilvl': '575', 'Race': 'Orc', 'Class': 'Shaman', 'Specc': 'Restoration', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Mikdiff', 'Player realm': 'Stormscale', 'Role': 'Healer', 'Total ilvl': '574', 'Race': 'Blood Elf', 'Class': 'Paladin', 'Specc': 'Holy', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Ashulus', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '573', 'Race': 'Blood Elf', 'Class': 'Paladin', 'Specc': 'Retribution', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Nravitsya', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '573', 'Race': "Mag'har Orc", 'Class': 'Hunter', 'Specc': 'Survival', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Naraaya', 'Player realm': 'Draenor', 'Role': 'Healer', 'Total ilvl': '572', 'Race': 'Blood Elf', 'Class': 'Paladin', 'Specc': 'Retribution', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Lozoot', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '571', 'Race': 'Dracthyr', 'Class': 'Evoker', 'Specc': 'Devastation', 'Faction': 'Alliance'},
    {'level': '80', 'Player name': 'Endorielle', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '570', 'Race': 'Blood Elf', 'Class': 'Mage', 'Specc': 'Arcane', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Diawar', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '567', 'Race': 'Night Elf', 'Class': 'Warrior', 'Specc': 'Fury', 'Faction': 'Alliance'},
    {'level': '80', 'Player name': 'Drveni', 'Player realm': 'Stormscale', 'Role': 'Tank', 'Total ilvl': '566', 'Race': 'Troll', 'Class': 'Druid', 'Specc': 'Guardian', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Karadin', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '566', 'Race': 'Human', 'Class': 'Paladin', 'Specc': 'Retribution', 'Faction': 'Alliance'},
    {'level': '80', 'Player name': 'Kyotetsu', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '566', 'Race': 'Blood Elf', 'Class': 'Demon Hunter', 'Specc': 'Havoc', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Drexyl', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '565', 'Race': 'Void Elf', 'Class': 'Warlock', 'Specc': 'Demonology', 'Faction': 'Alliance'},
    {'level': '80', 'Player name': 'Gumayushi', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '565', 'Race': 'Nightborne', 'Class': 'Monk', 'Specc': 'Windwalker', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Respite', 'Player realm': 'Draenor', 'Role': 'DPS', 'Total ilvl': '565', 'Race': 'Blood Elf', 'Class': 'Death Knight', 'Specc': 'Unholy', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Artix', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '559', 'Race': 'Blood Elf', 'Class': 'Paladin', 'Specc': 'Retribution', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Skausyskaus', 'Player realm': 'Draenor', 'Role': 'DPS', 'Total ilvl': '557', 'Race': 'Troll', 'Class': 'Priest', 'Specc': 'Shadow', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Macamonk', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '556', 'Race': 'Pandaren', 'Class': 'Monk', 'Specc': 'Windwalker', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Puffdrakey', 'Player realm': 'Tarren-Mill', 'Role': 'Healer', 'Total ilvl': '552', 'Race': 'Dracthyr', 'Class': 'Evoker', 'Specc': 'Preservation', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Magnushunter', 'Player realm': 'Stormscale', 'Role': 'DPS', 'Total ilvl': '543', 'Race': 'Orc', 'Class': 'Hunter', 'Specc': 'Beast Mastery', 'Faction': 'Horde'},
    {'level': '80', 'Player name': 'Jadee', 'Player realm': 'Stormscale', 'Role': 'Healer', 'Total ilvl': '534', 'Race': 'Troll', 'Class': 'Druid', 'Specc': 'Restoration', 'Faction': 'Horde'},
    {'level': '78', 'Player name': 'Kixdk', 'Player realm': 'Stormscale', 'Role': 'Tank', 'Total ilvl': '521', 'Race': 'Blood Elf', 'Class': 'Death Knight', 'Specc': 'Frost', 'Faction': 'Horde'},
    {'level': '70', 'Player name': 'Telepatic', 'Player realm': 'Stormscale', 'Role': 'Tank', 'Total ilvl': '513', 'Race': 'Zandalari Troll', 'Class': 'Paladin', 'Specc': 'Protection', 'Faction': 'Horde'}
]

# List of classes
classes = ['Paladin', 'Death Knight', 'Hunter', 'Warlock', 'Druid', 'Evoker', 'Mage', 'Monk', 'Warrior', 'Demon Hunter', 'Priest', 'Rogue', 'Shaman']

# Corresponding player count
player_count = [6, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1]

# Official World of Warcraft class colors
colors = ['#F58CBA', '#C41E3A', '#ABD473', '#8787ED', '#FF7D0A', '#33937F', '#40C7EB', '#00FF96', '#C79C6E', '#A330C9', '#FFFFFF', '#FFF569', '#0070DE']

app.layout = html.Div([
    html.H1("World of Warcraft Class Distribution", style={'color': '#FFFFFF'}),
    
    dcc.Dropdown(
        id='class-filter',
        options=[{'label': cls, 'value': cls} for cls in classes],
        value=classes,  # Default to showing all classes
        multi=True
    ),

    dcc.Graph(id='bar-chart'),

    # Reset button
    html.Button('Reset Table', id='reset-button', n_clicks=0, style={'margin-top': '20px','margin-bottom': '20px', 'backgroundColor': '#888888', 'color': '#FFFFFF'}),

    # Hidden div to store the state of reset button
    html.Div(id='reset-state', style={'display': 'block'}, children='not_clicked'),
    
    # Data table
    dash_table.DataTable(
        id='player-table',
        columns=[{'name': col, 'id': col} for col in data_list[0].keys()],
        data=data_list,
        sort_action='native',  # Enable sorting on columns
        style_table={'overflowX': 'auto'},  # Enable horizontal scrolling if needed
        style_cell={'textAlign': 'left', 'backgroundColor': '#333333', 'color': '#FFFFFF'},
        style_header={'backgroundColor': '#444444', 'color': '#FFFFFF', 'fontWeight': 'bold'},
        style_data_conditional=[  # Apply conditional formatting
            {
                'if': {'column_id': 'Faction', 'filter_query': '{Faction} = "Horde"'},
                'backgroundColor': '#880000',
                'color': 'white',
            },
            {
                'if': {'column_id': 'Faction', 'filter_query': '{Faction} = "Alliance"'},
                'backgroundColor': '#004488',
                'color': 'white',
            }
        ]
    )
], style={'backgroundColor': '#333333', 'color': '#FFFFFF', 'padding': '20px'})

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('class-filter', 'value')]
)
def update_figure(selected_classes):
    filtered_count = [player_count[classes.index(cls)] for cls in selected_classes]
    filtered_colors = [colors[classes.index(cls)] for cls in selected_classes]

    return {
        'data': [
            go.Bar(
                x=selected_classes,
                y=filtered_count,
                marker={'color': filtered_colors},  # Apply the official WoW class colors
                text=filtered_count,  # Display data values on bars
                textposition='inside',  # Position text inside the bars
                insidetextanchor='end'  # Align text to the top of the bars
            )
        ],
        'layout': go.Layout(
            title='Distribution of Players by Class',
            # xaxis={'title': 'Class'},
            yaxis={'title': 'Number of Players'},
            plot_bgcolor='#333333',  # Set plot background color to match the page
            paper_bgcolor='#333333',  # Set paper background color to match the page
            font={'color': '#FFFFFF'},  # Set font color to white for better visibility
            margin={'l': 40, 'r': 20, 't': 40, 'b': 60},  # Adjust margins for better display
        )
    }

@app.callback(
    [Output('player-table', 'data'), Output('reset-state', 'children')],
    [Input('bar-chart', 'clickData'), Input('reset-button', 'n_clicks')],
    [State('reset-state', 'children')]
)
def update_table_on_click(click_data, n_clicks, reset_state):
    if n_clicks > 0 and reset_state != 'clicked':  # Reset the table when reset button is clicked
        return data_list, 'clicked'  # Reset to full dataset and mark reset as clicked
    
    if click_data is None or reset_state == 'clicked':
        return data_list, 'not_clicked'  # If no bar is clicked or after reset, return all data and mark reset as not clicked

    selected_class = click_data['points'][0]['x']  # Get the class name from the clicked bar
    filtered_data = [player for player in data_list if player['Class'] == selected_class]

    return filtered_data, 'not_clicked'  # Filter the table based on the clicked bar and reset the state to not clicked

if __name__ == '__main__':
    app.run_server(debug=True)
