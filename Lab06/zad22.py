produkty1 = ["RAM", "banan", "smoothie", "zupa"]
produkty2 = ["jabol", "banan", "gruszka", "lód"]

zbior1 = set(produkty1)
zbior2 = set(produkty2)

only_1 = zbior1 - zbior2
only_2 = zbior2 - zbior1
both = zbior1 & zbior2

print("Tylko w 1:", only_1)
print("Tylko w 2:", only_2)
print("tu i tu:", both)
