#coding: utf-8


def task02(string1, string2): return "".join(s1+s2 for s1, s2 in zip(string1, string2))

if __name__ == "__main__":
    in_string1 = u"パトカー"
    in_string2 = u"タクシー"
    output = task02(in_string1, in_string2)
    print(output)
