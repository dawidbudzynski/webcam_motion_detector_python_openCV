from math import pi

from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure, show, output_file

from motion_detector import df

try:
    df['Start_string'] = df['Start'].dt.strftime('%H:%M:%S')
    df['End_string'] = df['End'].dt.strftime('%H:%M:%S')
    print(df['Start_string'])
except AttributeError:
    print('No motion recorded')
    quit()

cds = ColumnDataSource(df)

p = figure(height=200, width=1000,
           sizing_mode='scale_width', title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1
p.yaxis.visible = False
p.xaxis.formatter = DatetimeTickFormatter(milliseconds=["%H:%M:%S"],
                                          seconds=["%H:%M:%S"],
                                          minutes=["%H:%M:%S"],
                                          hours=["%H:%M:%S"])
p.xaxis.major_label_orientation = pi / 4

hover = HoverTool(tooltips=[('Start:', '@Start_string'), ('End:', '@End_string')])
p.add_tools(hover)

q = p.quad(left='Start', right='End', bottom=0, top=1, color='deepskyblue', source=cds)

output_file('Graph.html')
show(p)
