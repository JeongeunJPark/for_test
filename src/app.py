'''
 # @ Create Time: 2024-03-30 19:40:33.462492
'''

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__, title="for_test")
server = app.server

df_node = pd.read_csv('./data/df_node.csv')
df_edge = pd.read_csv('./data/df_edge.csv')
result = pd.read_csv('./data/test.csv')


colors = ['IndianRed', 'LightCoral', 'Salmon', 'DarkSalmon', 'LightSalmon', 'Crimson', 'Red',
          'FireBrick', 'DarkRed', 'Pink', 'LightPink', 'HotPink', 'DeepPink', 'MediumVioletRed',
          'PaleVioletRed', 'LightSalmon', 'Coral', 'Tomato', 'OrangeRed', 'DarkOrange', 'Orange',
          'Gold', 'Yellow', 'LightYellow', 'LemonChiffon', 'LightGoldenrodYellow', 'PapayaWhip',
          'Moccasin', 'PeachPuff', 'PaleGoldenrod', 'Khaki', 'DarkKhaki', 'Lavender', 'Thistle',
          'Plum', 'Violet', 'Orchid', 'Fuchsia', 'Magenta', 'MediumOrchid', 'MediumPurple', 'RebeccaPurple',
          'BlueViolet', 'DarkViolet', 'DarkOrchid', 'DarkMagenta', 'Purple', 'Indigo', 'SlateBlue',
          'DarkSlateBlue', 'MediumSlateBlue', 'GreenYellow', 'Chartreuse', 'LawnGreen', 'Lime', 'LimeGreen',
          'PaleGreen', 'LightGreen', 'MediumSpringGreen', 'SpringGreen', 'MediumSeaGreen', 'SeaGreen',
          'ForestGreen', 'Green', 'DarkGreen', 'YellowGreen', 'OliveDrab', 'Olive', 'DarkOliveGreen',
          'MediumAquamarine', 'DarkSeaGreen', 'LightSeaGreen', 'DarkCyan', 'Teal', 'Aqua', 'Cyan', 'LightCyan',
          'PaleTurquoise', 'Aquamarine', 'Turquoise', 'MediumTurquoise', 'DarkTurquoise', 'CadetBlue', 'SteelBlue',
          'LightSteelBlue', 'PowderBlue', 'LightBlue', 'SkyBlue', 'LightSkyBlue', 'DeepSkyBlue', 'DodgerBlue',
          'CornflowerBlue', 'MediumSlateBlue', 'RoyalBlue', 'Blue', 'MediumBlue', 'DarkBlue', 'Navy', 'MidnightBlue',
          'Cornsilk', 'BlanchedAlmond', 'Bisque', 'NavajoWhite', 'Wheat', 'BurlyWood', 'Tan', 'RosyBrown',
          'SandyBrown', 'Goldenrod', 'DarkGoldenrod', 'Peru', 'Chocolate', 'SaddleBrown', 'Sienna', 'Brown',
          'Maroon', 'White', 'Snow', 'HoneyDew', 'MintCream', 'Azure', 'AliceBlue', 'GhostWhite', 'WhiteSmoke',
          'SeaShell', 'Beige', 'OldLace', 'FloralWhite', 'Ivory', 'AntiqueWhite', 'Linen', 'LavenderBlush',
          'MistyRose', 'Gainsboro', 'LightGray', 'Silver', 'DarkGray', 'Gray', 'DimGray', 'LightSlateGray',
          'SlateGray', 'DarkSlateGray', 'Black']


nodes = [
    {
        'data': {'id': id_name, 'label': term, 'group': group, 'gene': gene, 'size': size},
        'position': {'x': pos_x, 'y': pos_y},
        'classes': color
    }
    for id_name, term, group, gene, size, pos_x, pos_y, color in zip(df_node['ID'], df_node['Term'], df_node['GOGroups'], df_node['Associated Genes Found'], df_node['Term PValue'],
                                                  [random.randint(10, 100) for i in range(len(df_node))],
                                                  [random.randint(10, 100) for j in range(len(df_node))], df_node['Color'])
]

edges = [
    {'data': {'source': source, 'target': target, 'weight': score}}
    for source, target, score in zip(df_edge['source'], df_edge['target'], df_edge['KappaScore'])
]

elements = nodes + edges

app.layout = html.Div([
    html.H1('Cytoscape_network', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='dropdown-update-layout',
        value='cose',
        clearable=False,
        options=[
            {'label': name.capitalize(), 'value': name}
            for name in ['cose', 'random', 'grid', 'circle', 'concentric', 'breadthfirst']
        ],
        style={'width': '30%'}
    ),
    html.H2(id='cytoscape-mouseoverNodeData-output-term'),
    html.H4(id='cytoscape-mouseoverNodeData-output-gene'),
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        stylesheet=[
            {
                "selector": 'node',
                'style': {
                    'content': textwrap.fill('data(label)', width=10),
                    #    'data(label)',
                    'textwrap.fill': 'data(label)',
                    'opacity': 0.8,
                    'text-opacity': 1, # text 투명도 설정
                    'height': 10,
                    'width': 10,
                    'font-size': '5px'
                }
            },
            {"selector": '.IndianRed', 'style': {'background-color': 'IndianRed'}},
            {"selector": '.LightCoral', 'style': {'background-color': 'LightCoral'}},
            {"selector": '.Salmon', 'style': {'background-color': 'Salmon'}},
            {"selector": '.DarkSalmon', 'style': {'background-color': 'DarkSalmon'}},
            {"selector": '.LightSalmon', 'style': {'background-color': 'LightSalmon'}},
            {"selector": '.Crimson', 'style': {'background-color': 'Crimson'}},
            {"selector": '.Red', 'style': {'background-color': 'Red'}},
            {"selector": '.FireBrick', 'style': {'background-color': 'FireBrick'}},
            {"selector": '.DarkRed', 'style': {'background-color': 'DarkRed'}},
            {"selector": '.Pink', 'style': {'background-color': 'Pink'}},
            {"selector": '.LightPink', 'style': {'background-color': 'LightPink'}},
            {"selector": '.HotPink', 'style': {'background-color': 'HotPink'}},
            {"selector": '.DeepPink', 'style': {'background-color': 'DeepPink'}},
            {"selector": '.MediumVioletRed', 'style': {'background-color': 'MediumVioletRed'}},
            {"selector": '.PaleVioletRed', 'style': {'background-color': 'PaleVioletRed'}},
            {"selector": '.Coral', 'style': {'background-color': 'Coral'}},
            {"selector": '.Tomato', 'style': {'background-color': 'Tomato'}},
            {"selector": '.OrangeRed', 'style': {'background-color': 'OrangeRed'}},
            {"selector": '.DarkOrange', 'style': {'background-color': 'DarkOrange'}},
            {"selector": '.Orange', 'style': {'background-color': 'Orange'}},
            {"selector": '.Gold', 'style': {'background-color': 'Gold'}},
            {"selector": '.Yellow', 'style': {'background-color': 'Yellow'}},
            {"selector": '.LightYellow', 'style': {'background-color': 'LightYellow'}},
            {"selector": '.LightGoldenrodYellow', 'style': {'background-color': 'LightGoldenrodYellow'}},
            {"selector": '.Moccasin', 'style': {'background-color': 'Moccasin'}},
            {"selector": '.PaleGoldenrod', 'style': {'background-color': 'PaleGoldenrod'}},
            {"selector": '.DarkKhaki', 'style': {'background-color': 'DarkKhaki'}},
            {"selector": '.Thistle', 'style': {'background-color': 'Thistle'}},
            {"selector": '.Violet', 'style': {'background-color': 'Violet'}},
            {"selector": '.Fuchsia', 'style': {'background-color': 'Fuchsia'}},
            {"selector": '.MediumOrchid', 'style': {'background-color': 'MediumOrchid'}},
            {"selector": '.Navy', 'style': {'background-color': 'Navy'}},
            {"selector": '.DarkOrchid', 'style': {'background-color': 'DarkOrchid'}},
            {"selector": '.Indigo', 'style': {'background-color': 'Indigo'}},
            {"selector": '.MediumSlateBlue', 'style': {'background-color': 'MediumSlateBlue'}},
            {"selector": '.LawnGreen', 'style': {'background-color': 'LawnGreen'}},
            {"selector": '.LightGreen', 'style': {'background-color': 'LightGreen'}},
            {"selector": '.SeaGreen', 'style': {'background-color': 'SeaGreen'}},
            {"selector": '.YellowGreen', 'style': {'background-color': 'YellowGreen'}},
            {"selector": '.DarkOliveGreen', 'style': {'background-color': 'DarkOliveGreen'}},
            {"selector": '.MediumAquamarine', 'style': {'background-color': 'MediumAquamarine'}},
            {"selector": '.Aqua', 'style': {'background-color': 'Aqua'}},
            {"selector": '.Turquoise', 'style': {'background-color': 'Turquoise'}},
            {"selector": '.LightSteelBlue', 'style': {'background-color': 'LightSteelBlue'}},
            {"selector": '.PowderBlue', 'style': {'background-color': 'PowderBlue'}},
            {"selector": '.CornflowerBlue', 'style': {'background-color': 'CornflowerBlue'}},
        ],
        layout={'name': 'cose'},
        style={'height': '100vh',
               'width': '80%'},
    ),
    html.H4("Result table"),

    dash_table.DataTable(
        data=result.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in result.columns],
        style_table={'width': '90%'},
        style_cell={'textAlign': 'left', 'font_family': 'notosans', 'font-size': '13px'},
    ),
    dcc.Store(id='intermediated-value')
])

@app.callback(Output('cytoscape', 'layout'),
              Input('dropdown-update-layout', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('cytoscape-mouseoverNodeData-output-term', 'children'),
              Input('cytoscape', 'mouseoverNodeData'))
def displayTapNodeData(data):
    if data:
        return "GO term: " + str(data['label'])

@app.callback(Output('cytoscape-mouseoverNodeData-output-gene', 'children'),
              Input('cytoscape', 'mouseoverNodeData'))
def displayTapNodeData(data):
    if data:
        return "Associated gene: " + str(data['gene']) + ", Term p-value: " + str(data['size'])




if __name__ == '__main__':
    app.run_server(debug=True)
