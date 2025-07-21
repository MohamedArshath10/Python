import plotly.express as px
data = {'x' : [1, 2, 3], 'y' : [2, 4, 6]}
fig = px.line(data, x="x", y="y", title='Interactive line plot')
fig.show()

# HeatMap in plotly
import numpy as np
z = np.array([[1,20,30], [20,1,6], [30, 60, 1]])
fig = px.imshow(z, text_auto=True, color_continuous_scale='viridis')
fig.update_layout(title = "Heat Map")
fig.show()