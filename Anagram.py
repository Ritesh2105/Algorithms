s1 = "fairy tales"
s2 = "rail safety"


def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) == len(s2):
        if sorted(s1) == sorted(s2):
            print("Two strings are anagrams")
    else:
        print("Not an anagram")


def anagram_another_way(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) == len(s2):
        ht = dict()
        for i in s1:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        for i in s2:
            if i in ht:
                ht[i] -= 1
            else:
                ht[i] = 1
        for i in ht:
            if ht[i] == 0:
                return print("Two strings are anagram")
    else:
        return print("Not an anagram")


if __name__ == '__main__':
    anagram(s1, s2)
    anagram_another_way(s1, s2)
