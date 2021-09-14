import numpy as np


def KCLcheck(*Currents):
    if sum(Currents) == 0:
        print("These currents equal 0")
    print("The total current does not equal 0")
    print(sum(Currents))

def KVLcheck(*Voltages):
    if sum(Voltages) == 0:
        print("These currents equal 0")
    print("The total voltages does not equal 0")
    print(sum(Voltages))

def findVoltage(Current, Resistance):
    print("Voltage:", Current*Resistance)

def findCurrent(Voltage, Resistance):
    print("Current:", Voltage/Resistance)

def findResistance(Voltage, Current):
    print("Resistance:", Voltage/Current)

def findPower(Voltage, Current):
    print("Power", Voltage*Current)

def MatrixMult(Vector, *Matrix):
    V = np.array(Vector)
    M = np.array(Matrix)
    final = np.linalg.lstsq(M, V, rcond=None)
    print("Answer: ", final[0])

def findSerRes(SerResis):
    print("Total Resistance in Series: ", sum(SerResis))

def findParRes(*ParResis):
    print(type(ParResis))
    final = 0
    for item in ParResis:
        final = (1/item) + final
    print("Total Resistance in Parallel: ", (1/final))

def findParSpecRes(R1, R2):
    print("Total Parallel Resistance of R1 and R2: ", (R1*R2)/(R1+R2))


