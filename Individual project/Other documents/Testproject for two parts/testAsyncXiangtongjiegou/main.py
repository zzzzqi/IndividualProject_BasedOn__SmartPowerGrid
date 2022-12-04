## Name: web_dashboard.py
## Date: 23 Aug 2022
## By: Group F Toumetis - MSc CS Final Project - University of Bristol

import asyncio
import panel as pn
import holoviews as hv
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource


# Enable Bokeh and Panel
hv.extension('bokeh')
pn.extension('vega', 'tabulator')

## ========================================================
## Build the layout of the dashboard
# Set the dashboard template
app = pn.template.MaterialTemplate(title='Smart Power Grids Dashboard')

button = pn.widgets.Button(name='Click me!')

p = figure(width=500, height=300)
cds = ColumnDataSource(data={'x': [0], 'y': [0]})
p.line(x='x', y='y', source=cds)
pane = pn.pane.Bokeh(p)


@pn.io.with_lock
async def stream(event):
    await asyncio.sleep(1)
    x, y = cds.data['x'][-1], cds.data['y'][-1]
    cds.stream({'x': list(range(x + 1, x + 6)), 'y': y + np.random.randn(5).cumsum()})
    pane.param.trigger('object')


# Equivalent to `.on_click` but shown
button.param.watch(stream, 'clicks')


app.main.append(pn.Row(button, pane))

app.servable()

