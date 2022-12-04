## Name: web_dashboard.py
## Date: 23 Aug 2022
## By: Group F Toumetis - MSc CS Final Project - University of Bristol

import os
import asyncio
import panel as pn
import holoviews as hv
import threading
import time
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# Enable Bokeh and Panel
hv.extension('bokeh')
pn.extension('vega', 'tabulator', nthreads=2)

## ========================================================
## Build the layout of the dashboard
# Set the dashboard template
app = pn.template.MaterialTemplate(title='Smart Power Grids Dashboard')


# def display_data_exploration_pane(var1):
#     data_exploration_pane = pn.Column(pn.widgets.TextInput(name='Text 11111', placeholder='Enter a string here...'))
#     button = pn.widgets.Button(name='Click me!')
#     data_exploration_pane.append(button)
#
#     @pn.depends(button)
#     def test_append_alert(var):
#         if button.clicks >= 3:
#             return pn.pane.Alert('## Alert\nThis is a warning111111!')
#         else:
#             return pn.pane.Alert('## Alert\nThis is a warning2222222!')
#
#     data_exploration_pane.append(test_append_alert)
#
#     return data_exploration_pane
#
#
# test_tab = pn.Tabs(
#     ("Data-exploration pane", display_data_exploration_pane(111)),
#     ("Selected event", pn.widgets.TextInput(name='Text 222222', placeholder='Enter a string here...'))
# )






# c = threading.Condition()
#
# button = pn.widgets.Button(name='Click to launch')
# text = pn.widgets.StaticText()
#
# queue = []
#
#
# def callback():
#     global queue
#     while True:
#         c.acquire()
#         for i, q in enumerate(queue):
#             text.value = f'Processing item {i + 1} of {len(queue)} items in queue.'
#             time.sleep(2)
#         queue.clear()
#         text.value = "Queue empty"
#         c.release()
#         time.sleep(1)
#
#
# thread = threading.Thread(target=callback)
# thread.start()
#
# def on_click(event):
#     print(event)
#     queue.append(event)
#
# button.on_click(on_click)
#
# app.main.append(pn.Row(button, text))



print("os.cpu_count() is :")
print(os.cpu_count())

def button_click(event):
    print('Button clicked for the {event.new}th time.')
    time.sleep(2)  # Simulate long running operation
    print('Finished processing {event.new}th click.')


button = pn.widgets.Button(name='Click me!')

button.on_click(button_click)


app.main.append(pn.Row(button))
app.servable()
