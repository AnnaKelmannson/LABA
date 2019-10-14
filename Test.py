import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import re
import math as m
import cmath as cm


class Measurement:
    def __init__(self, current, potential, color):
        self.current = list(map(float, current.split(',')))
        self.potential = list(map(float, potential.split(',')))
        try:
            self.resistance = [self.potential[j] / self.current[j] for j in range(len(self.current))]
        except ZeroDivisionError:
            self.resistance = None
            pass
        self.color = color


with open(r'C:\Users\Georg The Great\Desktop\01-10-2019_NiMeOSalTmen_LiBF4_AN-RT-50.mtc', 'r') as file:
    text = file.read()
    currents = re.findall(r'<i1>(.+?)</i1>', text)
    potentials = re.findall(r'<potential>(.+?)</potential>', text)
    colors = re.findall(r'<color>(.+?)</color>', text)
    measurements = [0] * len(currents)
    for i in range(len(currents)):
        measurements[i] = Measurement(currents[i], potentials[i], colors[i])
    pass


