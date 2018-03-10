import json
import os
from parser import *

rootdir = '/Users/scott/Downloads/bills/s'
count=1
for subdir, dirs, files in os.walk(rootdir):
	if (count==1):
		count+=1
	else:
		data = json.load(open(subdir+'/data.json'))
		name=data["bill_id"]
		lawDict=data["history"]
		if lawDict.get("enacted"):
			if lawDict.get("vetoed"):
				makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=True)
			else:
				makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isSigned=True)
		else:
			lawKeys = lawDict.keys()
			if (not "senate_passage_result" in lawKeys) and (not "house_passage_result" in lawKeys):
				makeLispPhrase(name)
			if "house_passage_result" in lawKeys:
				if (not lawDict.get("house_passage_result")):
					makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=False)
			if "senate_passage_result"in lawKeys:
				if (not lawDict.get("senate_passage_result")):
					makeLispPhrase(name,beenVotedOnSenate=True, passedSenate=False)
			if "house_passage_result" in lawKeys and (not "senate_passage_result"in lawKeys):
				makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True)
			if "senate_passage_result" in lawKeys and (not "house_passage_result"in lawKeys):
				makeLispPhrase(name,beenVotedOnSenate=True, passedSenate=True)
			if "senate_passage_result" in lawKeys and "house_passage_result" in lawKeys:
				if lawDict.get("vetoed"):
					if lawDict.get("enacted"):
						makeLispPhrase("Bill25",beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=True)
					else:
						makeLispPhrase("Bill25",beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=False)
				else:
					makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True)		
			
		



rootdir = '/Users/scott/Downloads/bills/hr'
count=1
for subdir, dirs, files in os.walk(rootdir):
	if (count==1):
		count+=1
	else:
		data= json.load(open(subdir+'/data.json'))
		name=data["bill_id"]
		lawDict=data["history"]
		if lawDict.get("enacted"):
			if lawDict.get("vetoed"):
				makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=True)
			else:
				makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isSigned=True)
		else:
			lawKeys = lawDict.keys()
			if (not "senate_passage_result" in lawKeys) and (not "house_passage_result" in lawKeys):
				makeLispPhrase(name)
			if "house_passage_result" in lawKeys:
				if (not lawDict.get("house_passage_result")):
					makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=False)
			if "senate_passage_result"in lawKeys:
				if (not lawDict.get("senate_passage_result")):
					makeLispPhrase(name,beenVotedOnSenate=True, passedSenate=False)
			if "house_passage_result" in lawKeys and (not "senate_passage_result"in lawKeys):
				makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True)
			if "senate_passage_result" in lawKeys and (not "house_passage_result"in lawKeys):
				makeLispPhrase(name,beenVotedOnSenate=True, passedSenate=True)
			if "senate_passage_result" in lawKeys and "house_passage_result" in lawKeys:
				if lawDict.get("vetoed"):
					if lawDict.get("enacted"):
						makeLispPhrase("Bill25",beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=True)
					else:
						makeLispPhrase("Bill25",beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=False)
				else:
					makeLispPhrase(name,beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True)		
			
		
	    