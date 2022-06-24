from main import get_substr


sts = ["abcabcbb", "bbbbb", "pwwkew",
       "abcdcdasds", "dvdf", "dtdztwhepnkguuuowsxztrmivgdyiw",
       "lursenhsaqzomihhopmfffywxjxnbsgonzitmqloilduvkblansfvqdubahcupshobccrqrzd"]

sns = [3, 1, 3, 4, 3, 14, 11]
# sas = ["abc", "b", "wke", "abcd", "vdf", "", ""]


def test():
    for st, sa in zip(sts, sns):
        assert get_substr(st) == sa
