import audio_csp as ac

song = ac.load_song("never_gonna_give_you_up.wav")

start_idx = ac.get_time_idx(song, 5)
stop_idx = ac.get_time_idx(song, 10)

clip = song[start_idx:stop_idx]

ac.goto_freq_domain(clip)

data = ac.get_frequency_data(clip)

freq = data[0]
ampl = data[1]

for i in range(len(freq)):
	if abs(freq[i]) >= 20 and abs(freq[i]) <= 200:
		clip[i] *= 3

ac.goto_time_domain(clip)

ac.save_song("bass_boosted.wav", clip)