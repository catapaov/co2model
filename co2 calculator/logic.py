"""
 Logic 
 """

"""
Change the percentage of co2 emitted depending on the season
 """

def modified_rate_worst(initial_rate, season,seasons):

    rate= (initial_rate / (seasons[season][0]))
    return rate

def modified_rate_best(initial_rate, season, seasons):

    rate= (initial_rate / (seasons[season][1]))
    return rate
  
"""
Define the season according to the month, day and time of the event
 """

def set_season(month,day,time):

    season= "low"
    months=["march","june","july","august","december","january"]
    days=["monday","friday","saturday","sunday"]
    times=["morning","night"]

    if month in months:
        if day in days:
            if time in times:
               season= "high"

        else:
            season= "medium"
    return season
"""
Calculate the total kg of CO2 that would lead to the event being
carried out in person. Two scenarios are offered, one with 
underestimates and the other with overestimates. For the calculation
, the size of the event is taken into account, whether it is national,
international, regional or local, how many people on average will 
attend and the date on which the event will take place. The season 
is used to determine how full the means of transport in which people
move will be to estimate the amount of co2 per passenger, the type of
event is used to estimate the distances that attendees would have to 
travel and the possible means of transportation. transport that you
would use because each one generates a different amount of co2
 """

def transport_calculator(people,continents,season, seasons,continent, type, types,transports):

    total={ 
    "best":0,
    "worst":0,

    }
    airplane= 0
    train=0
    bus=0

    if  type== "large_international":

        airplane= people*transports["airplane"]*types[type]*2

    elif type== "regional":

        airplane= (people*continents[continent][0])*transports["airplane"]*types[type]*2
        train=(people*continents[continent][1])*transports["train"]*types[type]*2

    elif type== "national":
        airplane= people*transports["airplane"]*types[type]*2*0.1
        train=people*transports["train"]*types[type]*2*0.45
        bus=people*transports["bus"]*types[type]*2*0.45

    else:

        bus=people*transports["bus"]*types[type]*2*0.8

    total["best"]= (modified_rate_best(airplane, season,seasons))+(modified_rate_best(train, season,seasons))+(modified_rate_best(bus, season,seasons))
    total["worst"]=(modified_rate_worst(airplane, season,seasons))+(modified_rate_worst(train, season,seasons))+(modified_rate_worst(bus, season,seasons))



    return total
   
  """
Calculate the total kg of CO2 that would lead to the event being
carried out in virtually. Take into account the duration and the
places from where people would connect to the event, since in each 
region the percentages of use of certain energy sources vary and 
I get the amount of co2 emitted
 """

def virtual_calculator(people,continents,continent,duration,energy):

    

    Gas=people*duration*continents[continent][0]*energy["Gas"]
    Hydroelectric=people*duration*continents[continent][1]*energy["Hydroelectric"]
    Nuclear=people*duration*continents[continent][2]*energy["Nuclear"]
    Eolic=people*duration*continents[continent][3]*energy["Eolic"]
    Solar=people*duration*continents[continent][4]*energy["Solar"]
    Carbon=people*duration*continents[continent][5]*energy["Carbon"]

    total= Gas+Hydroelectric+Nuclear+Eolic+Solar+Carbon

    return total
