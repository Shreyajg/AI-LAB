def vacumCleaner(clean):
    for i in range(0, 4):
        if not clean[i]:
            clean[i] = 1
            print("cleaning room",i)
        else:
            print("room ",i,"is clean")
    print("Anticlockwise check")
    for i in range(3, -1, -1):
        if not clean[i]:
            clean[i] = 1
        else:
            print("room", i, "is clean")

clean = [0, 0, 1, 0]
