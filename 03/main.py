

def get_substr(s: str):
    st = s
    subs = []
    while True:
        sub = ''
        for i in st:
            if i in sub:
                st = st[1:]
                break
            sub += i
        if len(subs) > 2 and sub == subs[-2]:
            break
        subs.append(sub)
    # return subs
    return max([len(su) for su in subs])


# sts = ["abcabcbb", "bbbbb", "pwwkew",
#        "abcdcdasds", "dvdf", "bbbc", "lursenhsaqzomihhopmfffywxjxnbsgonzitmqloilduvkblansfvqdubahcupshobccrqrzd"]

# for st in sts:
#     print('result:  ', get_substr(st))


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def get_substr(st: str):
#     sl = list(st)
#     ss = sorted(set(st), key=lambda i: sl.index(i))
#     sss = ''.join(ss)
#     if sss in st:
#         return sss
#     ssf = sss
#     while ssf not in st and ssf:
#         ssf = ssf[1:]
#     ssl = sss
#     while ssl not in st and ssl:
#         ssl = ssl[:-1]
#     return ssf if len(ssf) > len(ssl) else ssl

# print(get_substr('dvdf'))

#
