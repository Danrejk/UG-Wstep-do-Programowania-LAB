listy = [
    [1, 2, 3],
    [10, 20],
    [5, 5, 5, 5],
    [0, 1]
]

najwyzsza = max(listy, key=sum)
najnizsza = min(listy, key=sum)

print("Najwyższa suma:", najwyzsza)
print("Najniższa suma:", najnizsza)
