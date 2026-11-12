B = {"jabłko", "banan", "wiśnia"}

B.discard("gruszka")
print(B)

try:
    B.remove("gruszka")
except KeyError as e:
    print(e)

print("discard usuwa element ze zbioru, a jak dany element nie istnieje, po prostu nic nie robi. remove w przypadku jego braku - wywala errosa.")
