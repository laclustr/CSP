import csv

#Load Tracks
def load_tracks():
	tracks = []
	with open("classic_rock_songs.csv", "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			tracks.append(row)
		for dic in range(len(tracks)):
			tracks[dic]["year"] = int(tracks[dic]["year"])
			tracks[dic]['playcount'] = int(tracks[dic]['playcount'])
	return tracks

#Problem 1a
def make_year_vs_plays_dict(dic_lis):
	year_dict = {}
	for dic in range(len(tracks)):
		if dic_lis[dic]["year"] not in year_dict.keys():
			year_dict[dic_lis[dic]["year"]] = dic_lis[dic]["playcount"]
		else:
			year_dict[dic_lis[dic]["year"]] += dic_lis[dic]["playcount"]
	return year_dict

#Problem 1b
def print_sideways_histogram(dic):
	countperhash = 100
	for year in sorted(dic.keys()):
		print(f"{str(year)[2:]}: {"#" * (dic[year] // countperhash)}")
	print("--------------------------------")
	print(f"# = {countperhash} counts")
#End Problem 1b

def swap(li, idx1, idx2):
	temp = li[idx1]
	li[idx1] = li[idx2]
	li[idx2] = temp
	return li

#Problem 2
def track_playcount_list(dic_lis):
	for song in range(len(dic_lis) - 1, 0, -1):
		for i in range(song):
			if dic_lis[i]["playcount"] > dic_lis[i + 1]["playcount"]:
				dic_lis = swap(dic_lis, i, i + 1)
	return dic_lis[::-1]

#Problem 2b
def print_sorted_table(dic_lis):
	dic_lis = track_playcount_list(dic_lis)
	for song in range(20):
		print(f"Title: {dic_lis[song]["title"]}, Artist: {dic_lis[song]["artist"]}, Year: {dic_lis[song]["year"]}")

#Problem 3
def rev_tuples(dic_lis):
	new_dic = {}
	for dic in range(len(dic_lis)):
		if dic_lis[dic]["artist"] not in new_dic.keys():
			new_dic[dic_lis[dic]["artist"]] = dic_lis[dic]["playcount"]
		else:
			new_dic[dic_lis[dic]["artist"]] += dic_lis[dic]["playcount"]

	tup_lis = []
	for key in new_dic.keys():
		tup_lis.append((key, new_dic[key]))

	for tup in range(len(tup_lis) - 1, 0, -1):
		for i in range(tup):
			if tup_lis[i][1] > tup_lis[i + 1][1]:
				tup_lis = swap(tup_lis, i, i + 1)
	return tup_lis[::-1]

#Problem 3b
def print_top25_pct(dic_lis):
	tup_lis = rev_tuples(dic_lis)

	total_plays = 0
	for i in tup_lis:
		total_plays += i[1]

	for song in range(25):
		print(f"{song}: {tup_lis[song][0]}, {(tup_lis[song][1] / total_plays) * 100:.1f}%")