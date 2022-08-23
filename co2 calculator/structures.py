"""
Base structures
 """

 """
The season refers to the time of year in which the event takes place, since when calculating co2, 
the total fuel burned is divided among all the passengers on a flight. This is usually done with 
an approximate, however, with the season the This calculation is a little closer to reality since
planes and trains will not always be 100% full and therefore the amount of co2 that is "assigned"
to each person will not be the same. the dates and percentages were determined by information that
I consulted on the months, days and hours in which these conveyances have more passengers
 """
 
seasons={ 
    "high":(0.9,1), 
    "medium":(0.6,0.9),#he value of the season is a tuple that #indicates the percentage of passengers in the worst and best cases
    "low":(0.3,0.6),

    }

 """
Here we store the value of the average amount of co2 (in g) associated with the burning of fuel for each conveyance,
these values were consulted in various articles and studies on the amount of co2 released by each transport. 
The ideal would be not to arbitrarily fill the values but that they were updated
through collaborations with transport companies and people who carry out research on the matter

 """
transport={ 
    "airplane":310.0,
    "train":87.09,
    "bus":107.25,

    }

 """
Depending on the type of event, an average distance is assigned that each person 
attending the event would travel. This is a fairly broad approximation since not
everyone will travel the same distance, however, making this calculation accurately 
would make the use of the application more complicated by the user since the user would
have to enter more data that may not know beforehand and that would take 
more time to find out

 """
types={ 
    "large_international":7000,# An event attended by people from all over the world
    "national":1500,
    "regional":3000,#Event attended by people from the same continent
    "local":800,#Event attended by people from the same city, department or state
    }

 """
As there are several options available for transportation in the model,
two conveyances were considered: plane and train, and since the percentage
of co2 that these two emit is different, I considered it appropriate to take
into account the percentage of people who usually use one or the other 
conveyances to that this trend is reflected in the calculation

 """

continents_t={ 
    "Africa":(0.0,0.0),# tuples with the percentage of people who usually use a plane to
    "America":(0.8,0.2),#traveling long distances vs. the percentage of people
    "Asia":(0.0,0.0),#who does it by train respectively
    "Europe":(0.6,0.4),
    "Oceania":(0.0,0.0),
    }

 """
 As there are several options available between energy sources in the model,
 the percentages of use of certain types of energy sources are considered to
 enrich the calculation of CO2 from remote meetings, the values are tuples 
 with the percentages of use of: gas, hydropower, nuclear power, wind power, 
 solar power and coal as primary energy sources respectively

 """
continents_v={ 
    "Africa":(0.4,0.17,0.001,0.002,0.002,0.31),
    "America":(0.32,0.02,0.009,0.032,0.014,0.11),
    "Asia":(0.17,0.12,0.0047,0.005,0.003,0.51),
    "Europe":(0.25,0.17,0.23,0.1,0.03,0.15),
    "Oceania":(0.16,0.13,0.0,0.009,0.1,0.45),
    }
 """
Here the values of co2 (in kg) per kWh associated with each energy source are stored 
 """
energy={ 
    "Gas":0.185,
    "Hydroelectric":0.025,
    "Nuclear":0.0012,
    "Eolic":0.011,
    "Solar":0.04,
    "Coal":3.5,
    }
