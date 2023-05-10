import plotly.io as pio
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()

pio.write_html(fig, file="index.html", auto_open=True)
