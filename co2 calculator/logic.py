"""
 Logic 
 """

def modified_rate_worst(initial_rate, season,seasons):

    rate= (initial_rate / (seasons[season][0]))
    return rate

def modified_rate_best(initial_rate, season, seasons):

    rate= (initial_rate / (seasons[season][1]))
    return rate

def set_season(month,day,time):

    season= "low"
    months=[1]
    days=["monday","friday","saturday","sunday"]
    times=["morning","night"]

    if month in months:
        if day in days:
            if time in times:
               season= "high"

        else:
            season= "medium"
    return season


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

def virtual_calculator(people,continents,continent,duration,energy):

    

    Gas=people*duration*continents[continent][0]*energy["Gas"]
    Hydroelectric=people*duration*continents[continent][1]*energy["Hydroelectric"]
    Nuclear=people*duration*continents[continent][2]*energy["Nuclear"]
    Eolic=people*duration*continents[continent][3]*energy["Eolic"]
    Solar=people*duration*continents[continent][4]*energy["Solar"]
    Carbon=people*duration*continents[continent][5]*energy["Carbon"]

    total= Gas+Hydroelectric+Nuclear+Eolic+Solar+Carbon

    return total