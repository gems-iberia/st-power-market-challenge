#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:56:01 2023

@author: Nora Schürhoff
"""

import pandas as pd
import numpy as np
import zipfile
import os

# Inputs-----------------------------------------------------------------------
zip_path = 'data/all_trades_2022.zip'
extract_path = 'data/all_trades_2022'
file_name = 'all_2022.csv'


# Load DataFrame--------------------------------------------------------------
# Extract the data if still a zip
if not os.path.exists(extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

data = pd.read_csv(os.path.join(extract_path, file_name))


# 1. Give an overview of the top 10 agents in terms of traded volumes --------
# Calculate total energy traded for buys and sells separately
buy_volume = data.groupby(
    'buy_agent')['energy'].sum().reset_index(name='buy_volume')
sell_volume = data.groupby(
    'sell_agent')['energy'].sum().reset_index(name='sell_volume')

# Merge buy and sell volumes
agent_volumes = pd.merge(
    buy_volume, sell_volume, left_on='buy_agent', right_on='sell_agent', how='outer')

# Fill NaN values with 0 (for agents who only buy or only sell)
agent_volumes.fillna(0, inplace=True)

# Calculate total volume (buy + sell)
agent_volumes['total_volume'] = agent_volumes['buy_volume'] + \
    agent_volumes['sell_volume']

# Combine buy and sell_agent rows to don´t forget about only sellers
agent_volumes['agent'] = np.where(
    agent_volumes['buy_agent'] == 0, agent_volumes['sell_agent'], agent_volumes['buy_agent'])

agent_volumes = agent_volumes[[
    'agent', 'total_volume', 'buy_volume', 'sell_volume']]

# Sort by total volume and select the top 10
top_10_traders = agent_volumes.sort_values(
    by='total_volume', ascending=False).head(10)

print(top_10_traders)


# 2. Calculate an hourly Volume-Weighted Average Price (vwap)-----------------
# Calculate monetary value
data['monetary_value'] = data['energy'] * data['price']

# Calculate hourly vwap
hourly_vwap = data.groupby('contract_start').agg(sum_monetary_value=('monetary_value', 'sum'),
                                                 sum_energy=('energy', 'sum'))
hourly_vwap['vwap'] = hourly_vwap['sum_monetary_value'] / \
    hourly_vwap['sum_energy']

# Merge hourly vwap info back into data
data = pd.merge(data, hourly_vwap['vwap'], on='contract_start', how='left')


# 3. Score agents´ trades according to their spread with vwap. ------------------
# Add spread and score columns
data['spread'] = data['price'] - data['vwap']
data['score'] = data['spread'] / data['vwap']
data['weighted_score'] = data['score']*data['energy']

# Calculate total scores for buys and sells separately
buy_score = data.groupby('buy_agent')[
    'weighted_score'].sum().reset_index(name='buy_score')
sell_score = data.groupby('sell_agent')[
    'weighted_score'].sum().reset_index(name='sell_score')


# Merge buy and sell scores with agent metrics
temp = pd.merge(
    buy_score, sell_score, left_on='buy_agent', right_on='sell_agent', how='outer')

# Fill NaN values with 0 (for agents who only buy or only sell)
temp.fillna(0, inplace=True)

# Calculate total score. Negative buy and positive sell values favorable
temp['overall_score'] = temp['sell_score'] - temp['buy_score']

# Combine buy and sell_agent rows to don´t forget about only sellers
temp['agent'] = np.where(
    temp['buy_agent'] == 0, temp['sell_agent'], temp['buy_agent'])

agent_metrics = pd.merge(
    temp[['agent', 'buy_score', 'sell_score', 'overall_score']], agent_volumes, on='agent')

# Sort by total volume and select the top 10
top_10_traders = agent_metrics.sort_values(
    by='total_volume', ascending=False).head(10)


# Print or save the result
print(top_10_traders)
