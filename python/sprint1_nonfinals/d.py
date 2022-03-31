from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    n = len(temperatures)-1
    if len(temperatures) == 1:
        return 1
    if  temperatures[0] > temperatures[1]:
            count += 1
    if temperatures[n] > temperatures[n - 1]:
            count += 1
    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            count += 1    
    return count
    
def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
