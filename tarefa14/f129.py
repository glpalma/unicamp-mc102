from fatorial import fatorial
from math import e, sqrt, pi

def main():
    #prob = (fatorial(100)/(fatorial(20) * fatorial(80)) * ((1/4) ** 20) * ((3/4) ** 80))
    #poisson = (((25 ** 20)/fatorial(20)) * (e ** (-25)))
    normal = (1/(5 * sqrt(2 * pi))) * e ** (-((20-25) ** 2) / 50)
    #print(prob)
    print(normal)

main()