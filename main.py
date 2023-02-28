painting = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

dates = [1939, 1933, 1946, 1940]

paintings = list(zip(painting, dates))

print(paintings)


painting.append('The Broken Column')
painting.append('The Wounded Deer')
painting.append('Me and My Doll')

dates.append(1944)
dates.append(1946)
dates.append(1937)

paintings = list(zip(painting, dates))

print(paintings)

print(len(paintings))

audio_tour_number = list(range(1, len(paintings)))
audio_tour_numbers = [1, 2, 3, 4, 5, 6, 7]

master_list = list(zip(audio_tour_number,painting,dates))

print(master_list)




