def solution(answers):
    answer = []
    
    hash_map = {k:0 for k in range(1, 4)}
    
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    st1 = []
    st2 = []
    st3 = []
    
    for i in range(len(answers)) :
        st1.append(pattern1[i%len(pattern1)])
        st2.append(pattern2[i%len(pattern2)])
        st3.append(pattern3[i%len(pattern3)])
        
        if st1[i] == answers[i] :
            hash_map[1] += 1
        if st2[i] == answers[i] :
            hash_map[2] += 1
        if st3[i] == answers[i] :
            hash_map[3] += 1
    
    max_value = max(hash_map.values())
    
    for key, value in hash_map.items() :
        if value == max_value :
            answer.append(key)
    
    return answer