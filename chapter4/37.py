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

	result = list() #1文づつのリストを格納
	mecabbinfos = list() #1単語づつの辞書型のリストを格納
	infokeys = ["surface", "pos", "pos1", "pos2", "pos3", "ctype", "cform", "base", "kana", "yomi"]
	for line in lines:
		line = line.strip("\n")

		if line == "EOS":
			if line != []:
				result.append(mecabbinfos)
				mecabbinfos = list()

		else:
			infovalues = re.split("\t|,", line)
			infodicts = dict(zip(infokeys, infovalues)) #keyとvaluseを引っ付ける
			#getinfodicts = dict((k, v) for k, v in infodicts.items() if k in getinfos)
			mecabbinfos.append(infodicts)

	return result


if __name__ == "__main__":
	filename = "neko.txt.mecab" #読み込むファイル名
	output = Morphol(filename) #1行毎に辞書型になったリストを返す
	base_list = [dist["base"] for dists in output for dist in dists]

	counter = Counter(base_list)
	countdict =  counter.most_common()
	words, cnts = zip(*counter.most_common(10)) #？？？
	X, Y = range(len(words)), cnts
	Xlabel = map(lambda x: x.decode("UTF-8"), words)
	plt.bar(X, Y, align="center")
	plt.xticks(X, Xlabel)
	plt.show()


