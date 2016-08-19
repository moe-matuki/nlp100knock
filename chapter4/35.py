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

def n_succession(output):
	n_succ = list()
	L = 1

	for dists in output:
		for dist in dists:
			if(dist["pos"] == "名詞" and dist["base"] != "*"):
				n_succ.append(dist["base"])
			else:
				l = len(n_succ)
				if l > 1 :
					if(l > L):
						L = l
						wo = "".join(n_succ)
						result = [L, wo]
						n_succ = list()
	return result





if __name__ == "__main__":
	filename = "neko.txt.mecab" #読み込むファイル名
	getinfos = ["surface","pos", "pos1"] #欲しい辞書のkey
	output = Morphol(filename) #1行毎に辞書型になったリストを返す

	n_succession = n_succession(output) #名詞の連接（連続して出現する名詞）を最長一致で抽出


	for i in n_succession:
		print(i)

