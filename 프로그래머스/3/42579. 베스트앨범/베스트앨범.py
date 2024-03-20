def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    play_dict = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_dict.keys():
            genre_dict[genre] = play
        else:
            genre_dict[genre] += play
        
        if genre not in play_dict.keys():
            play_dict[genre] = [(idx, play)]
        else:
            play_dict[genre].append((idx, play))
    
    print(genre_dict)
    print(play_dict)
        
    for (k, v) in sorted(genre_dict.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(play_dict[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
            
    return answer