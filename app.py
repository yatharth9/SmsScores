#Fetch pycricbuzz via pip
from pycricbuzz import Cricbuzz

import json

#For System Arguments
import sys

#For sending the SMS
import lib.sms as SMS

#Fetches the commentary for matchid(mid) via the cricbuzz object
def commentary(mid):
    c = Cricbuzz()
    comm = c.commentary(mid)
    comms = list(comm.values())[0]
    latest_comm = comms[0]
    return str(latest_comm)
    #print(latest_comm)
    #print (comm.values()[0].keys()[0])
    
    #Remove the next line from comments to print entire commentary 
    #print(json.dumps(comm, indent=4, sort_keys=True))

#Fetches the live score for matchid(mid) via the cricbuzz object
def live_score(mid):
    c = Cricbuzz()
    lscore = c.livescore(mid)
    l_score = json.dumps(lscore, indent=4, sort_keys=True)
    #print(l_score)
    return l_score

def beautify(initial):
    s1 = initial.replace('{',' ')
    s2 = s1.replace('}',' ')
    s3 = s2.replace('[',' ')
    s4 = s3.replace(']',' ')
    return(s4)
    

#This is calling the commentary and live score via match id passed as command line arguement
def main():
    id = sys.argv[1]
    #commentary("30540")
    #live_score("30540")
    lcom = commentary(id)
    ls = live_score(id)
    message = lcom + ls
    s_message = beautify(message)
    #print(s_message)
    SMS.send(s_message)

# __name__ 
if __name__=="__main__": 
    main()