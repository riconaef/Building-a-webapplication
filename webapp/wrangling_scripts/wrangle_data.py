import pandas as pd
import datetime as dt
import plotly.graph_objs as go

# Read in data, wrangle it and prepare the plotly visualizations.

df_price = pd.read_csv('data/market-price')
df_amount = pd.read_csv('data/total-bitcoins')
df_allcc = pd.read_csv('data/allcc')

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart to plot the bitcoin price
    # as a line chart
    
    graph_one = [] 
    
    x = []
    y = df_price['market-price']

    for i in range(len(df_price)):
        x.append(dt.datetime.strptime(df_price['Timestamp'][i], '%Y-%m-%d %H:%M:%S'))
    
    graph_one.append(
      go.Scatter(
      x = x,
      y = y,
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Bitcoin Price',
                xaxis = dict(title = 'time [year]'),
                yaxis = dict(title = 'price [$]')
                )

# second chart to plot the bitcoin price on a logarithmic scale  
    graph_two = []

    x = []
    y = df_price['market-price']

    for i in range(len(df_price)):
        x.append(dt.datetime.strptime(df_price['Timestamp'][i], '%Y-%m-%d %H:%M:%S'))
    
    graph_two.append(
      go.Scatter(
      x = x,
      y = y,
      mode = 'lines'
    )
  )
    
    layout_two = dict(title = 'Bitcoin price on a logarithmic price scale',
                xaxis = dict(title = 'time [year]',),
                yaxis = dict(title = 'price [$]', type= 'log'),
                )
    
# third chart plots the total mined bitcoins
    graph_three = []
    x = []
    y = df_amount['total-bitcoins']

    for i in range(len(df_amount)):
        x.append(dt.datetime.strptime(df_amount['Timestamp'][i], '%Y-%m-%d %H:%M:%S'))
    
    graph_three.append(
      go.Scatter(
      x = x,
      y = y,
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Bitcoins mined',
                xaxis = dict(title = 'time [year]'),
                yaxis = dict(title = 'Total amount of bitcoins mined')
                       )
    
# fourth chart shows the market capitalization of bitcoin and other crypto currencies
    graph_four = []
    
    x = df_allcc['name'][:10]
    y = df_allcc['market_cap'][:10]
    
    graph_four.append(
      go.Bar(
      x = x,
      y = y,
      )
    )

    layout_four = dict(title = 'Market capitalization of different crypto currencies',
                xaxis = dict(title = ''),
                yaxis = dict(title = 'Total market capitalization in billions'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
