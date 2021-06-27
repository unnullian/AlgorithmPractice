def solution(n, lost, reserve):
    answer = n
    
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]
    
    hash_map = {v:1 for v in _reserve}
    # { {2:1}, {4:1} }
    
    for lost_num in _lost :
        
        if hash_map.get(lost_num-1) == 1 :
            hash_map[lost_num-1] = None
            
        elif hash_map.get(lost_num+1) == 1 :
            hash_map[lost_num+1] = None
            
        else :
            answer -= 1

    return answer