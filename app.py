import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web

from pandas_datareader import wb

df = pd.read_csv('assets/southamericaworldbank.csv')

import json

with open('southamerica.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)
    
country_id_map = {}
for feature in json_data['features']:
    feature["id"] = feature["properties"]["iso_a2"]
    country_id_map[feature["properties"]["name_sort"]] = feature["id"]

df["id"] = df["Country"].apply(lambda x: country_id_map[x])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Innovation in South America - Inputs",
                        className='text-center mt-4 mb-4'),
                width=12),
    ),
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    "Dashboard of Innovation Indicators (Inputs) for South American countries inspired by the ", 
                    html.A(
                        "Global Innovation Index 2023",
                        href='https://www.wipo.int/edocs/pubdocs/en/wipo-pub-2000-2023-en-main-report-global-innovation-index-2023-16th-edition.pdf',
                        target="_blank",
                        style={'color': '#2F8FE8',
                        'text-decoration': 'none'},
                        id='wipo-link',
                    ),
                    " from the World Intellectual Property Organization (WIPO) with data from the ",
                    html.A(
                        "World Bank.",
                        href='https://databank.worldbank.org/source/world-development-indicators#',
                        target="_blank",
                        style={'color': '#2F8FE8',
                        'text-decoration': 'none'},
                        id='world-bank-link',
                    ),
                ]
            ),
            width=12
        ),
    ),
    dbc.Row(
        dbc.Col(html.H2("Infrastructure",
                        className=' mb-4'),
                width=12)
    ),

    dbc.Row([
        #INFRASTRUCTURE MAP
        dbc.Col([            
            dcc.Dropdown(
                id='infrastructure-map-column-dropdown',
                options=[
                    {'label': '% Electricity Access', 'value': '% Electricity Access'},
                    {'label': '% Electricity Access Rural', 'value': '% Electricity Access Rural'},
                    {'label': '% Electricity Access Urban', 'value': '% Electricity Access Urban'},
                    {'label': 'Mobile phone subscriptions per 100', 'value': 'Mobile phone subscriptions per 100'},
                    {'label': '% Internet Users', 'value': '% Internet Users'},
                ],
                value='% Electricity Access',
                #value=''% Electricity Access',  # Default values
                multi=False  # Allow multiple selections
            ),
            dcc.Graph(id='infrastructure-map'),             
        ],# width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=5, xl=5,
        ),
        
        #LINE GRAPH INFRASTRUCTURE
        dbc.Col([            
            dcc.Dropdown(
                id='infrastructure-line-column-dropdown',
                options=[
                    {'label': '% Electricity Access', 'value': '% Electricity Access'},
                    {'label': '% Electricity Access Rural', 'value': '% Electricity Access Rural'},
                    {'label': '% Electricity Access Urban', 'value': '% Electricity Access Urban'},
                    {'label': 'Mobile phone subscriptions per 100', 'value': 'Mobile phone subscriptions per 100'},
                    {'label': '% Internet Users', 'value': '% Internet Users'},
                ],
                value=['% Electricity Access'],
                #value=''% Electricity Access',  # Default values
                multi=True  # Allow multiple selections
            ),
            dcc.Graph(id='infrastructure-line-plot', style={'border-radius': '15px'},),
            
        ],# width={'size':5, 'offset':1, 'order':1},
        xs=12, sm=12, md=12, lg=7, xl=7,
        ),
    ],className=' mb-4'),
    #HUMAN CAPITAL PART
    dbc.Row(
        dbc.Col(html.H2("Human Capital",
                        className=' mb-4'),
                width=12)
    ),
    dbc.Row([
        #HUMAN CAPITAL
        dbc.Col([            
            dcc.Dropdown(
                id='humancapital-heatmap-column-dropdown',
                options=[
                    {'label': 'Government expenditure on education, total (% of GDP)', 'value': 'Government expenditure on education, total (% of GDP)'},
                    {'label': 'Pupil-teacher ratio Primary', 'value':  'Pupil-teacher ratio Primary'},
                    {'label': 'Pupil-teacher ratio Secondary', 'value': 'Pupil-teacher ratio Secondary'},
                    {'label': 'School enrollment Tertiary', 'value': 'School enrollment Tertiary'},
                ],               
                value='Government expenditure on education, total (% of GDP)',
                multi=False  # Allow multiple selections
            ),
            dcc.Graph(id='humancapital-heatmap'),             
        ],# width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=5, xl=5,
        ),
        #LINE GRAPH HUMAN
        dbc.Col([            
            dcc.Dropdown(
                id='humancapital-line-column-dropdown',
                options=[
                    {'label': 'Government expenditure on education, total (% of GDP)', 'value': 'Government expenditure on education, total (% of GDP)'},
                    {'label': 'Pupil-teacher ratio Primary', 'value':  'Pupil-teacher ratio Primary'},
                    {'label': 'Pupil-teacher ratio Secondary', 'value': 'Pupil-teacher ratio Secondary'},
                    {'label': 'School enrollment Tertiary', 'value': 'School enrollment Tertiary'},
                ],
                value=['Government expenditure on education, total (% of GDP)'],
                multi=True  # Allow multiple selections
            ),
            dcc.Graph(id='humancapital-line-plot', style={'border-radius': '15px'},),
            
        ],# width={'size':5, 'offset':1, 'order':1},
        xs=12, sm=12, md=12, lg=7, xl=7,
        ),
    ],className='mb-4'),
    #INSTITUTIONS AND MARKET SOPHISTICATION PART
    dbc.Row(
        dbc.Col(html.H2("Institutions and Market sophistication",
                        className=' mb-4'),
                width=12)
    ),
    dbc.Row([
        #INSTITUTIONS AND MARKET SOPHISTICATION
        dbc.Col([            
            dcc.Dropdown(
                id='institutionmarket-heatmap-column-dropdown',
                options=[
                    {'label': 'Regulatory Quality: Estimate', 'value': 'Regulatory Quality: Estimate'},
                    {'label': 'Government Effectiveness: Estimate', 'value':  'Government Effectiveness: Estimate',},
                    {'label': 'Rule of Law: Estimate', 'value': 'Rule of Law: Estimate',},
                    {'label': 'Domestic credit to private sector (% of GDP)', 'value': 'Domestic credit to private sector (% of GDP)',},
                ], 
                value='Regulatory Quality: Estimate',
                multi=False  # Allow multiple selections
            ),
            dcc.Graph(id='institutionmarket-heatmap'),             
        ],# width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=5, xl=5,
        ),
        #LINE GRAPH HUMAN
        dbc.Col([            
            dcc.Dropdown(
                id='institutionmarket-line-column-dropdown',
                options=[
                    {'label': 'Regulatory Quality: Estimate', 'value': 'Regulatory Quality: Estimate'},
                    {'label': 'Government Effectiveness: Estimate', 'value':  'Government Effectiveness: Estimate',},
                    {'label': 'Rule of Law: Estimate', 'value': 'Rule of Law: Estimate',},
                    {'label': 'Domestic credit to private sector (% of GDP)', 'value': 'Domestic credit to private sector (% of GDP)',},
                ],
                value=['Regulatory Quality: Estimate'],
                multi=True  # Allow multiple selections
            ),
            dcc.Graph(id='institutionmarket-line-plot', style={'border-radius': '15px'},),
            
        ],# width={'size':5, 'offset':1, 'order':1},
        xs=12, sm=12, md=12, lg=7, xl=7,
        ),
    ],),
    dbc.Row(
        dbc.Col(html.P("Sebastián D. Rosado,  2024",
                       style={'textAlign': 'right'},
                       className='text-align-right mt-4 mb-4'),
                width=12),
    ),
], fluid=True)

# Callback INFRASTRUCURE MAP
@app.callback(
    Output('infrastructure-map', 'figure'),
    [Input('infrastructure-map-column-dropdown', 'value')]
)
def update_infrastructure_map_plot(selected_column):
    # Create line plot using Plotly Express
    fig = px.choropleth(
        df,
        locations="id",
        geojson=json_data,
        color=selected_column,
        hover_name="Country",
        color_continuous_scale=px.colors.sequential.deep,
        template='plotly_white',
        #hover_data=["Density"],
        #title="",
        animation_frame="Year",

    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin=dict(l=50, r=50, t=50, b=50), autosize=True, hovermode='closest',
                         ##geo=dict(
                            ##center=dict(lon=0, lat=0),  # Set the center of the map (longitude, latitude)
                            ##projection_scale=1,         # Adjust the scale of the map projection
                            ##visible=True,               # Set the map to be initially visible
                            #scope='world',              # Set the geographic scope (e.g., 'world', 'usa', 'europe')                    
                    ##)
    )
    return fig

# Callback INFRASTRUCTURE LINE
@app.callback(
    Output('infrastructure-line-plot', 'figure'),
    [Input('infrastructure-line-column-dropdown', 'value')]
)
def update_infrastructure_line_plot(selected_column2):
    # Create line plot using Plotly Express
    fig2 = px.line(
        df,
        x="Year",
        y=selected_column2,
        color='Country',
        line_dash='variable',
        labels={'variable': 'Year', 'value': 'Selected Columns'},
        template='plotly_white',
        title=f'{selected_column2} Over Time',)  
    fig2.update_layout(
        title=dict(
            font=dict(size=16)  # Set the desired font size
        )
    )
    return fig2


###############
# Callback HUMAN CAPITAL HEATMAP
@app.callback(
    Output('humancapital-heatmap', 'figure'),
    [Input('humancapital-heatmap-column-dropdown', 'value')]
)
def update_humancapital_map_plot(selected_column):
    # Create line plot using Plotly Express

    fig = px.imshow(
        df.pivot(index='Country', columns='Year', values=selected_column),
        template='plotly_white',
        labels={"value": selected_column},
        color_continuous_scale=px.colors.sequential.deep,
    )    
    return fig

# Callback HUMAN CAPITAL LINE
@app.callback(
    Output('humancapital-line-plot', 'figure'),
    [Input('humancapital-line-column-dropdown', 'value')]
)
def update_humancapital_line_plot(selected_column2):
    # Create line plot using Plotly Express
    fig2 = px.line(
        df,
        x="Year",
        y=selected_column2,
        color='Country',
        line_dash='variable',
        labels={'variable': 'Year', 'value': 'Selected Columns'},
        template='plotly_white',
        title=f'{selected_column2} Over Time',)  
    fig2.update_layout(
        title=dict(
            font=dict(size=16)  # Set the desired font size
        )
    )
    return fig2

###############
# Callback Institutions and Market sophistication HEATMAP
@app.callback(
    Output('institutionmarket-heatmap', 'figure'),
    [Input('institutionmarket-heatmap-column-dropdown', 'value')]
)
def update_institutions_map_plot(selected_column):
    # Create line plot using Plotly Express

    fig = px.imshow(
        df.pivot(index='Country', columns='Year', values=selected_column),
        template='plotly_white',
        labels={"value": selected_column},
        color_continuous_scale=px.colors.sequential.deep,
    )    
    return fig


# Callback Institutions and Market sophistication LINE
@app.callback(
    Output('institutionmarket-line-plot', 'figure'),
    [Input('institutionmarket-line-column-dropdown', 'value')]
)
def update_institutions_line_plot(selected_column2):
    # Create line plot using Plotly Express
    fig2 = px.line(
        df,
        x="Year",
        y=selected_column2,
        color='Country',
        line_dash='variable',
        labels={'variable': 'Year', 'value': 'Selected Columns'},
        template='plotly_white',
        title=f'{selected_column2} Over Time',)  
    fig2.update_layout(
        title=dict(
            font=dict(size=16)  # Set the desired font size
        )
    )
    return fig2

##############

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
