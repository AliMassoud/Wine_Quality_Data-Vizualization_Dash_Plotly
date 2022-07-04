from cProfile import label
from inspect import trace
from itertools import count
from turtle import color
from unicodedata import name
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import MinMaxScaler

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("winequality.csv")

#PREPARING THE GRAPHS
# options = df[['MentHlth', 'PhysHlth', 'GenHlth']]

# fig = px.scatter(df, x="MentHlth", y="BMI", color = 'MentHlth', log_x=True, size_max=20)

# fig2 = px.scatter(df, x="PhysHlth", y="BMI", color = 'PhysHlth', log_x=True, size_max=20)

# fig3 = px.box(df, x="Smoker", y="Age", color='Diabetes_012')  # add quartile



# fig4 = px.bar(df, x='Education', y = 'PhysHlth', color='Education')




fig = px.histogram(df, x="pH")
# fig = px.line(df, x="citric acid", y="alcohol", title='Life expectancy in Canada')

# fig2 = px.bar(df, x='type', y='quality', color='type')
# fig2 = px.pie(df, values='quality', names='type')
# fig2 = px.scatter(df, x="density", y="quality", color = 'quality', log_x=True, size_max=20)

fig2 = make_subplots(rows=1, cols=2)

fig2.add_trace(
    # px.scatter(df, x="density", y="quality", color = 'quality', log_x=True, size_max=20),
    # go.Scatter(x=df['density'], y=df['quality']),
    # go.Box(df, x="alcohol", y="quality", color='quality'),  # add quartile
    go.Bar(x=df['type'], y=df['quality'], marker=dict(color=df['type'], coloraxis="coloraxis")),
    row=1, col=1
)

fig2.add_trace(
    go.Scatter(x=df['alcohol'], y=df['quality']),
    # px.scatter(df, x="alcohol", y="quality", color = 'quality', log_x=True, size_max=20),
    row=1, col=2
)


# @app.callback(
#     Output("graph", "figure"), 
#     Input("dropdown", "value"))
# def update_bar_chart(value):
#     df = pd.read_csv("diabetes_health_indicators.csv")
#     print("I am heree")
#     print(value)
#     mask = df["Diabetes_012"] == value
#     print(mask.head())
#     fig = px.bar(df[mask], x="Diabetes_012", y="Age", 
#                  color="Smoker", barmode="group")
#     return fig


# fig3 = px.treemap(df, path = ['runtime'],
#                           values = 'runtime',
#                           color  = 'type')

# fig4 = px.line(df, x = frequencies.keys(), y = frequencies.values())

app.layout = html.Div(children=[
    html.H1(children='Wine Quality Data Visualization'),
    html.H3(children='Ali Massoud'),
    html.H3(children='Ali Massoud'),
    html.Div(children=[
        dcc.Graph(
        id='graph',
        figure=fig        
    ),
    html.P("Mean:"),
    dcc.Slider(id="mean", min=-3, max=3, value=0, 
               marks={-3: '-3', 3: '3'}),
    ],style={'width': '100vh', 'height': '90vh'}),
    html.Div(children=[
        html.H2(children='In this graph we show the rarity of wine with good quality and less density'),
        dcc.Graph(
        id='quality_density',
        figure=fig2
    )
    ])
])

@app.callback(
    Output("graph", "figure"), 
    Input("mean", "value"))
def display_color(mean):
    # data = np.random.normal(mean, std, size=800) # replace with your own data source
    # data = max_min_scaler.fit_transform(df['MEAN_TEMPERATURE_MONTREAL'])
    data = pd.DataFrame()
    data['pH'] = df['pH'].values - mean
    fig = px.histogram(data, range_x=[-10, 10])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)


    # ,
    # dcc.Dropdown(
    #     id="dropdown",
    #     options=['0', '1', '2'],
    #     value="0",
    #     clearable=False,
    # ),
    # dcc.Graph(id="graph"),
    # dcc.Graph(
    #     id='BMI_PhysHlth',
    #     figure=fig2
    # ),
    # dcc.Graph(
    #     id='Smoker_Diabetes',
    #     figure=fig3
    # )