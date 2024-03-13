files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

def custom_key(list):
    return (list[0].lower(), int(list[1]))

def solution(files):
    answer = []
    #i는 string
    for _str in files:
        head = find_head(_str)[0] 
        numbers = find_mid(_str, find_head(_str)[1])[0]
        tail = find_end(_str, find_mid(_str, find_head(_str)[1])[1])
        answer.append([head, numbers, tail])
    sorted_list = sorted(answer, key = lambda x: custom_key(x))
    
    res = []
    for obj in sorted_list:
        tmp = obj[0] + str(obj[1]) + obj[-1]
        res.append(tmp)

    print(res)
    return res
        

def find_head(str):
    idx = 0
    for i in str:
        if ord(i) < 48 or ord(i) > 57: idx += 1
        else: return str[:idx], idx

#배열, 인덱스 시작 지점을 인덱스로 받음. 문제가 되었던 부분! 다시 숫자가 나올 수도 있으므로 중간에 break 해줘야 함.
def find_mid(str,idx):
    end_idx = idx
    for i in range(idx, len(str)):
        if ord(str[i]) >= 48 and ord(str[i]) <= 57: end_idx += 1
        else: break
    return str[idx:end_idx], end_idx
    
#배열, 인덱스 시작 지점을 인덱스로 받음.
def find_end(str, idx):
    return str[idx:]

solution(files)
