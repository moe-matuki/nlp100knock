 
#!/usr/bin/python
# coding: UTF-8

from collections import Counter
import matplotlib.pyplot as plt

def readlinesFile(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()
	return(lines)

def Morphol(filename):
	import re
	lines = readlinesFile(filename)

	result = list()
	mecabbinfos = list()
	infokeys = ["surface", "pos", "pos1", "pos2", "pos3", "ctype", "cform", "base", "kana", "yomi"]
	for line in lines:
		line = line.strip("\n")

		if line == "EOS":
			if line != []:
				result.append(mecabbinfos)
				mecabbinfos = list()

		else:
			infovalues = re.split("\t|,", line)
			infodicts = dict(zip(infokeys, infovalues))
			#getinfodicts = dict((k, v) for k, v in infodicts.items() if k in getinfos)
			mecabbinfos.append(infodicts)

	return result


if __name__ == "__main__":
	filename = "neko.txt.mecab"
	output = Morphol(filename) 
	base_list = [dist["base"] for dists in output for dist in dists]

	counter = Counter(base_list)
	countdict =  counter.most_common()
	cnts, freqs = zip(*counter.most_common())
	X, Y = range(len(cnts)), freqs
	plt.plot(X, Y)
	plt.xscale('log')
	plt.yscale('log')
	plt.show()