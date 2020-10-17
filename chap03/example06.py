'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
이진 검색
이진 검색 알고리즘을 사용하려면 배열의 데이터가 정렬되어야 한다.
이 검색 알고리즘은 선형 검색보다 빠르다.

이진 검색은 배열의 중앙 값에서 키 값이 어디에 위치하는지 파악하고
있는 구간을 따라 전체 배열에서 절반을 자른다.

다시 자른 배열의 중앙 값과 키 값을 비교하여, 어느 배열을 자를지 결정한다.
이 점 떄문에 이진 검색은 정렬된 알고리즘에서 사용하기 편하다.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from typing import Any, Sequence

def bin_search (a: Sequence, key: Any) -> int:
      # sequence a에서 key와 일치하는 원소를 탐색
      pl = 0
      pr = len(a) -1

      while True:
            pc = (pl + pr) // 2

            # a[pc], 즉 시퀀스의 중앙 값이 키 값과 동일하면 그 중앙 값의 인데스를 리턴
            if a[pc] == key:
                  return pc

            # 키 값이 중앙 값보다 크므로 검색 범위를 그 위로 좁힌다.
            elif a[pc] < key:
                  pl = pc + 1
            else:
                  pr = pc -1
            if pl > pr:
                  break
      return -1

if __name__ == "__main__":
      num = int(input("원소 수를 입력하세요."))
      x   = [None] * num

      print("배열 데이터를 오름차순으로 입력하세요.")
      x[0] = int(input("x[0]:   "))

      for i in range (1, num):
            while True:
                  x[i] = int(input(f'x[{i}]:  '))
                  if x[i] >= x[i-1]:
                        break
            
      ky = int(input("검색할 값을 입력하세요.:  "))
      idx = bin_search(x, ky)

      if idx == -1:
            print("검색 값을 갖는 원소가 존재하지 않습니다.")
      else:
            print(f'검색 값은 x[{idx}]에 있습니다.')