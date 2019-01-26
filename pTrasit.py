import json
import csv
import math
from collections import defaultdict
#!/usr/bin/python3

import psycopg2
import configparser

#read config file
Config = configparser.ConfigParser()
Config.read("../Relevance/config.ini")

#get database info from config file
hostname = Config.get("nucleus","hostname")
username = Config.get("nucleus","username")
password = Config.get("nucleus","password")
database = Config.get("nucleus","database")

hostname1 = Config.get("deepend","hostname")
username1 = Config.get("deepend","username")
password1 = Config.get("deepend","password")
database1 = Config.get("deepend","database")

con = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
print("connection success")
cur=con.cursor()
con1 = psycopg2.connect(host=hostname1, user=username1, password=password1, dbname=database1)
cur1 = con1.cursor()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def poisonCalculate(k):
      constant=0.13533528
      pinit=(constant*math.pow(2,k))/factorial(k)
      return pinit
def commitToDatabase(competenciesJson, resource):


def pTransit(resource):
    #Let c1 be the competency r1 be the resource.
    competencies = #all competencies related to r1.
    competenciesJson = {};
    for c1 in competencies:
        assesments = cur1.query(#all assesments in in competency c1)
        ptrans = 0;
        for a in assesments:
            k = cur.query(#number of students who completed in 1st attempt)
            kTotal = cur.query(#total studnets who attemptted a1 and consumed r1)
            ptrans /= len(assesments);
            ptrans += k/kTotal
        competenciesJson[c1] = ptrans
    commitToDatabase(competenciesJson, resource)
if __name__ == '__main__':
        #print(values)
con.close()
con1.close()
