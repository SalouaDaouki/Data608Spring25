import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import seaborn as sns

df = sns.load_dataset("penguins")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Penguin Data Explorer"),
    dcc.Dropdown(
        id='x-axis',
        options=[{'label': col, 'value': col} for col in ['bill_length_mm', 'flipper_length_mm']],
        value='bill_length_mm'
    ),
    dcc.Graph(id='scatter-plot')
])

@app.callback(
    Output('scatter-plot', 'figure'),
    Input('x-axis', 'value')
)
def update_graph(x_axis):
    fig = px.scatter(df, x=x_axis, y='body_mass_g', color='species')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
