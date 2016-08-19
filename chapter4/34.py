#!/usr/bin/python
# coding: UTF-8

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

def numPhrases(output):
	result = list()

	for dists in output:
		for n in range(len(dists)-2):
			w0 = dists[n]
			w1 = dists[n + 1]
			w2 = dists[n + 2]
			if(w0["pos"] == "名詞" and w1["pos"] == "助詞" and w2["pos"] == "名詞"):
				if(w0["base"] != "*" and w1["base"] == "の" and w2["base"] != "*"):
					result.append(w0["base"] + w1["base"] + w2["base"])

	return result


if __name__ == "__main__":
	filename = "neko.txt.mecab" #読み込むファイル名
	output = Morphol(filename) #1行毎に辞書型になったリストを返す
	numPhrases = numPhrases(output) #名詞の名詞を全て抽出する

	for i in numPhrases:
		print(i)

