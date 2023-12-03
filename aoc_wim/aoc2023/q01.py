"""
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
"""
import regex as re
from aocd import data, submit


ns = "one, two, three, four, five, six, seven, eight, nine".split(", ")
d = dict(zip(ns, "123456789"))
a = b = 0
pat_b = re.compile(rf"(\d|{'|'.join(ns)})")
for line in data.splitlines():

    nums_a = []
    for c in line:
        if c in "0123456789":
            nums_a.append(int(c))

    nums_b = [int(d.get(x, x)) for x in pat_b.findall(line, overlapped=True)] or [0]
    a += nums_a[0] * 10 + nums_a[-1]
    b += nums_b[0] * 10 + nums_b[-1]

print("answer_a:", a)
print("answer_b:", b)
submit(a, part="a", day=1, year=2023)
submit(b, part="b", day=1, year=2023)

