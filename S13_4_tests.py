from S13_4 import *

#print(analyser_ressource([],[]))
print(analyser_ressource([0],[0]))
print(analyser_ressource([89, 90, 91],[90,89,91]))
print(analyser_ressource([0],[0,1]))
print(analyser_ressource([101],[0]))
print(analyser_ressource([0],[-1]))
#print(analyser_ressource(["allo"],[0]))
print(analyser_ressource([0.5, 0.7],[0.7, 0.5]))
print(analyser_ressource(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
print(analyser_ressource([91, 92],[0, 0]))
print(analyser_ressource([0, 0], [91, 92]))