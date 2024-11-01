import requests
from dash import Dash, html, dcc, Input, Output, State
import dash_table
import pandas as pd

app = Dash(__name__)

# Define a function to fetch player data from the backend API
def get_player_projections(player_name):
    response = requests.get(f"http://localhost:5000/api/player_projections?name={player_name}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame()

app.layout = html.Div([
    html.H1("Fantasy Valuation Dashboard"),
    dcc.Input(id="input-player", type="text", placeholder="Enter player name"),
    html.Button("Submit", id="submit-button"),
    html.Div(id="output-table")
])

@app.callback(
    Output("output-table", "children"),
    Input("submit-button", "n_clicks"),
    State("input-player", "value")
)
def update_output(n_clicks, player_name):
    if n_clicks and player_name:
        # Call the backend API to get projections
        projections = get_player_projections(player_name)
        return dash_table.DataTable(data=projections.to_dict('records'))

if __name__ == "__main__":
    app.run_server(debug=True)
