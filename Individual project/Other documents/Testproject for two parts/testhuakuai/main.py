## Name: web_dashboard.py
## Date: 23 Aug 2022
## By: Group F Toumetis - MSc CS Final Project - University of Bristol

import asyncio
import panel as pn
import holoviews as hv

# Enable Bokeh and Panel
hv.extension('bokeh')
pn.extension('vega', 'tabulator')

## ========================================================
## Build the layout of the dashboard
# Set the dashboard template
app = pn.template.MaterialTemplate(title='Smart Power Grids Dashboard')
# Set the dashboard's instructions
# test_widget_slider = pn.widgets.IntSlider(
#     name="test: ",
#     value=15,
#     start=0,
#     end=200,
#     step=1,
# )
#
# pn.config.throttled = True
#
# @pn.depends(test_widget_slider)
# def testfuc(test_widget_slider_var):
#     return test_widget_slider_var + 5
#
# test_page = pn.Column(
#         test_widget_slider,
#         testfuc
# )

button = pn.widgets.Button(name='Click me!')
text = pn.widgets.StaticText()


async def run_async(event):
    text.value = f'Running {event.new}'
    await asyncio.sleep(2)
    text.value = f'Finished {event.new}'


button.on_click(run_async)

app.main.append(pn.Row(button, text))

app.servable()
