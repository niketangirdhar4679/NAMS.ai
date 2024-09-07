import plotly.express as px
import dash
from dash import dcc, html

app = dash.Dash(__name__)

def create_visualization(data):
    fig = px.scatter(data, x='location', y='accident_severity', color='weather')
    return fig

app.layout = html.Div([
    dcc.Graph(figure=create_visualization(crash_data)),
])

if __name__ == '__main__':
    app.run_server(debug=True)
