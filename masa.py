def kilogramos_a_gramos(kilogramos):
    return kilogramos *1000

def kilogramos_a_toneladas(kilogramos):
    return kilogramos /1000

def toneladas_a_(toneladas):
    return toneladas *1000

if __name__=="__main__":
    kilogramos= 2.5
    gramos= kilogramos_a_gramos(kilogramos)
    print(f"{kilogramos} kilogramos son equivalentes {gramos} gramos")