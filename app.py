import dash
from dash import dcc, html  # Updated import for Dash 2.0+
import pandas as pd
from sqlalchemy import create_engine

# Initialize the Dash app
app = dash.Dash(__name__)

# Load data from the database
def fetch_data():
    # Update this connection string with your actual database credentials
    engine = create_engine("postgresql://username:password@localhost:5432/baseball")
    df = pd.read_sql("SELECT * FROM processed_statcast", engine)
    return df

df = fetch_data()

# Create app layout
app.layout = html.Div(children=[
    html.H1(children='Statcast Dashboard'),
    dcc.Graph(
        id='launch-speed-vs-angle',
        figure={
            'data': [
                {'x': df['launch_angle'], 'y': df['launch_speed'], 'type': 'scatter', 'name': 'Hits'},
            ],
            'layout': {
                'title': 'Launch Speed vs Launch Angle'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
