def hririak_ordenatzen (hiriak):
    for x in hiriak.values() :
        if x >= 200000:
          gehiagokoen_zerrenad = [len(hiriak)]
          gehiagokoen_zerrenad[x] = hiriak.keys()

    print(gehiagokoen_zerrenad)


gure_hriak = dict(Bilbo = 200800, Donostia = 100000, Irueñea = 203000)

hririak_ordenatzen( gure_hriak)