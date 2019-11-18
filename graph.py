import sqlite3
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('weather.db')

def graph_data():
    c = conn.cursor()
    c.execute('SELECT created_at, raw_value FROM reading')
    data = c.fetchall()

    dates = []
    values = []
    
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values,'-')
    plt.show()
    c.close

graph_data()
conn.close()
