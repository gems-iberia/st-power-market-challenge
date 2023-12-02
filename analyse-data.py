#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:56:01 2023

@author: Nora Schürhoff
"""

import pandas as pd

# Inputs-----------------------------------------------------------------------
path = 'data/all_2022.csv'


# Load DataFrame--------------------------------------------------------------
data = pd.read_csv(path)


# Analysis with small data-set
#data = data.head(100)

# 1. Give an overview of the top 10 agents in terms of traded volumes --------
# Calculate total energy traded for buys and sells separately
buy_volume = data.groupby(
    'buy_agent')['energy'].sum().reset_index(name='buy_volume')
sell_volume = data.groupby(
    'sell_agent')['energy'].sum().reset_index(name='sell_volume')

# Merge buy and sell volumes
combined_volumes = pd.merge(
    buy_volume, sell_volume, left_on='buy_agent', right_on='sell_agent', how='outer')

# Fill NaN values with 0 (for agents who only buy or only sell)
combined_volumes.fillna(0, inplace=True)

# Calculate total volume (buy + sell)
combined_volumes['total_volume'] = combined_volumes['buy_volume'] + \
    combined_volumes['sell_volume']

# Rename columns for clarity and drop columns not needed
combined_volumes.rename(columns={'buy_agent': 'agent'}, inplace=True)

combined_volumes = combined_volumes[[
    'agent', 'total_volume', 'buy_volume', 'sell_volume']]

# Sort by total volume and select the top 10
top_10_traders = combined_volumes.sort_values(
    by='total_volume', ascending=False).head(10)


print(top_10_traders)
