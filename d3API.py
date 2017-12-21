#!/bin/python

#Script to talk to the d3 api

#Import requirements
import requests
import argparse
import pprint
import json
from prettytable import PrettyTable

apikey="<insert here>"
profileEndpoint="https://eu.api.battle.net/d3/profile/<insert here>"

def accountInfo(myAPIKey,myEndPoint): # Funciton to pull general account wide stats

  #Build URL to list account details
  targetURL = myEndPoint+"/?locale=en_GB&apiKey="+myAPIKey

  #Make request
  r = requests.get(targetURL)

  #Push resultes in to a json object and work out size of array
  results_json = r.json()

  #Define table structure

  tablea = PrettyTable(['Key', 'Value'])
  
  tablea.add_row(['BattleTag',results_json['battleTag']])
  tablea.add_row(['Paragon',results_json['paragonLevel']])
  tablea.add_row(['Hardcore paragon',results_json['paragonLevelHardcore']])
  tablea.add_row(['Seasonal paragon',results_json['paragonLevelSeason']])
  tablea.add_row(['Hardcore seasonal paragon',results_json['paragonLevelSeasonHardcore']])
  tablea.add_row(['Highest hardcore level',results_json['highestHardcoreLevel']])
  tablea.add_row(['Monster kills',results_json['kills']['monsters']])
  tablea.add_row(['Elite kills',results_json['kills']['elites']])

  print tablea

  return

def listCharacters(myAPIKey,myEndPoint): # Function to pull a list of characters

  #Build URL to list account details
  targetURL = myEndPoint+"/?locale=en_GB&apiKey="+myAPIKey

  #Make request
  r = requests.get(targetURL)

  #Push resultes in to a json object and work out size of array
  results_json = r.json()
  total_chars = len(results_json['heroes'][0]['name']) -1

  #Define table structure
  t = PrettyTable(['id', 'Character', 'Class', 'Level', 'Hardcore', 'Seasonal'])

  #Loop through each json object, pull out the game name and playtime and load it into table rows
  for i in range(0,total_chars):
    t.add_row([results_json['heroes'][i]['id'],results_json['heroes'][i]['name'],results_json['heroes'][i]['class'],results_json['heroes'][i]['level'],results_json['heroes'][i]['hardcore'],results_json['heroes'][i]['seasonal']])

  #Print table
  print t

  return

def characterDetail(myAPIKey,myEndPoint,myHero): # Function to give individual character stats

  #Build URL to list character details
  targetURL = myEndPoint+"/hero/"+myHero+"?locale=en_GB&apiKey="+myAPIKey

  #Make request
  r = requests.get(targetURL)

  #Push resultes in to a json object and work out size of array
  results_json = r.json()

  #Define stats table
  statst = PrettyTable(['Key', 'Value'])
  
  statst.add_row(['Name',results_json['name']])
  statst.add_row(['Class',results_json['class']])
  statst.add_row(['Level',results_json['level']])
  statst.add_row(['Str',results_json['stats']['strength']])
  statst.add_row(['Dex',results_json['stats']['dexterity']])
  statst.add_row(['Int',results_json['stats']['intelligence']])
  statst.add_row(['Vit',results_json['stats']['vitality']])
  statst.add_row(['Damage',results_json['stats']['damage']])
  statst.add_row(['CHC',results_json['stats']['critChance']])
  statst.add_row(['CHD',results_json['stats']['critDamage']])
  statst.add_row(['IAS',results_json['stats']['attackSpeed']])
  statst.add_row(['Toughness',results_json['stats']['toughness']])
  statst.add_row(['Armour',results_json['stats']['armor']])

  print statst

  #Define build table
  buildt = PrettyTable(['Key', 'Skill', 'Rune'])
  
  LMB=results_json['skills']['active'][0]['skill']['name']
  buildt.add_row(['LMB',results_json['skills']['active'][0]['skill']['name'],results_json['skills']['active'][0]['rune']['name']])
  buildt.add_row(['RMB',results_json['skills']['active'][1]['skill']['name'],results_json['skills']['active'][1]['rune']['name']])
  buildt.add_row(['1',results_json['skills']['active'][2]['skill']['name'],results_json['skills']['active'][2]['rune']['name']])
  buildt.add_row(['2',results_json['skills']['active'][3]['skill']['name'],results_json['skills']['active'][3]['rune']['name']])
  buildt.add_row(['3',results_json['skills']['active'][4]['skill']['name'],results_json['skills']['active'][4]['rune']['name']])
  buildt.add_row(['4',results_json['skills']['active'][5]['skill']['name'],results_json['skills']['active'][5]['rune']['name']])
  buildt.add_row(['P1',results_json['skills']['passive'][0]['skill']['name'],'N/A']) 
  buildt.add_row(['P2',results_json['skills']['passive'][1]['skill']['name'],'N/A']) 
  buildt.add_row(['P3',results_json['skills']['passive'][2]['skill']['name'],'N/A']) 
  buildt.add_row(['P4',results_json['skills']['passive'][3]['skill']['name'],'N/A']) 
  print buildt

  return

#Setup argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--account", help="account stats", action='store_true', required=False)
parser.add_argument("-l", "--listall", help="list characters", action='store_true', required=False)
parser.add_argument("-c", "--character", help="character detail for <heroID>", action='store', required=False)
args = parser.parse_args()

#Main code
if args.listall:
  listCharacters(apikey,profileEndpoint)
elif args.character:
  characterDetail(apikey,profileEndpoint,args.character)
elif args.account:
  accountInfo(apikey,profileEndpoint) 
