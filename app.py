import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html


from components import Column, Header, Row
# from auth import auth

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Optionally display a log in screen.                                                                   #
# If `REQUIRE_LOGIN = True` in `config.py`, then auth_instance allows you to programatically access the #
# username of the currently logged in user.                                                             #
# If `REQUIRE_LOGIN = False`, then no login screen will be displayed and `auth_instance` will be `None` #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# auth_instance = auth(app)

server = app.server  # Expose the server variable for deployments

# Standard Dash app code below
app.layout = html.Div(children=[
    dcc.Tabs(id='tabs', children=[
        dcc.Tab(id='website', label='Website', children=[
            html.Div(children=[
                # This will track the progression of the test
                html.P(id='test_phase', children=0, style={'display': 'none'}),
                html.P(id='data', children=[0, 0, 0], style={'display': 'none'}),
                # Tested website
                html.H1(id='title', children='eLibrary UX Design Test'),
                html.Button(id='test_start', children='Start Test', n_clicks=0),
                html.Button(id='test_end', children='End Test', n_clicks=0, style={'display': 'none'}),
                html.Hr(),
                html.P(id='text'),
                html.Hr(),
                html.H5('Yunke\'s eLibrary'),
                html.Div(id='books_section', children=[
                    html.Button(id='books', children='Books', n_clicks=0),
                    html.Br(),
                    html.Button(id='lord_of_the_flies', children='Lord Of The Flies', n_clicks=0),
                    html.Button(id='uzumaki', children='Uzumaki', n_clicks=0),
                    html.P(id='uzumaki_phase', children=0, style={'display': 'none'}),  # Uzumaki state
                    html.Button(id='the_art_of_war', children='The Art Of War', n_clicks=0),
                    html.Button(id='the_prince', children='The Prince', n_clicks=0),
                    html.P(id='the_prince_phase', children=0, style={'display': 'none'})  # The Prince state
                ]),
                html.Div(id='contact_section', children=[
                    html.Button(id='contact', children='Contact Us', n_clicks=0),
                    html.Br(),
                    html.Button(id='email', children='E-mail', n_clicks=0, style={'display': 'none'}),
                    html.P(id='email_phase', children=0, style={'display': 'none'}),  # Email state
                    html.Button(id='phone', children='Phone', n_clicks=0, style={'display': 'none'})
                ]),
                html.Button(id='submit', children='Submit Test'),
                html.P(id='submit_phase', children=0, style={'display': 'none'}),  # Submit state
            ])
        ]),
        dcc.Tab(id='analytics', label='Test Results', children=[
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'All Results', 'value': 'tests'},
                    {'label': 'Test 1 Results', 'value': 'test_1'},
                    {'label': 'Test 2 Results', 'value': 'test_2'},
                    {'label': 'Test 3 Results', 'value': 'test_3'}
                ],
                value='tests'),
            html.Div(children=[

                # Test 1
                # --------------------------------------------------------------------------------------------------------
                html.Div(
                    id='test_1',
                    className='row',
                    children=[
                        html.Div(
                            id='test_1_data',
                            children=[0, 5, 10, 11, 4, 2, 0, 1, 0, 1],
                            style={'display': 'none'}
                        ),
                        html.Div(
                            className='five columns',
                            children=[
                                dcc.Graph(
                                    id='test_1_bar',
                                    figure={
                                        'data': [
                                            {
                                                'x': [i for i in range(1, 11)],
                                                'y': [],
                                                'type': 'bar',
                                                'marker': {
                                                    'color': ['rgba(30,144,255,0.8)', 'rgba(255,140,0,0.8)'] +
                                                             ['rgba(30,144,255,0.8)' for i in range(8)]
                                                },
                                            },
                                        ],
                                        'layout': {
                                            'title': 'Number Of Clicks Used In Test 1',
                                            'xaxis': {
                                                'dtick': 1
                                            },
                                            'yaxis': {
                                                'dtick': 1
                                            },
                                            'autosize': True,
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    }
                                )]),
                        html.Div(
                            className='five columns',
                            children=[
                                dcc.Graph(
                                    id='test_1_pie',
                                    figure={
                                        'data': [
                                            {
                                                'labels': [str(i) + ' clicks' for i in range(1, 11)],
                                                'values': [],
                                                'type': 'pie',
                                            },
                                        ],
                                        'layout': {
                                            'title': 'Distribution Of Performances In Test 1',
                                            'autosize': True,
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    }
                                )
                            ]
                        )
                    ]
                ),

                # Test 2
                # --------------------------------------------------------------------------------------------------------

                html.Div(
                    id='test_2',
                    className='row',
                    children=[
                        html.Div(
                            id='test_2_data',
                            children=[1, 15, 1, 12, 6, 0, 0, 0, 1, 0],
                            style={'display': 'none'}
                        ),
                        html.Div(
                            className='five columns',
                            children=[
                                dcc.Graph(
                                    id='test_2_bar',
                                    figure={
                                        'data': [
                                            {
                                                'x': [i for i in range(1, 11)],
                                                'y': [],
                                                'type': 'bar',
                                                'marker': {
                                                    'color': ['rgba(30,144,255,0.8)', 'rgba(255,140,0,0.8)'] +
                                                             ['rgba(30,144,255,0.8)' for i in range(8)]
                                                },
                                            },
                                        ],
                                        'layout': {
                                            'title': 'Number Of Clicks Used In Test 2',
                                            'xaxis': {
                                                'dtick': 1
                                            },
                                            'yaxis': {
                                                'dtick': 1
                                            },
                                            'autosize': True,
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    }
                                )]),
                        html.Div(
                            className='five columns',
                            children=[
                                dcc.Graph(
                                    id='test_2_pie',
                                    figure={
                                        'data': [
                                            {
                                                'labels': [str(i) + ' clicks' for i in range(1, 11)],
                                                'values': [],
                                                'type': 'pie',
                                            },
                                        ],
                                        'layout': {
                                            'title': 'Distribution Of Performances In Test 2',
                                            'autosize': True,
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    }
                                )
                            ]
                        )
                    ]
                ),

                # Test 3
                # --------------------------------------------------------------------------------------------------------
                html.Div(
                    id='test_3',
                    className='row',
                    children=[
                        html.Div(
                            id='test_3_data',
                            children=[0, 10, 11, 8, 6, 0, 3, 2, 1, 0],
                            style={'display': 'none'}
                        ),
                        html.Div(
                            className='five columns',
                            children=[
                                dcc.Graph(
                                    id='test_3_bar',
                                    figure={
                                        'data': [
                                            {
                                                'x': [i for i in range(1, 11)],
                                                'y': [],
                                                'type': 'bar',
                                                'marker': {
                                                    'color': ['rgba(30,144,255,0.8)', 'rgba(255,140,0,0.8)'] +
                                                             ['rgba(30,144,255,0.8)' for i in range(8)]
                                                },
                                            },
                                        ],
                                        'layout': {
                                            'title': 'Number Of Clicks Used In Test 3',
                                            'xaxis': {
                                                'dtick': 1
                                            },
                                            'yaxis': {
                                                'dtick': 1
                                            },
                                            'autosize': True,
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    }
                                )]),
                        html.Div(
                            className='five columns',
                            children=[
                                dcc.Graph(
                                    id='test_3_pie',
                                    figure={
                                        'data': [
                                            {
                                                'labels': [str(i) + ' clicks' for i in range(1, 11)],
                                                'values': [],
                                                'type': 'pie',
                                            },
                                        ],
                                        'layout': {
                                            'title': 'Distribution Of Performances In Test 3',
                                            'autosize': True,
                                        }
                                    },
                                    config={
                                        'displayModeBar': False
                                    }
                                )
                            ]
                        )
                    ]
                ),
            ])
        ])
    ])
])


# State Management
# -------------------------------------------------------------------------------------------------`-------
@app.callback(
    Output(component_id='test_phase', component_property='children'),
    [Input(component_id='test_start', component_property='n_clicks'),
     Input(component_id='test_end', component_property='n_clicks'),
     Input(component_id='the_prince_phase', component_property='children'),
     Input(component_id='uzumaki_phase', component_property='children'),
     Input(component_id='email_phase', component_property='children'),
     Input(component_id='submit_phase', component_property='children')
     ]
)
def state_stuff(s_clicks, e_clicks, the_prince_phase, uzumaki_phase, email_phase, sub_phase):
    if s_clicks == e_clicks or sub_phase == 1:
        return 0
    if s_clicks != 0 and the_prince_phase == 0 and uzumaki_phase == 0 and email_phase == 0:
        return 1
    if email_phase != 0:
        return 4
    if uzumaki_phase != 0:
        return 3
    if the_prince_phase != 0:
        return 2


# Start and End Test
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='test_start', component_property='style'),
    [Input(component_id='test_phase', component_property='children')]
)
def start_button(phase):
    if phase == 0:
        return {'display': 'inline'}
    else:
        return {'display': 'none'}


@app.callback(
    Output(component_id='test_end', component_property='style'),
    [Input(component_id='test_phase', component_property='children')]
)
def end_button(phase):
    if phase == 0 or phase == 4:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


# Test Text
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='text', component_property='children'),
    [Input(component_id='test_phase', component_property='children')]
)
def start_test(phase):
    if phase == 0:
        return 'When the test starts, you will try to accomplish the tasks that will be posted here.'
    if phase == 1:
        return 'Test 1: Read the book titled "The Prince".'
    if phase == 2:
        return 'Test 2: Read the book titled "Uzumaki".'
    if phase == 3:
        return 'Test 3: Send an e-mail to the owners of the eLibrary.'
    if phase == 4:
        return 'Test completed! Please press the submit button'


# Books Section
# --------------------------------------------------------------------------------------------------------

@app.callback(
    Output(component_id='books', component_property='style'),
    [Input(component_id='contact', component_property='n_clicks'),
     Input(component_id='test_phase', component_property='children')]
)
def books_visibility(n_clicks, phase):
    if phase == 4 or n_clicks % 2 != 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


@app.callback(
    Output(component_id='books', component_property='children'),
    [Input(component_id='books', component_property='n_clicks')]
)
def name_button(b_clicks):
    if b_clicks % 2 == 0:
        return 'Books'
    else:
        return 'Back'


@app.callback(
    Output(component_id='lord_of_the_flies', component_property='style'),
    [Input(component_id='books', component_property='n_clicks'),
     Input(component_id='contact', component_property='n_clicks'), ]
)
def lord_of_tje_flies_visibility(b_clicks, c_clicks):
    if b_clicks % 2 == 0 or c_clicks % 2 != 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


@app.callback(
    Output(component_id='uzumaki', component_property='style'),
    [Input(component_id='books', component_property='n_clicks'),
     Input(component_id='contact', component_property='n_clicks'), ]
)
def uzumaki_visibility(b_clicks, c_clicks):
    if b_clicks % 2 == 0 or c_clicks % 2 != 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


@app.callback(
    Output(component_id='the_art_of_war', component_property='style'),
    [Input(component_id='books', component_property='n_clicks'),
     Input(component_id='contact', component_property='n_clicks'), ]
)
def the_art_of_war_visibility(b_clicks, c_clicks):
    if b_clicks % 2 == 0 or c_clicks % 2 != 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


@app.callback(
    Output(component_id='the_prince', component_property='style'),
    [Input(component_id='books', component_property='n_clicks'),
     Input(component_id='contact', component_property='n_clicks'), ]
)
def the_prince_visibility(b_clicks, c_clicks):
    if b_clicks % 2 == 0 or c_clicks % 2 != 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


# Contact Section
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='contact', component_property='style'),
    [Input(component_id='books', component_property='n_clicks'),
     Input(component_id='test_phase', component_property='children')]
)
def contact_visibility(b_clicks, phase):
    if phase == 4 or b_clicks % 2 != 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


@app.callback(
    Output(component_id='contact', component_property='children'),
    [Input(component_id='contact', component_property='n_clicks')]
)
def contact_text(c_clicks):
    if c_clicks % 2 == 0:
        return 'Contact Us'
    else:
        return 'Back'


@app.callback(
    Output(component_id='email', component_property='style'),
    [Input(component_id='contact', component_property='n_clicks')]
)
def email_visibility(c_clicks):
    if c_clicks % 2 == 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


@app.callback(
    Output(component_id='phone', component_property='style'),
    [Input(component_id='contact', component_property='n_clicks')]
)
def phone_visibility(c_clicks):
    if c_clicks % 2 == 0:
        return {'display': 'none'}
    else:
        return {'display': 'inline'}


# Reset Buttons
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='books', component_property='n_clicks'),
    [Input(component_id='test_phase', component_property='children'),
     Input(component_id='lord_of_the_flies', component_property='n_clicks'),
     Input(component_id='uzumaki', component_property='n_clicks'),
     Input(component_id='the_art_of_war', component_property='n_clicks'),
     Input(component_id='the_prince', component_property='n_clicks')]
)
def reset_books(phase, lord_of_the_flies_clicks, uzumaki_n_clicks, the_art_of_war, the_prince):
    return 0


@app.callback(
    Output(component_id='contact', component_property='n_clicks'),
    [Input(component_id='test_phase', component_property='children'),
     Input(component_id='email', component_property='n_clicks'),
     Input(component_id='phone', component_property='n_clicks')]
)
def reset_contact(phase, email_clicks, phone_clicks):
    return 0


# Test 1
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='the_prince_phase', component_property='children'),
    [Input(component_id='the_prince', component_property='n_clicks'),
     Input(component_id='submit_phase', component_property='children')],
    [State('test_phase', 'children')]
)
def test_1(the_prince_clicks, submit_phase, phase):
    if submit_phase == 1 or phase != 1:
        return 0
    else:
        return 1


# Test 2
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='uzumaki_phase', component_property='children'),
    [Input(component_id='uzumaki', component_property='n_clicks'),
     Input(component_id='submit_phase', component_property='children')],
    [State('test_phase', 'children')]
)
def test_2(uzumaki_clicks, submit_phase, phase):
    if submit_phase == 1 or phase != 2:
        return 0
    else:
        return 1


# Test 3
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='email_phase', component_property='children'),
    [Input(component_id='email', component_property='n_clicks'),
     Input(component_id='submit_phase', component_property='children')],
    [State('test_phase', 'children')]
)
def test_3(email_clicks, submit_phase, phase):
    if submit_phase == 1 or phase != 3:
        return 0
    else:
        return 1


# Submit
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='submit', component_property='style'),
    [Input(component_id='test_phase', component_property='children')]
)
def submit_visibility(phase):
    if phase == 4:
        return {'display': 'inline'}
    else:
        return {'display': 'none'}


@app.callback(
    Output(component_id='submit_phase', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks'),
     Input(component_id='test_start', component_property='n_clicks')],
    [State('test_phase', 'children')]
)
def submit_phase(submit_clicks, s_clicks, phase):
    if phase == 4:
        return 1
    else:
        return 0


# Update Data
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='data', component_property='children'),
    [Input(component_id='books', component_property='n_clicks'),
     Input(component_id='lord_of_the_flies', component_property='n_clicks'),
     Input(component_id='uzumaki', component_property='n_clicks'),
     Input(component_id='the_art_of_war', component_property='n_clicks'),
     Input(component_id='the_prince', component_property='n_clicks'),
     Input(component_id='contact', component_property='n_clicks'),
     Input(component_id='email', component_property='n_clicks'),
     Input(component_id='phone', component_property='n_clicks'),
     Input(component_id='submit_phase', component_property='children')],
    [State('test_phase', 'children'),
     State('data', 'children')]
)
def update_data(books_clicks, lord_of_the_flies_clicks, uzumaki_clicks, the_art_of_war_clicks, the_prince,
                contact_clicks, email_clicks, phone_clicks, sub_phase, phase, data):
    dataset = data
    if sub_phase == 1:
        return [0, 0, 0]
    if phase == 1:
        dataset[0] += 1
        return dataset
    elif phase == 2:
        dataset[1] += 1
        return dataset
    elif phase == 3:
        dataset[2] += 1
        return dataset
    else:
        return dataset


# Test 1 Graph
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='test_1_data', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='test_1_data', component_property='children'),
     State(component_id='data', component_property='children')]
)
def update_test_1_data(sub_clicks, curr_data, new_data):
    dataset = curr_data
    new_dataset = new_data
    if new_dataset != [0, 0, 0]:
        dataset[new_dataset[0] - 1] += 1
    return dataset


@app.callback(
    Output(component_id='test_1_bar', component_property='figure'),
    [Input(component_id='test_1_data', component_property='children')],
    [State(component_id='test_1_bar', component_property='figure')]
)
def update_test_1_bar(data, figure):
    dataset = data
    new_figure = figure
    new_figure['data'][0]['y'] = dataset
    return new_figure


@app.callback(
    Output(component_id='test_1_pie', component_property='figure'),
    [Input(component_id='test_1_data', component_property='children')],
    [State(component_id='test_1_pie', component_property='figure')]
)
def update_test_1_pie(data, figure):
    dataset = data
    figure['data'][0]['values'] = dataset
    return figure


# Test 2 Graph
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='test_2_data', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='test_2_data', component_property='children'),
     State(component_id='data', component_property='children')]
)
def update_test_2_data(sub_clicks, curr_data, new_data):
    dataset = curr_data
    new_dataset = new_data
    if new_dataset != [0, 0, 0]:
        dataset[new_dataset[1] - 1] += 1
    return dataset


@app.callback(
    Output(component_id='test_2_bar', component_property='figure'),
    [Input(component_id='test_2_data', component_property='children')],
    [State(component_id='test_2_bar', component_property='figure')]
)
def update_test_2_bar(data, figure):
    dataset = data
    new_figure = figure
    new_figure['data'][0]['y'] = dataset
    return new_figure


@app.callback(
    Output(component_id='test_2_pie', component_property='figure'),
    [Input(component_id='test_2_data', component_property='children')],
    [State(component_id='test_2_pie', component_property='figure')]
)
def update_test_2_pie(data, figure):
    dataset = data
    figure['data'][0]['values'] = dataset
    return figure


# Test 3 Graph
# --------------------------------------------------------------------------------------------------------

@app.callback(
    Output(component_id='test_3_data', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='test_3_data', component_property='children'),
     State(component_id='data', component_property='children')]
)
def update_test_3_data(sub_clicks, curr_data, new_data):
    dataset = curr_data
    new_dataset = new_data
    if new_dataset != [0, 0, 0]:
        dataset[new_dataset[2] - 1] += 1
    return dataset


@app.callback(
    Output(component_id='test_3_bar', component_property='figure'),
    [Input(component_id='test_3_data', component_property='children')],
    [State(component_id='test_3_bar', component_property='figure')]
)
def update_test_3_bar(data, figure):
    dataset = data
    new_figure = figure
    new_figure['data'][0]['y'] = dataset
    return new_figure


@app.callback(
    Output(component_id='test_3_pie', component_property='figure'),
    [Input(component_id='test_3_data', component_property='children')],
    [State(component_id='test_3_pie', component_property='figure')]
)
def update_test_3_pie(data, figure):
    dataset = data
    figure['data'][0]['values'] = dataset
    return figure


# Dropdown
# --------------------------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='test_1', component_property='style'),
    [Input(component_id='dropdown', component_property='value')]
)
def test_1_visibility(value):
    if value == 'test_1' or value == 'tests':
        return {'display': 'inline'}
    else:
        return {'display': 'none'}


@app.callback(
    Output(component_id='test_2', component_property='style'),
    [Input(component_id='dropdown', component_property='value')]
)
def test_1_visibility(value):
    if value == 'test_2' or value == 'tests':
        return {'display': 'inline'}
    else:
        return {'display': 'none'}


@app.callback(
    Output(component_id='test_3', component_property='style'),
    [Input(component_id='dropdown', component_property='value')]
)
def test_1_visibility(value):
    if value == 'test_3' or value == 'tests':
        return {'display': 'inline'}
    else:
        return {'display': 'none'}



if __name__ == '__main__':
    app.run_server(debug=True)
