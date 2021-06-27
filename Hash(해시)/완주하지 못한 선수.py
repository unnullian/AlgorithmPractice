def solution(participant, completion):
    answer = ''
    totalParticipantHash = 0
    totalCompletionHash = 0
    dicParticipant = {}

    for parti in participant :
        hashValue = hash(parti)
        totalParticipantHash += hashValue
        dicParticipant[hashValue] = parti
        
    for comple in completion :
        totalCompletionHash += hash(comple)
        
    resultHashValue = totalParticipantHash - totalCompletionHash

    answer = dicParticipant[resultHashValue]
    
    return answer