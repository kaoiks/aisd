import math
from os import stat
import sys
import operator
from generator import generate
from algos.greedy import greedy
from algos.dynamic import dynamic





def main():
    # file = open("plecak.txt")

    # n = int(file.readline().split(" - ")[0]) #liczba kontenerow
    # sizes = [int(x) for x in file.readline().split(" - ")[0].split(" ")] #wagi
    # values = [int(x) for x in file.readline().split(" - ")[0].split(" ")] #wartosc
    # b = int(file.readline().split(" - ")[0]) #ladownosc statku
    # kontenery = []
    # #wagi=[]
    # for i in range(n):
    #     kontener = [sizes[i],values[i]]
    #     kontenery.append(kontener)

    b = 100
    kontenery = generate(b, 5*b, 10)
    n = len(kontenery)

    greedy_ship = greedy(kontenery,n,b)
    dynamic_ship = dynamic(kontenery,n,b)

    print("Zachłanny: ", greedy_ship)
    print(count_value(greedy_ship))
    print("Dynamiczny", dynamic_ship)
    print(count_value(dynamic_ship))

def count_value(containers):
    total = 0
    for cont in containers:
        total += cont[1]
    return total

main()