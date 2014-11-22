#does semantic analysis to predict words
import string
from nltk.corpus import framenet as fn
#from pyspark import SparkContext

def parGetFrame(lemma):
    frame = fn.frames_by_lemma("donkey")
    if frame != []:
        f = frame.pop()
        return 'asdf'
    else:
        return 'asdfasd'

def getFrames(phrase):
    frames = []
    content = [s.translate(string.maketrans("",""), string.punctuation) for s in phrase.split()]
    for lemma in content:
        frame = fn.frames(lemma)
        if frame != []:
            frames.append([f.name for f in frame])
    return frames

def getSuggestion(sentence):
    pass

if __name__ == "__main__":
	text = "The pizza delivery man was very rude. I am not going to give him a."
	f = getFrames(text)
	d = {}
	d_rev = {}
	for frame_list in f:
		for frame in frame_list:
			if frame not in d:
				d[frame] = 1
			else:
				d[frame] += 1
	for k in d.keys():
		if d[k] not in d_rev:
			d_rev[d[k]] = [k]
		else:
			d_rev[d[k]].append(k)
	biggest = max(d_rev.keys())
	print d_rev[biggest]
