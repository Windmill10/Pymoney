def GenF():
    print("Genf")
    a = yield 1
    print("a = ", a)
    c = yield 2

def GenG():
    print("GenG")
    f = GenF()
    print("Generated f")
    h = next(f)
    print(h)
    i = f.send('c')

GenG()