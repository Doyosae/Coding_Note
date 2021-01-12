from typing import Any, Sequence
import copy

def seq_search (seq: Sequence, key: Any) -> int:
      # 시퀀스 x와 찾고 싶은 값 key를 받고
      # seq를 딥 카피해서 a에 저장하고 그 끝에 key를 append
      a = copy.deepcopy(seq)
      a.append(key)

      # 탐색 시작
      # 만약에 a[0]에 key가 있다면 멈춘다.
      # 그렇지 않으면 -1를 리턴한다.
      i = 0
      while True:
            if a[i] == key:
                  break

            # 탐색하는 리스트의 시퀀스를 세는 인자
            i = i + 1
      return -1 if i == len(seq) else i

if __name__ == "__main__":
      num = int(input("원소 수를 입력허세요.  : "))

      # 입력한 원소 수 만큼의 빈 리스트 생성
      x = [None] * num

      # 값 하나하나 다 입력
      for i in range (num):
            x[i] = int(input(f'x[{i}]: '))
      
      # 찾고 싶은 값 입력
      ky = int(input("검색 할 값을 입력하세요. :  "))
      idx = seq_search(x, ky)

      if idx == -1:
            print("검색값을 찾는 원소가 없다.")
      else:
            print(f"검색값은 x[{idx}]에 있습니다.")
