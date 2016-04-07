import random

def test(times, percent, obsize):
    observations = [0] * obsize
    random.seed(10)

    for i in range(0,times):
        int1 = percent * obsize
        int2 = obsize
        for j in range (0, obsize):
            next = int1/int2
            rand = random.random()
            if rand < next:
                observations[j] += 1
                int1 = int1 - 1
            int2 = int2 - 1

    return observations



with open('abalone.txt') as linetext:
    text = linetext.readlines()

lines = len(text)
print (lines)

print(test(10, 0.1, 100))