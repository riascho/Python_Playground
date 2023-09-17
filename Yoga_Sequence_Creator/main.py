from random import sample, shuffle
import os

inversions = ["Shoulderstand", "Plough", "Bridge", "Fish","Side Plank","Table Top"]

strength = ["Crow","Chaturanga"]

stretches = ["Konasana",
    "Uttanasana", "Lounge", "Dandasana", "Triangle","Extended Side Angle Pose","Padottanasana","Head-To-Knee"]

backbends = ["Cobra", "Bow", "Wheel", "Camel","King Pigeon"]

twists = ["Matsyendrasana", "Lying Down Spinal Twist", "Table Twist","Torso Sway Twist","Gomukhasana"]

balances = ["Tree", "Dancer", "Half Moon", "Warrior 3","Utkatasana","Garudasana","Boat"]

sequence = sample(inversions,1) + sample(strength,1) + sample(stretches, 2) + sample(
    backbends, 2) + sample(twists, 2) + sample(balances, 2)
shuffle(sequence)

f = open('sequence.txt', 'w')

for i, asana in enumerate(sequence):
  f.write(f'{i+1}\t\t{asana}\n')

f.close()
