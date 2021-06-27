def solution(phone_book):
    
    answer = True
        
    for phone_num in phone_book:
        num = ""
        for each_num in phone_num :
            num += each_num
            if num in phone_book and num != phone_num :
                answer = False
    
    return answer