

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'val: {self.val}, next: {self.next}'


def main(l1, l2):
    ls1 = ''
    ls2 = ''
    for i in l1:
        ls1 = str(i)+ls1
    for i in l2:
        ls2 = str(i)+ls2
    ls1 = int(ls1)
    ls2 = int(ls2)
    ls = list(str(ls1+ls2))
    ls = [int(l) for l in ls]
    ls.reverse()
    return ls


def get_list(l1):
    count = 0
    nxt = l1
    prob = [nxt]
    while True:
        count += 1
        nxt = nxt.next
        if not nxt or count > 5:
            break
        prob.append(nxt)
    ls = [x.val for x in prob]
    return ls


def set_list(l1, rev=False):
    ln = []
    for l in l1:
        ln.append(ListNode(l))
    if rev:
        ln.reverse()
    n1 = ln[0]
    count = 0
    for n in ln:
        if count == 0:
            count += 1
            continue
        n.next = n1
        n1 = n
    return ln[-1]


x1 = ListNode(2, ListNode(4, ListNode(3)))
x2 = ListNode(5, ListNode(6, ListNode(4)))
y = set_list(main(get_list(x1), get_list(x2)))

print(y)
