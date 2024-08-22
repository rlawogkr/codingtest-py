# 차량별로 주차요금을 계산하려고 함
# 출차 기록이 없으면, 23:59 에 출차된 것으로 간주
# 1. 누적시간 <= 기본 시간: 기본 요금을 청구
# 2. 누적시간 > 기본 시간: 초과된 시간에 대해 단위 시간마다 단위 요금을 청구
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림
#
import math

def solution(fees, records):
    answer = []
    car = {}  # <carNum: 입차 시간>
    total_time = {}  # <carNum: 주차 요금>

    # 1. 주차 기록 처리
    for record in records:
        time, carNum, io = record.split()  # 시간, 차량 번호, 입출차 정보
        hour, minute = time.split(":")
        realTime = int(hour) * 60 + int(minute)  # 시간을 분으로 변환

        if io == "IN":
            car[carNum] = realTime  # 차량 입차 시간 저장
        elif io == "OUT":
            # 차량 출차 시간과 입차 시간 차이 계산
            parked_time = realTime - car[carNum]
            if carNum in total_time:
                total_time[carNum] += parked_time
            else:
                total_time[carNum] = parked_time
            del car[carNum]  # 차량 입차 기록 삭제

    # 2. 자정까지 주차 중인 차량 처리
    for carNum, in_time in car.items():
        end_time = 23 * 60 + 59  # 자정까지의 시간 (23:59)
        parked_time = end_time - in_time
        if carNum in total_time:
            total_time[carNum] += parked_time
        else:
            total_time[carNum] = parked_time

    # 3. 주차 요금 계산
    for carNum, total in total_time.items():
        over_time = max(0, total - fees[0])
        charge = fees[1] + math.ceil(over_time / fees[2]) * fees[3]
        total_time[carNum] = charge

    # 4. 차량 번호로 정렬하고 결과 리스트에 추가
    sorted_cars = sorted(total_time.items())  # 차량 번호로 정렬
    for carNum, charge in sorted_cars:
        answer.append(charge)


    return answer
