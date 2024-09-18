from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

# initialize app
app = Dash()

# app layout
app.layout = [
    html.Div(className='row', children='Self-employment Income Tax', style={'textAlign': 'center', 'fontSize': 30}),
    html.Div(className='row', children=[
        dcc.Input(id='daily-rate', type='number', min=0, value=500), 
        dcc.Input(id='days-worked', type='number', min=0, value=220)
        ]),
    html.Div(id='yearly-income')
]

@callback(
    Output(component_id='yearly-income', component_property='children'),
    Input(component_id='daily-rate', component_property='value'),
    Input(component_id='days-worked', component_property='value'),
)
def update_income(daily_rate, days_worked):
    yearly_income = daily_rate * days_worked
    return yearly_income


if __name__ == "__main__":
    app.run(debug=True)