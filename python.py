import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=[[3, 18, 0, 9, 24, 23, 22], [76, 32, 8, 49, 4, 3, 29], [3, 37, 110, 87, 83, 125, 40],
                      [1, 40, 15, 28, 12, 12, 47], [11, 68, 7, 11, 11, 10, 12], [29, 32, 1, 18, 7, 6, 55],
                      [137, 24, 9, 9, 11, 7, 12], [15, 53, 1, 4, 13, 21, 10], [0, 0, 42, 14, 12, 18, 0],
                      [43, 0, 4, 7, 12, 27, 12], [7, 45, 14, 45, 13, 13, 33], [0, 3, 31, 5, 10, 8, 1],
                      [2, 2, 68, 15, 18, 25, 0], [1, 4, 38, 23, 12, 17, 19]],
                   x=['Country', 'Dance/EDM', 'Hip Hop', 'Indie/Alternative', 'Pop', 'RnB', 'Rock'],
                   y=['Hearts', 'Plants', 'Faces', 'Hands/Arms', 'Food/Drinks', 'Musical', 'Animals', 'Celebration',
                   'Fire', 'Wearables', 'Weather/Sky', 'Sports', 'Money', 'Symbols'],
                   colorscale= 'Rainbow')
data=[trace]

py.image.save_as({'data':data}, 'nameofyourgraph', format='png')