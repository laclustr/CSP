import wave
import sys
import os
import subprocess

### START OF DEPENDENCY JUNK ###

if not os.path.exists("assets"):
	os.mkdir("assets")
	
sys.path.append("assets")

def is_package_installed(package_name, target_folder):
	""" Check if package_name is installed to a specific target_folder """
	
	package_folder = os.path.join(target_folder, package_name)

	return os.path.exists(package_folder)

def install_package_to_folder(package_name, target_folder):
	""" Installs package_name to target_folder using pip/pip3 """
	if not is_package_installed(package_name, target_folder):
		print(f"Installing: {package_name} to {target_folder} folder...")
		try:
			with open(os.devnull, "w") as devnull:
				try:
					if os.name == "nt":
						subprocess.check_call(['pip', 'install', '--target', target_folder, package_name], stdout=devnull, stderr=devnull)
					else:
						subprocess.check_call(['pip3', 'install', '--target', target_folder, package_name], stdout=devnull, stderr=devnull)
				except subprocess.CalledProcessError:
					raise Exception(f"pip must be installed, and you must have an internet connection. Verify with pip --version or pip3 --version on mac/Linux")

		except subprocess.CalledProcessError:
			raise Exception(f"Error installing {package_name}")


install_package_to_folder("numpy", "assets")
import numpy as np

### END OF DEPENDENCY JUNK ###

class Song:
	"""Represent a wav file as an integer list"""
	def __init__(self, filename, flatten=False):
		self.filename     = filename
		self.num_frames   = None
		self.num_channels = None
		self.frequency	  = None
		self.sample_width = None
		self.bit_depth	  = None
		self.arr_dtype    = None
		self.time_domain  = True
		self.freqs        = None
		
		self.song_arr	     = None
		self.song_arr_time = None
		self.song_arr_fft  = None

		self._init_attrs(filename, flatten)

	def _init_attrs(self, filename, flatten):
		with wave.open(filename, "rb") as wav_file:
			self.num_frames   = wav_file.getnframes()
			self.num_channels = wav_file.getnchannels()
			self.frequency	  = wav_file.getframerate()
			self.sample_width = wav_file.getsampwidth()
			self.bit_depth	  = self.sample_width * 8

			match self.bit_depth:
				case 8:
					self.arr_dtype = np.int8
				case 16:
					self.arr_dtype = np.int16
				case 32:
					self.arr_dtype = np.int32
				case 64:
					self.arr_dtype = np.int64
				case _:
					sys.exit(f"Invalid bit depth in {filename}. Something went wrong with it.")

			# Check if actually 2 channel if trying to load 2 channel
			if self.num_channels != 2 and not flatten:
				sys.exit(f"Audio file {filename} has this many channels: {self.num_channels}. Cannot grab 2 channels.")

			# Read the audio data as a byte object
			audio_data = wav_file.readframes(self.num_frames)

			# Convert the byte object to an int np array of correct size
			int_data = np.frombuffer(audio_data, dtype=self.arr_dtype)




			"""
			Mention to Dr.B!!!!!!!!
			"""




			# If the audio has multiple channels, take the average to flatten to mono
			if self.num_channels == 2 and flatten:
				left_channel = int_data[0::2]
				right_channel = int_data[1::2]
				int_data = ((left_channel.astype(np.int32) + right_channel.astype(np.int32)) // 2).astype(self.arr_dtype)
			
			self.song_arr = int_data.tolist()

	def copy(self):
		"""Copies the song but appears to just copy the list representing the song."""
		song_copy = Song(self.filename, flatten = True)
		song_copy.song_arr = self.song_arr.copy()
		return song_copy

	def append(self, value):
		"""Append value to end of list."""
		self.song_arr.append(value)

	def extend(self, iterable):
		"""Adds any iterable to the end of the list."""
		self.song_arr.extend(iterable)
		
	def insert(self, index, value):
		"""Inserts value at index and reindexes."""
		self.song_arr.insert(index, value)

	def remove(self, x):
		"""Remove the first instance of x in the song."""
		return self.song_arr.remove(x)

	def pop(self, i=None):
		"""Remove the last, or specified index."""
		if i == None:
			return self.song_arr.pop()
		else:
			return self.song_arr.pop(i)

	def reverse(self):
		"""Reverse the song, in place."""
		self.song_arr.reverse()
		return self

	def goto_freq_domain(self):
		"""Song is now represented in Fourier space"""
		self.time_domain = False
		self.song_arr_fft = np.fft.fft(self.song_arr)
		self.song_arr = self.song_arr_fft

	def goto_time_domain(self):
		"""Song is now represented in time domain"""
		self.time_domain = True
		self.song_arr = np.real(np.fft.ifft(self.song_arr_fft)).tolist()

	def get_frequency(self):
		return self.frequency

	def get_frequency_data(self):
		"""Returns the frequencies and the magnitudes of those frequencies in Fourier space"""
		if self.time_domain:
			sys.exit(f"To do this you must have your song represented in the frequency domain with goto_freq_domain() first")

		return (np.fft.fftfreq(len(self.song_arr), d=1/self.frequency), np.abs(self.song_arr))

	def set_frequency(self, new_frequency):
		"""Mutate the frequency metadata of the Song"""
		self.frequency = new_frequency

	def save_song(self, file_path, n_channels=1, other=None):
		"""Save the song to file_path. Optional parameter for 2 channel."""
		if other and n_channels != 2:
			sys.exit(f"Require 2 channels to merge two songs.")
		if other and n_channels == 2:
			if self.frequency != other.frequency:
				sys.exit(f"Ch1 Frequency: {self.frequency}, Ch2 Frequency: {other.frequency}. Two channels must have the same frequency to be compatible.")
			if len(self.song_arr) != len(other.song_arr):
				sys.exit(f"Ch1 Len: {len(self.song_arr)}, Ch2 Len: {len(other.song_arr)}. Ch1 and Ch2 must have the same lengths to be compatible.")
			if self.arr_dtype != other.arr_dtype:
				sys.exit(f"Ch1 data type: {self.arr_dtype}, Ch2 data type: {other.arr_dtype}. Ch1 and Ch2 are not compatible data types. Check the bit depth of your files.")

		print(f"Writing {file_path}...")
		with wave.open(file_path, "wb") as wav_file:
			# Set WAV file parameters
			wav_file.setnchannels(n_channels)
			wav_file.setsampwidth(self.sample_width)
			wav_file.setframerate(self.frequency)
			wav_file.setnframes(len(self.song_arr))
			wav_file.setcomptype('NONE', 'not compressed')
			
			# Get the list of integers to write
			audio_data = np.array(self.song_arr, dtype=self.arr_dtype)

			if other:
				# Zip the two underlying channel arrays together.
				other_data = np.array(other.song_arr, dtype=other.arr_dtype)
				audio_data = np.vstack((audio_data, other_data)).reshape(-1, order="F")

			# Write the audio data to the WAV file
			wav_file.writeframes(audio_data)

	def __add__(self, other):
		if isinstance(other, Song):
			out_song = self.copy()
			out_song.song_arr = self.song_arr + other.song_arr
			return out_song
		elif isinstance(other, list):
			out_song = self.copy()
			out_song.song_arr = self.song_arr + other
			return out_song

		try:
			out_song = self.copy()
			out_song.song_arr += [other]
			return out_song
		except:
			sys.exit(f"Does not support concatenation between song list and {type(other)}")

	def __iadd__(self, other):
		if isinstance(other, Song):
			self.song_arr += other.song_arr
			return self
		elif isinstance(other, list):
			self.song_arr += other
			return self

		try:
			self.song_arr += [other]
			return self
		except:
			sys.exit(f"Does not support concatenation between song list and {type(other)}")

	def __radd__(self, other):
		other.__add__(self)
		return self

	def __getitem__(self, index):
		if isinstance(index, slice):
			out = self.copy()
			out.song_arr = out.song_arr[index.start:index.stop:index.step]
			return out

		return self.song_arr[index]

	def __setitem__(self, index, value):
		if isinstance(index, slice):
			try:
				start, stop, step = index.indices(len(self.song_arr))

				if len(value) != (stop - start):
					raise ValueError("The length of the value must match the slice length.")
 
				self.song_arr[start:stop] = value
			except Exception as e:
				sys.exit(e)

		self.song_arr[index] = value

	def __delitem__(self, index):
		if isinstance(index, slice):
			del self.song_arr[index.start:index.end:index.step]
		else:
			del self.song_arr[index] 

	def __iter__(self):
		self.iter_idx = 0
		return self

	def __next__(self):
		if self.iter_idx < len(self.song_arr):
			result = self.song_arr[self.iter_idx]
			self.iter_idx += 1
			return result
		raise StopIteration

	def __eq__(self, other):
		return self.song_arr == other.song_arr

	def __len__(self):
		return len(self.song_arr)

	def __repr__(self):
		return repr(self.song_arr)

	def __str__(self):
		return repr(self.song_arr)

def load_song(filename, stereo_sound=False):
	"""
		Load filename as a song that behaves mostly like a list of integers representing the waveform.
		stereo_sound=False flattens WAV to a 1D list. Removes channel information and averages left/right channels to mono sound.
		stereo_sound=True  returns a tuple of left and right channel songs.
		Only works with .wav extension.
	"""
	if not os.path.exists(filename):
		sys.exit(f"{filename} does not exist. Please load a valid audio file.")
	if not os.path.splitext(filename)[1] == ".wav":
		sys.exit(f"{filename} is not a .wav file. This program only works for wav files.")

	try:
		if not stereo_sound:



			#Mention to Dr. B that flatten= needed to be added



			return Song(filename, flatten=True)
		else:
			left  = Song(filename)
			right = Song(filename)

			left.song_arr  = left.song_arr[::2]
			right.song_arr = right.song_arr[1::2]

			return (left, right)
	except:
		sys.exit(f"Something went wrong... Are you sure {filename} exists, and is a .wav file?")

def save_song(filename, song, other=None):
	"""Saves song as filename. Only works with .wav extension. If other exists, song is the left channel and other is the right channel."""
	if not isinstance(song, Song):
		if isinstance(song, list):
			sys.exit(f"Problem saving... The song (or first channel) you provided is not an appropriate parameter. This must be the list returned by the load_song() function, not just a regular list.")
		else:
			sys.exit(f"Problem saving... The song (or first channel) you provided is not an appropriate parameter. This must be the list returned by the load_song() function, and you passed a {type(song)}.")
	
	if other and not isinstance(other, Song):
		if isinstance(other, list):
			sys.exit(f"Problem saving... The second channel you provided is not an appropriate parameter. This must be the list returned by the load_song() function, not just a regular list.")
		else:
			sys.exit(f"Problem saving... The second channel you provided is not an appropriate parameter. This must be the list returned by the load_song() function, and you passed a {type(other)}.")
	
	if other:
		song.save_song(filename, n_channels=2, other=other)
	else:
		song.save_song(filename)

def get_time_idx(song, time):
	"""Returns start index closest to time in sec."""
	return int(song.frequency * time)

def goto_freq_domain(song):
	"""Song is now represented in Fourier space"""
	song.goto_freq_domain()

def goto_time_domain(song):
	"""Song is now represented in time domain"""
	song.goto_time_domain()

def get_frequency_data(song):
	"""Returns the frequencies and the magnitudes of those frequencies in Fourier space"""
	return song.get_frequency_data()

def get_song_frequency(song):
	return song.get_frequency()

def set_song_frequency(song, new_frequency):
	"""Mutate the frequency metadata of the Song"""
	song.set_frequency(new_frequency)

if __name__ == "__main__":	
	pass