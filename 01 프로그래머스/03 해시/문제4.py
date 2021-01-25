def sorting(list):
    
    index_list = []
    for index in range(len(list)-1):
        for j in range(len(list)-1-index):
            if list[j+1][1] > list[j][1]:
                temp_v, temp_j = list[j][0], list[j][1]
                list[j][0], list[j][1] = list[j+1][0], list[j+1][1]
                list[j+1][0], list[j+1][1] = temp_v, temp_j
                
    for d1, d2 in list:
        index_list.append(d1)

    return index_list


def solution(genres, plays):
    plays_per_genre = {}
    genre_index     = {}
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre in plays_per_genre:
            plays_per_genre[genre] += play
            genre_index[genre].append([index, play])
        else:
            plays_per_genre[genre] = play
            genre_index[genre]     = [[index, play]]
    
    print("장르별 당 재생수:        ", plays_per_genre)
    print("장르별 인덱스와 재생수:  ", genre_index)
    ####################################################################################

    answer = []
    plays_per_genre = sorted(plays_per_genre.items(), key=(lambda x:x[1]), reverse=True)
    for g in plays_per_genre:
        print(g[0])
        index_list = sorting(genre_index[str(g[0])])
        answer     = answer + index_list[:2]

    print(answer)
    return answer

'''
해결 아이디어
1. 장르별 총 재생수를 딕셔너리로 계산하고 재생수에 따른 sort
2. 장르별 [인덱스, 재생수] 항목으로 딕셔너리 만들기
3. 1. 에서 소팅한 재생수롤 반복문으로 돌려서
    해당 키에 해당하는 [인덱스, 재생수] 리스트를 받고 재생수가 큰 순서대로 [인덱스, 재생수] 나열
    거기에 해당하는 인덱스 추출
'''
def main():
    solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

if __name__ == "__main__":
    main()