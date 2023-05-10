import plotly.io as pio
import plotly.express as px

pio.renderers.default = "notebook"
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()
