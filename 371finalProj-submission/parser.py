def makeLispPhrase(billName, beenVotedOnHouse=False, beenVotedOnSenate=False, passedHouse=False, passedSenate=False, isSigned=False, isVetoed=False, hadOverturn=False, isOverturned=False):
	lispParse=[]
	lispParse.append("(isa "+billName+" Bill-Idea)\n")
	lispParse.append("(writtenSponsored "+billName+")\n")
	count=0
	if beenVotedOnHouse: 
		lispParse.append("(houseVoteResult "+ billName+ " "+str(passedHouse) + ")\n")
		count+=1
	if beenVotedOnSenate: 
		lispParse.append("(houseVoteResult "+billName+" "+str(passedSenate)+")\n")
		count+=1
	if isSigned:
		lispParse.append("(presidentSigned " +billName+")")
		count+=1
	if isVetoed:
		lispParse.append("(presidentVeto " +billName+")")
		count+=1
	if hadOverturn:
		lispParse.append("(vetoOverTurn "+billName+" "+ str(isOverturned)+")\n")
	# for item in lispParse:
	# 	print(item)
	# print("\n")
	lispParse = '\n'.join(lispParse)
	return lispParse



# print(makeLispPhrase("Bill20"))
# makeLispPhrase("Bill21",beenVotedOnHouse=True, passedHouse=False)
# makeLispPhrase("Bill22" ,beenVotedOnSenate=True, passedSenate=False)
# makeLispPhrase("Bill23",beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=False)
# makeLispPhrase("Bill24",beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isSigned=True,)
# makeLispPhrase("Bill25",beenVotedOnHouse=True, passedHouse=True,beenVotedOnSenate=True, passedSenate=True,isVetoed=True,hadOverturn=True, isOverturned=True)



