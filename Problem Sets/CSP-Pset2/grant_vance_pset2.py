import random
from audio_csp import audio_csp as acsp

#Problem 1
def reverse_list(lis):
	result = []

	for i in lis:
		result = [i] + result

	return result

#Problem 2
def lin_search(lis, key):
	for i in range(len(lis)):
		if lis[i] == key:
			return i

	return -1

#Problem 3
def bin_search(lis, key):
	topidx = len(lis) - 1
	btmidx = 0

	for i in range(len(lis)):
		mid = (topidx + btmidx) // 2

		if lis[mid] == key:
			return mid
		elif lis[mid] < key:
			btmidx = mid
		else:
			topidx = mid

	return -1
#End Problem 3

def swap(lis, idx1, idx2):
	temp = lis[idx2]
	lis[idx2] = lis[idx1]
	lis[idx1] = temp

#Problem 4
def selection_sort(lis):
	for i in range(len(lis)):
		smallest_idx = i

		for f in range(i + 1, len(lis)):
			if lis[f] < lis[smallest_idx]:
				smallest_idx = f

		swap(lis, i, smallest_idx)

#Problem 5
def bubble_sort(lis):
	for i in range(len(lis)):
		for f in range(len(lis) - 1):
			if lis[f] > lis[f + 1]:
				swap(lis, f, f + 1)

#Problem 6
def insertion_sort(lis):
	for i in range(1, len(lis)):
		for j in range(i, 0, -1):
			if lis[j] < lis[j - 1]:
				swap(lis, j, j - 1)

#Problem 7
def count_ints(lis, threshold):
	counter = 0

	for i in range(len(lis)):
		if lis[i] >= threshold:
			counter += 1

	return counter

#Problem 8
def list_mask(lis, threshold):
	for i in range(len(lis)):
		if lis[i] >= threshold:
			lis[i] = ""
		else:
			lis[i] = "*"

	return lis

#Problem 9
def img_mask(lis, lis_mask):
	for i in range(len(lis)):
		if lis_mask[i] == "":
			lis[i] = 0

	return lis

#Problem 10
def min_max(lis):
	min0 = lis[0]
	max0 = lis[0]

	for i in lis:
		if i > max0:
			max0 = i 
		if i < min0:
			min0 = i

	return (min0, max0)

#Problem 11
def get_avg(lis):
	sum0 = 0

	for i in lis:
		sum0 += i

	return sum0 / len(lis)

#Problem 12
def get_stdev(lis):
	avg = get_avg(lis)
	vari = 0

	for i in lis:
		vari += (i - avg) ** 2

	vari /= len(lis)

	return vari ** 0.5

#Problem 13
def alt_sum(lis):
	sum0 = 0

	for i in range(len(lis)):
		if not i % 2:
			sum0 += lis[i]
		else:
			sum0 -= lis[i]

	return sum0

#Problem 14
def setify(lis):
	seen = []

	for i in range(len(lis)):
		if lis[i] not in seen:
			seen += [lis[i]]

	return seen

#Problem 15
def set_add(lis, val):
	lis = setify(lis)
	notFound = True

	for i in lis:
		if i == val:
			notFound = False

	if notFound:
		return lis + [val]

	return lis

#Problem 16
def set_union(lis1, lis2):
	for i in range(len(lis1)):
		lis2 = set_add(lis2, lis1[i])
		insertion_sort(lis2)

	lis2 = setify(lis2)

	return lis2

#Problem 17
def set_intersection(lis1, lis2):
	same = []
	for i in range(len(lis1)):
		for j in range(len(lis2)):
			if lis1[i] == lis2[j] and lis1[i] not in same:
				same += [lis1[i]]
	return same

#Problem 18
def is_subset(lis1, subset):
	isct = set_intersection(lis1, subset)
	if isct == subset:
		return True
	return False

#Problem 19
def set_difference(A, B):
	diff = []

	for i in range(len(A)):
		if A[i] not in B:
			diff += [A[i]]

	return diff

#Problem 20
def set_symmetric_diff(A, B):
	diff = []

	for i in range(len(A)):
		if A[i] not in B:
			diff += [A[i]]

	for i in range(len(B)):
		if B[i] not in diff and B[i] not in A:
			diff += [B[i]]

	return diff

#Problem 21
def shuffle_list(L):
	for i in range(len(L) - 1, 0, -1):
		j = random.randint(0, i)
		swap(L, i, j)
	return L

#Problem 22
def consecutive_song(N):
	lis = []

	for i in range(1, N + 1):
		lis += [i]

	lis = shuffle_list(lis)

	for i in range(len(lis) - 1):
		if (lis[i] + 1) == lis[i + 1]:
			return True

	return False

#Problem 23
def con_song_prob(N):
	success = 0
	simulations = 10000

	for i in range(simulations):
		if consecutive_song(N):
			success += 1

	return success / simulations

#Problem 24
def is_mountain_list(L):
	if len(L) < 3:
		return False

	maxIdx = 0

	for i in range(len(L)):
		if L[i] > L[maxIdx]:
			maxIdx = i

	if L[maxIdx - 1] == L[maxIdx] or L[maxIdx + 1] == L[maxIdx]:
		return False

	for i in range(maxIdx):
		if not (L[i] < L[i + 1]):
			return False

	for i in range(maxIdx, len(L) - 1):
		if not (L[i] > L[i + 1]):
			return False

	return True

#Problem 25
def largest_hotel_value(L, amount):
	insertion_sort(L)
	maxVal = 0
	startIdx = 0

	for i in range(len(L)):	
		testVal = 0

		for j in range(i, len(L)):
			testVal += L[j]

			if testVal > amount:
				break

			if testVal > maxVal:
				maxVal = testVal

	return maxVal

#Problem 26
def my_soda(N):
	simulations = 1000
	success = 0

	for _ in range(simulations):
		lis = []

		for i in range(N):
			lis += [i]

		newLis = lis.copy()
		shuffle_list(newLis)

		for i in range(len(lis)):
			if lis[i] == newLis[i]:
				success += 1
				break

	return success / simulations
#End Problem 26

def to_str_w_space(lis):
	res = ""
	for i in range(len(lis)):
		if i == len(lis) - 1:
			res += lis[i]
		else:
			res += lis[i] + " "

	return res

#Project 1
def play_mastermind():
	code = ""
	for i in range(4):
		code += str(random.randint(0,9))
	code_as_list = []
	for i in range(len(code)):
		code_as_list += [code[i]]

	response = []
	for i in range(len(code)):
		response += ["_"]
	print(code)
	print("Code: " + to_str_w_space(response))

	guesses = 10
	while guesses > 0:
		answer = input("Guess: ")
		answer_as_list = []
		for i in range(len(answer)):
			answer_as_list += [answer[i]]

		if code_as_list == answer_as_list:
			print("Code: Right!")
			break

		guesses -= 1
		if len(answer) != len(code):
			guesses += 1
			continue

		comp_list = code_as_list[:]
		for i in range(len(code_as_list)):
			if code_as_list[i] == answer_as_list[i]:
				response[i] = code_as_list[i]
				comp_list[i] = "/"

		for i in range(len(code_as_list)):
			if comp_list[i] in answer_as_list and response[i] == "_":
				idx = lin_search(comp_list, answer_as_list[i])
				response[i] = "*"
				comp_list[i] = "/"

		if guesses == 0:
			print("Code: " + code)
			break

		print("Code: " + to_str_w_space(response))
	
#Project 2
def play_wordle():
	words = ['aback', 'abase', 'abate', 'abbey', 'abide', 'about', 'above', 'abyss', 'acorn', 'acrid', 'actor', 'acute', 'adage', 'adapt', 'admit', 'adobe', 'adopt', 'adore', 'adult', 'after', 'again', 'agape', 'agate', 'agent', 'agile', 'aging', 'aglow', 'agony', 'agree', 'ahead', 'aisle', 'album', 'alien', 'alike', 'alive', 'allow', 'aloft', 'alone', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'amass', 'amber', 'amiss', 'ample', 'angel', 'anger', 'angry', 'angst', 'anode', 'antic', 'anvil', 'aorta', 'apart', 'aphid', 'apple', 'apply', 'apron', 'aptly', 'arbor', 'ardor', 'argue', 'aroma', 'ascot', 'aside', 'askew', 'asset', 'atoll', 'atone', 'audio', 'audit', 'avail', 'avert', 'await', 'awake', 'awash', 'awful', 'axiom', 'azure', 'bacon', 'badge', 'badly', 'bagel', 'baker', 'balsa', 'banal', 'barge', 'basic', 'basin', 'bathe', 'baton', 'batty', 'bawdy', 'bayou', 'beach', 'beady', 'beast', 'beaut', 'beefy', 'beget', 'begin', 'being', 'belch', 'belie', 'belly', 'below', 'bench', 'beret', 'berth', 'beset', 'bevel', 'binge', 'biome', 'birch', 'birth', 'black', 'blame', 'bland', 'blare', 'blaze', 'bleak', 'bleed', 'bleep', 'blimp', 'block', 'bloke', 'blond', 'blown', 'bluff', 'blurb', 'blurt', 'blush', 'boast', 'booby', 'boost', 'booze', 'boozy', 'borax', 'bossy', 'bough', 'boxer', 'brace', 'braid', 'brain', 'brake', 'brash', 'brass', 'brave', 'bravo', 'bread', 'break', 'breed', 'briar', 'bribe', 'bride', 'brief', 'brine', 'bring', 'brink', 'briny', 'brisk', 'broad', 'broke', 'brook', 'broom', 'broth', 'brown', 'brush', 'brute', 'buddy', 'buggy', 'bugle', 'build', 'built', 'bulky', 'bully', 'bunch', 'burly', 'cable', 'cacao', 'cache', 'cadet', 'camel', 'cameo', 'candy', 'canny', 'canoe', 'canon', 'caper', 'carat', 'cargo', 'carol', 'carry', 'carve', 'catch', 'cater', 'caulk', 'cause', 'cedar', 'chafe', 'chain', 'chalk', 'champ', 'chant', 'chaos', 'chard', 'charm', 'chart', 'cheat', 'cheek', 'cheer', 'chest', 'chief', 'child', 'chill', 'chime', 'chock', 'choir', 'choke', 'chord', 'chunk', 'chute', 'cider', 'cigar', 'cinch', 'circa', 'civic', 'class', 'clean', 'clear', 'cleft', 'clerk', 'click', 'climb', 'cling', 'clock', 'clone', 'close', 'cloth', 'cloud', 'clown', 'cluck', 'coach', 'coast', 'cocoa', 'colon', 'comet', 'comma', 'condo', 'conic', 'corny', 'could', 'count', 'court', 'cover', 'covet', 'cower', 'coyly', 'craft', 'cramp', 'crane', 'crank', 'crass', 'crate', 'crave', 'craze', 'crazy', 'creak', 'credo', 'crept', 'crime', 'crimp', 'croak', 'crone', 'cross', 'crowd', 'crown', 'crumb', 'crush', 'crust', 'crypt', 'cumin', 'curly', 'cynic', 'daddy', 'daisy', 'dance', 'dandy', 'death', 'debit', 'debug', 'debut', 'decal', 'decay', 'decoy', 'delay', 'delta', 'delve', 'denim', 'depot', 'depth', 'deter', 'devil', 'diary', 'dicey', 'digit', 'diner', 'dingo', 'disco', 'ditto', 'dodge', 'dogma', 'doing', 'dolly', 'donor', 'donut', 'doubt', 'dowry', 'dozen', 'drain', 'drawn', 'dream', 'drink', 'drive', 'droll', 'drool', 'droop', 'drove', 'duchy', 'dutch', 'duvet', 'dwarf', 'dwell', 'dwelt', 'early', 'earth', 'easel', 'ebony', 'edict', 'egret', 'eject', 'elder', 'elope', 'elude', 'email', 'ember', 'empty', 'enact', 'endow', 'enema', 'enjoy', 'ennui', 'ensue', 'enter', 'epoch', 'epoxy', 'equal', 'equip', 'erode', 'error', 'erupt', 'essay', 'ether', 'ethic', 'ethos', 'evade', 'event', 'every', 'evoke', 'exact', 'exalt', 'excel', 'exert', 'exist', 'expel', 'extra', 'exult', 'facet', 'faint', 'faith', 'farce', 'fault', 'favor', 'feast', 'feign', 'feral', 'ferry', 'fewer', 'fiber', 'field', 'fiend', 'fifty', 'filet', 'final', 'finch', 'finer', 'first', 'fishy', 'fixer', 'fjord', 'flail', 'flair', 'flake', 'flame', 'flank', 'flare', 'flash', 'flask', 'flesh', 'flick', 'fling', 'flirt', 'float', 'flock', 'flood', 'floor', 'flora', 'floss', 'flour', 'flout', 'flown', 'fluff', 'flume', 'flung', 'flunk', 'flyer', 'focal', 'focus', 'foggy', 'folly', 'foray', 'force', 'forge', 'forgo', 'forte', 'forth', 'forty', 'found', 'foyer', 'frail', 'frame', 'frank', 'fresh', 'fried', 'frock', 'frond', 'front', 'frost', 'froth', 'frown', 'froze', 'fully', 'fungi', 'funky', 'funny', 'gamer', 'gamma', 'gamut', 'gaudy', 'gaunt', 'gauze', 'gawky', 'gecko', 'genre', 'ghoul', 'giant', 'giddy', 'girth', 'given', 'glass', 'glaze', 'gleam', 'glean', 'glide', 'gloat', 'globe', 'gloom', 'glory', 'glove', 'glyph', 'gnash', 'going', 'golem', 'goner', 'goofy', 'goose', 'gorge', 'gouge', 'grace', 'grade', 'grail', 'grand', 'grant', 'graph', 'grasp', 'grate', 'great', 'green', 'greet', 'grief', 'grime', 'grimy', 'grind', 'gripe', 'groin', 'groom', 'group', 'grout', 'grove', 'growl', 'gruel', 'guano', 'guard', 'guest', 'guide', 'guild', 'guile', 'gully', 'gummy', 'guppy', 'gusty', 'hairy', 'halve', 'handy', 'happy', 'harsh', 'hatch', 'hater', 'havoc', 'heady', 'heard', 'heart', 'heath', 'heave', 'heavy', 'hefty', 'heist', 'helix', 'hello', 'hence', 'heron', 'hilly', 'hinge', 'hippo', 'hitch', 'hoard', 'hobby', 'homer', 'honey', 'horde', 'horse', 'hotel', 'hound', 'house', 'howdy', 'human', 'humid', 'humor', 'humph', 'hunch', 'hunky', 'hurry', 'hutch', 'hyena', 'hyper', 'igloo', 'image', 'impel', 'inane', 'index', 'inept', 'inert', 'infer', 'inlay', 'inner', 'input', 'inter', 'intro', 'ionic', 'irate', 'irony', 'islet', 'itchy', 'ivory', 'jaunt', 'jazzy', 'jelly', 'jerky', 'jiffy', 'joint', 'joker', 'jolly', 'joust', 'judge', 'juice', 'karma', 'kayak', 'kazoo', 'kebab', 'khaki', 'kiosk', 'knave', 'knead', 'kneel', 'knelt', 'knock', 'knoll', 'koala', 'label', 'labor', 'lager', 'lanky', 'lapel', 'lapse', 'large', 'larva', 'laser', 'latte', 'layer', 'leafy', 'leaky', 'leapt', 'learn', 'leash', 'leave', 'ledge', 'leech', 'leery', 'leggy', 'lemon', 'libel', 'light', 'lilac', 'limit', 'linen', 'liner', 'lingo', 'lithe', 'liver', 'local', 'locus', 'lofty', 'logic', 'loopy', 'loser', 'louse', 'lover', 'lower', 'lowly', 'loyal', 'lucid', 'lucky', 'lunar', 'lunch', 'lunge', 'lusty', 'lying', 'macaw', 'madam', 'magic', 'magma', 'maize', 'major', 'manga', 'mania', 'manly', 'manor', 'maple', 'march', 'marry', 'marsh', 'mason', 'masse', 'match', 'matey', 'mauve', 'maxim', 'maybe', 'mayor', 'mealy', 'meant', 'medal', 'media', 'medic', 'melon', 'mercy', 'merge', 'merit', 'merry', 'metal', 'meter', 'metro', 'micro', 'midge', 'midst', 'mimic', 'mince', 'miner', 'minus', 'model', 'modem', 'moist', 'molar', 'mommy', 'money', 'month', 'moose', 'mossy', 'motor', 'motto', 'moult', 'mount', 'mourn', 'mouse', 'movie', 'mucky', 'mulch', 'mummy', 'mural', 'mushy', 'music', 'musty', 'naive', 'nanny', 'nasty', 'natal', 'naval', 'needy', 'neigh', 'nerdy', 'never', 'nicer', 'niche', 'night', 'ninja', 'ninth', 'noble', 'noise', 'north', 'nymph', 'occur', 'ocean', 'octet', 'offal', 'often', 'older', 'olive', 'onion', 'onset', 'opera', 'order', 'organ', 'other', 'ought', 'ounce', 'outdo', 'outer', 'overt', 'owner', 'oxide', 'paint', 'panel', 'panic', 'papal', 'paper', 'parer', 'parry', 'party', 'pasta', 'patio', 'patty', 'pause', 'peace', 'peach', 'pearl', 'penne', 'perch', 'perky', 'pesky', 'phase', 'phone', 'phony', 'photo', 'piano', 'picky', 'piety', 'pilot', 'pinch', 'piney', 'pinky', 'pinto', 'pious', 'piper', 'pique', 'pithy', 'pixel', 'pixie', 'place', 'plait', 'plank', 'plant', 'plate', 'plaza', 'pleat', 'pluck', 'plumb', 'plunk', 'point', 'poise', 'poker', 'polka', 'polyp', 'porch', 'pound', 'power', 'press', 'price', 'prick', 'pride', 'prime', 'primo', 'primp', 'print', 'prior', 'prize', 'probe', 'prone', 'prong', 'proud', 'prove', 'prowl', 'proxy', 'prune', 'psalm', 'pulpy', 'purge', 'qualm', 'quart', 'queen', 'query', 'quest', 'queue', 'quick', 'quiet', 'quirk', 'quite', 'quote', 'radio', 'rainy', 'raise', 'ramen', 'ranch', 'range', 'ratio', 'rayon', 'react', 'ready', 'realm', 'rebel', 'rebus', 'rebut', 'recap', 'recur', 'refer', 'regal', 'relic', 'renew', 'repay', 'repel', 'rerun', 'resin', 'retch', 'retro', 'retry', 'revel', 'rhino', 'rhyme', 'rider', 'ridge', 'right', 'riper', 'risen', 'rival', 'robin', 'robot', 'rocky', 'rodeo', 'rogue', 'roomy', 'rouge', 'round', 'rouse', 'route', 'rover', 'royal', 'ruddy', 'ruder', 'rupee', 'rusty', 'saint', 'salad', 'sally', 'salsa', 'salty', 'sandy', 'sassy', 'saucy', 'saute', 'savor', 'scald', 'scale', 'scant', 'scare', 'scarf', 'scent', 'scoff', 'scold', 'scone', 'scope', 'scorn', 'scour', 'scout', 'scowl', 'scram', 'scrap', 'scrub', 'sedan', 'seedy', 'sense', 'serum', 'serve', 'seven', 'sever', 'shade', 'shaft', 'shake', 'shaky', 'shall', 'shame', 'shank', 'shape', 'shard', 'sharp', 'shave', 'shawl', 'shell', 'shift', 'shine', 'shire', 'shirk', 'shore', 'shorn', 'shout', 'shove', 'shown', 'showy', 'shrub', 'shrug', 'shyly', 'siege', 'sight', 'since', 'sissy', 'sixth', 'skate', 'skier', 'skiff', 'skill', 'skimp', 'skirt', 'skunk', 'slang', 'slate', 'sleek', 'sleep', 'slice', 'slope', 'slosh', 'sloth', 'slump', 'slung', 'small', 'smart', 'smash', 'smear', 'smelt', 'smile', 'smirk', 'smite', 'smith', 'smock', 'smoke', 'snack', 'snafu', 'snail', 'snake', 'snaky', 'snare', 'snarl', 'sneak', 'snoop', 'snort', 'snout', 'soggy', 'solar', 'solid', 'solve', 'sonic', 'sound', 'sower', 'space', 'spade', 'speak', 'speck', 'spell', 'spelt', 'spend', 'spent', 'spice', 'spicy', 'spiel', 'spike', 'spill', 'spine', 'spire', 'splat', 'spoke', 'spoon', 'spout', 'spray', 'spurt', 'squad', 'squat', 'staff', 'stage', 'staid', 'stain', 'stair', 'stake', 'stale', 'stall', 'stand', 'stark', 'start', 'stash', 'state', 'stead', 'steam', 'steed', 'steel', 'stein', 'stern', 'stick', 'stiff', 'still', 'sting', 'stink', 'stint', 'stock', 'stoic', 'stole', 'stomp', 'stone', 'stony', 'stool', 'store', 'storm', 'story', 'stout', 'stove', 'strap', 'straw', 'stray', 'study', 'stung', 'style', 'sugar', 'sulky', 'super', 'surer', 'surly', 'sushi', 'sweat', 'sweep', 'sweet', 'swell', 'swill', 'swine', 'swirl', 'swish', 'swoon', 'swung', 'syrup', 'table', 'taboo', 'tacit', 'tacky', 'taken', 'tally', 'talon', 'tangy', 'taper', 'tapir', 'tardy', 'taste', 'tasty', 'taunt', 'tawny', 'teach', 'teary', 'tease', 'tempo', 'tenth', 'tepid', 'terse', 'thank', 'their', 'theme', 'there', 'these', 'thief', 'thigh', 'thing', 'think', 'third', 'thorn', 'those', 'three', 'threw', 'throw', 'thumb', 'thump', 'thyme', 'tiara', 'tibia', 'tidal', 'tiger', 'tilde', 'tipsy', 'titan', 'tithe', 'title', 'today', 'tonic', 'topaz', 'topic', 'torch', 'torso', 'totem', 'touch', 'tough', 'towel', 'toxic', 'toxin', 'trace', 'tract', 'trade', 'train', 'trait', 'trash', 'trawl', 'treat', 'trend', 'triad', 'trice', 'trite', 'troll', 'trope', 'trove', 'truly', 'truss', 'trust', 'truth', 'tryst', 'tunic', 'tutor', 'twang', 'tweak', 'tweed', 'twice', 'twine', 'twirl', 'twist', 'ulcer', 'ultra', 'uncle', 'under', 'undue', 'unfed', 'unfit', 'unify', 'unite', 'unlit', 'unmet', 'untie', 'until', 'unzip', 'upset', 'urban', 'usage', 'usher', 'using', 'usual', 'usurp', 'utter', 'uvula', 'vague', 'valet', 'valid', 'value', 'vapid', 'vault', 'venom', 'verge', 'verve', 'video', 'vigor', 'vinyl', 'viola', 'viral', 'visor', 'vital', 'vivid', 'vodka', 'voice', 'voila', 'voter', 'vouch', 'vying', 'wacky', 'waltz', 'wagon', 'waste', 'watch', 'weary', 'wedge', 'weird', 'whack', 'whale', 'wheel', 'whelp', 'where', 'which', 'whiff', 'while', 'whine', 'whiny', 'whirl', 'whisk', 'whoop', 'widen', 'wince', 'windy', 'witch', 'woken', 'woman', 'wooer', 'wordy', 'world', 'worry', 'worse', 'worst', 'would', 'woven', 'wrath', 'wreak', 'wrist', 'write', 'wrong', 'wrote', 'wrung', 'yacht', 'yearn', 'yield', 'young', 'youth', 'zebra', 'zesty']
	word_choice = words[random.randint(0, len(words) - 1)]
	word_as_list = []
	for i in range(len(word_choice)):
		word_as_list += [word_choice[i]]

	response = []
	for i in range(len(word_choice)):
		response += ["_"]

	print("Word: " + to_str_w_space(response))

	guesses = 5
	while guesses > 0:
		answer = input("Guess: ")
		answer_as_list = []
		for i in range(len(answer)):
			answer_as_list += [answer[i]]

		if word_as_list == answer_as_list:
			print("Word: Correct!")
			break

		guesses -= 1
		if len(answer) != len(word_choice):
			guesses += 1
			continue

		comp_list = word_as_list[:]
		for i in range(len(word_as_list)):
			if word_as_list[i] == answer_as_list[i]:
				response[i] = word_as_list[i]
				comp_list[i] = "/"

		for i in range(len(word_as_list)):
			if answer_as_list[i] in comp_list and response[i] == "_":
				idx = lin_search(comp_list, answer_as_list[i])
				response[i] = "*"
				comp_list[i] = "/"

		if guesses == 0:
			print("Word: " + word_choice)
			break

		print("Word: " + to_str_w_space(response))

#AF Problem 1
def carnival_up_and_down():
	carnival = acsp.load_song("carnival.wav")

	for i in range(1, 281):
		start = 48000 * (i - 1)
		end = 48000 * i
		segment = carnival[start:end]

		if not i % 2:
			for j in range(len(segment)):
				segment[j] *= 1.5
		else:
			for j in range(len(segment)):
				segment[j] *= 0.5

		carnival[start:end] = segment

	acsp.save_song("carnival_up_and_down_p1.wav", carnival)

#AF Problem 2
def carnival_mute_10s():
	carnival = acsp.load_song("carnival.wav")
	for i in range(480000):
		carnival[i] = 0
	acsp.save_song("carnival_mute_10s_p2.wav", carnival)

#AF Problem 3
def carnival_10s_backwards():
	carnival = acsp.load_song("carnival.wav")

	cut = carnival[:480001]
	carnival = carnival[480001:]

	rev_cut = acsp.load_song("carnival.wav")[:1]
	for i in range(len(rev_cut)):
		rev_cut.pop()

	for i in range(len(cut) - 1, -1, -1):
		rev_cut += [cut[i]]

	carnival = rev_cut + carnival

	acsp.save_song("carnival_10s_backwards_p3.wav", carnival)

#AF Problem 4
def ramp_up_volume():
	carnival = acsp.load_song("carnival.wav")
	vol_mul = 0
	for i in range(len(carnival)):
		carnival[i] *= vol_mul
		vol_mul += 1 / len(carnival)
	acsp.save_song("carnival_ramp_up_volume_p4.wav", carnival)

#AF Problem 5
def no_chorus():
	carnival = acsp.load_song("carnival.wav")
	res = acsp.load_song("carnival.wav")
	for i in range(len(res)):
		res.pop()

	res += carnival[624000:3072000]
	res += carnival[3696000:7152000]
	res += carnival[7824000:11520000]
	res += carnival[12096000:]
	carnival = res

	acsp.save_song("carnival_no_chorus_p5.wav", res)

#AF Problem 6
def triad_CEG():
	C = acsp.load_song("C.wav")
	E = acsp.load_song("E.wav")
	G = acsp.load_song("G.wav")

	combined = C.copy()
	for i in range(len(C)):
		combined[i] = C[i] + E[i] + G[i]

	acsp.save_song("triad_CEG_p6.wav", combined)
#End AF Problem 6

def lim_list(song):
	for i in range(len(song)):
		if song[i] > 32767:
			song[i] = 32767
		elif song[i] < -32768:
			song[i] = -32768
	return song

#AF Problem 7
def triad_ACE():
	A = acsp.load_song("A.wav")
	C = acsp.load_song("C.wav")
	E = acsp.load_song("E.wav")

	combined = A.copy()
	for i in range(len(A)):
		combined[i] = A[i] + C[i] + E[i]

	combined = lim_list(combined)

	acsp.save_song("triad_ACE_p7.wav", combined)

#AF Problem 8
def bass_boosted_and_sped_up():
	carnival = acsp.load_song("carnival.wav", True)
	carnivalL = carnival[0]
	carnivalR = carnival[1]

	acsp.set_song_frequency(carnivalL, 56112)
	acsp.set_song_frequency(carnivalR, 56112)

	acsp.goto_freq_domain(carnivalL)
	acsp.goto_freq_domain(carnivalR)

	dataL = acsp.get_frequency_data(carnivalL)
	dataR = acsp.get_frequency_data(carnivalR)

	freqL = dataL[0]
	amplL = dataL[1]
	freqR = dataR[0]
	amplR = dataR[1]

	for i in range(len(freqL)):
		if 0 < freqL[i] < 150:
			carnivalL[i] *= 3.5
	for i in range(len(freqR)):
		if 0 < freqR[i] < 150:
			carnivalR[i] *= 3.5

	acsp.goto_time_domain(carnivalL)
	acsp.goto_time_domain(carnivalR)

	carnivalL = lim_list(carnivalL)
	carnivalR = lim_list(carnivalR)

	acsp.save_song("carnival_bass_boosted_and_sped_up_p8.wav", carnivalL, carnivalR)