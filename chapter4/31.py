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

def select(output, getinfos):
	result = list()
	infodicts = output
	for infodict in infodicts:
		for word in infodict: 
			getinfodicts = dict((k, v) for k, v in word.items() if k in getinfos)
			result.append(getinfodicts)
	return result

def verbSelect(posfile):
	result = list()
	for dist in posfile:
		if dist["pos"] == "動詞":
			getinfodicts = dist["surface"]
			result.append(getinfodicts)
	return result


if __name__ == "__main__":
	filename = "neko.txt.mecab" #読み込むファイル名
	getinfos = ["surface","pos"] #欲しい辞書のkey
	output = Morphol(filename) #1行毎に辞書型になったリストを返す
	posfile = select(output, getinfos) #単語と品詞の書かれた単語の辞書のリスト

	for i in verbSelect(posfile):
		print(i)



