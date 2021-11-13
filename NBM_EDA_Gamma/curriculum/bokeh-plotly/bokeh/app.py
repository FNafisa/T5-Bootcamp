from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np
app = Flask('using bokeh')


@app.route('/')
def index():
    measured = np.random.normal(0, 1, 1000)
    hist, edges = np.histogram(measured, density=True, bins=50)

    fig = figure(title='Plot of normal distribution',
                 background_fill_color="#E8DDCB", plot_width=600,
                 plot_height=400)
    fig.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
             fill_color='#ACACAC', line_color='#888888')
    javascript, div = components(fig)
    return render_template('index.html', javascript=javascript, div=div)


app.run(port=5000, debug=True)
