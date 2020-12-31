import math
diagonal_distnace, height_ratio, width_ratio = map(int, input().split())

def calculator (diagonal_distnace, height_ratio, width_ratio):    
    diagonal_ratio  = math.sqrt(height_ratio**2 + width_ratio**2)
    height_distance = diagonal_distnace * height_ratio / diagonal_ratio
    width_distance  = diagonal_distnace * width_ratio / diagonal_ratio
    return height_distance, width_distance

r1, r2 = calculator(diagonal_distnace, height_ratio, width_ratio)
print(int(r1), int(r2))