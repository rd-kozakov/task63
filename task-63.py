file = open("sport.txt", encoding='cp1251')
file.readline()
sport_count = {}
for line in file:
    cat = line.strip().split('\t')
    if len(cat) > 3:
        sport = cat[3]
        for sports in sport.strip().split(','):
            clean_sport = sports.strip()
            if clean_sport:
                if clean_sport in sport_count:
                    sport_count[clean_sport] += 1
                else:
                    sport_count[clean_sport] = 1
file.close()
top_sports = sorted(sport_count.items(), key=lambda x: x[1], reverse=True)[:3]

for sport, count in top_sports:
    print(sport, count)