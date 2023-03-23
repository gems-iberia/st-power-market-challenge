# st-power-market-challenge

## Welcome !

Below you can find the description of a analysis challenge that we ask people with coding/analysis skills to perform when applying for a job in our team.

The goal of this coding challenge is to provide the applicant some insight into the business we're in and as such provide the applicant an indication about the challenges she/he will be confronted with. 

Time is scarce, we know. Therefore we ask you not to spend more than 4 hours on this challenge. . We know it is not possible to deliver a finished implementation of the challenge in only four hours. Even though your submission will not be complete, it will provide us plenty of information and topics to discuss later on during the talks.

This coding-challenge is part of a formal process and is used in collaboration with the recruiting companies we work with.  Submitting a pull-request will not automatically trigger the recruitement process.
## Who are we 

We are the Short-Term Optimisation team of BP Iberia within [GEM](https://gems.engie.com/).

[GEM](https://gems.engie.com/), which stands for 'Global Energy Management', is the energy management arm of [ENGIE](https://www.engie.com/), one of the largest global energy players, 
with access to local markets all over the world.  

BP Iberia covers the GEMS activities of Spain & Portugal, consisting of around 75 people with experience in energy markets, IT and modeling. In smaller teams consisting of a mix of people with different experiences, we are active on the [day-ahead](https://en.wikipedia.org/wiki/European_Power_Exchange#Day-ahead_markets) market, [intraday markets](https://en.wikipedia.org/wiki/European_Power_Exchange#Intraday_markets) and [collaborate with the TSO to balance the grid continuously](https://en.wikipedia.org/wiki/Transmission_system_operator#Electricity_market_operations).

## The challenge

### In short
Analyse the provided trading data in order to get some insights in the Iberian continuous intraday power market. 

### More in detail
In order to build some insight, we propose you calculate and present below metrics. You should at least use one month of data from the dataset provided. 
Feel free to use the complete dataset. 

#### Data
The provided dataset is based on publicly available trade data published by [OMIE](https://www.omie.es/es/file-access-list). 

#### Format
Coding and presentation can be done in a Jupiter Notebook which should be uploaded in a new branch to this repository. 
Alternatively README.md could be used to build a report if you prefer to code in regular .py files.

#### Proposed metrics
1. Give an overview of the top 10 agents in terms of traded volumes
2. Calculate an hourly Volume-Weighted Average Price (vwap)
```math
vwap = \frac{ \sum_{n} (P_i \cdot V_i) } {\sum_{n} V_i}
```
where `P` is the trades price and `V` the volume of every one of the n trades within the hour. 
3. Score agents' trades according to their spread with vwap. Context: someone who would be able to structurally sell above vwap, or buy below, would be doing a good job.  


### Want more challenge?

Having fun with this challenge and want to make it more realistic? Feel free to come up with your own metrics of visuals to build further insights 


## More info

For more info on energy management, check out:

 - [OMIE - Mercado de electricidad](https://www.omie.es/es/mercado-de-electricidad)


## FAQ

##### Can an existing solver be used to calculate the unit-commitment
Implementations should not rely on an external solver and thus contain an algorithm written from scratch (clarified in the text as of version v1.1.0)
