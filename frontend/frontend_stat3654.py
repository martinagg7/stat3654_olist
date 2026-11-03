from dash import Dash, html, dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
my_app = Dash(__name__, external_stylesheets=external_stylesheets,
              suppress_callback_exceptions=True)
server = my_app.server

#%% Overview
overview_layout = html.Div([
    html.H2("Olist E-Commerce Dataset Analysis"),
    html.P("Kate Pierce (Front End) and Martina Garcia (Back End)"),

    html.H4("About the Dataset"),
    html.P("Olist is a Brazilian e-commerce company that connects small businesses to "
           "online marketplaces. The public dataset contains real, anonymized orders "
           "placed between 2016 and 2018, including product details, pricing, payment "
           "method, customer location, and shipping status."),

    html.H4("About the Project"),
    html.P("We explore the Olist data through visualizations and apply data analytics "
           "techniques to better understand customers and orders."),
])

#%% Numerical
numerical_layout = html.Div([
    html.H2("Numerical Features"),
    html.P("[Placeholder: histograms, boxplots, scatterplots]"),
])

#%% Categorical
categorical_layout = html.Div([
    html.H2("Categorical Features"),
    html.P("[Placeholder: bar charts and pie charts]"),
])

#%% Combined
combined_layout = html.Div([
    html.H2("Combined Features"),
    html.P("[Placeholder: numerical by categorical comparisons]"),
])

#%% Data Analytics
analytics_layout = html.Div([
    html.H2("Data Analytics"),
    html.P("[Placeholder: PCA, clustering, and other analysis results]"),
])

#%% Layout
my_app.layout = html.Div([
    html.H1("Olist E-Commerce Dashboard", style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[overview_layout]),
        dcc.Tab(label='Numerical', children=[numerical_layout]),
        dcc.Tab(label='Categorical', children=[categorical_layout]),
        dcc.Tab(label='Combined', children=[combined_layout]),
        dcc.Tab(label='Data Analytics', children=[analytics_layout]),
    ])
])

#%% Run
if __name__ == "__main__":
    my_app.run(debug=False, port=8050, host='0.0.0.0')