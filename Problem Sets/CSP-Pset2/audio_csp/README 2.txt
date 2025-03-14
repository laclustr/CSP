audio_csp has 2 function calls for loading your data as integer lists.

Put the audio_csp.py file in the same folder as your working directory and then import audio_csp at the top of your file.

load_song(filename) will flatten left and right speaker values into a 1d list and return that list
load_song(filename, True) will return left and right speaker values as two separate lists of ints.

unpack them as follows:
for a flattened file:
rick_roll = audio_csp.load_song("never_gonna_give_you_up.wav")

for two channels separately:
channels = audio_csp.load_song("never_gonna_give_you_up.wav", True)
left_channel = channels[0]
right_channel = channels[1]

You may pass audio_csp.save_song a filename and a singular 1D song list to save a mono sound file
audio_csp.save_song("flattened_muted_astley.wav", rick_roll)

You may pass audio_csp.save_song a filename and two 1D song lists to save a stereo file. The first list is the left channel, the second is the right.
audio_csp.save_song("muted_left_channel.wav", left, right)

A few more useful functions:
get_time_idx(song, time) -> give an instance of the song and the time you want (in seconds) and it'll tell you the index where that time starts in the list.

set_song_list(song, list) -> sets the song's list to a list of integers. Be sure that `song` was loaded using audio_csp.load_song() because it contains a bunch of metadata associated with the song that you will save later.

get_song_freq(song) -> returns the frequency of the song

set_song_freq(song, new_freq) -> sets the frequency of the song to new_freq

Some more advanced ideas:
goto_freq_domain(song) -> moves the data to the frequency domain via a Fourier transform
	While in the frequency domain, you can call get_frequency_data(song) which returns a list. The first element is the frequencies and the second is the amplitudes associated with those frequencies.

goto_time_domain(song) -> moves you back from the frequency domain to the time domain