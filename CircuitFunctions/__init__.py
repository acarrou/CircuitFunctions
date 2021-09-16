import numpy as np


def KCL(*Currents):
    """
    KCL (Calculates Kirchhoff's Current Law with voltages given)

    :param flaot Currents: The currents given
    """
    if sum(Currents) == 0:
        print("These currents equal 0")
    print("The total current does not equal 0")
    print(sum(Currents))


def KVL(*Voltages):
    """
    KVL (Calculates Kirchhoff's Voltage Law with voltages given)

    :param flaot Voltages: The voltages given
    """
    if sum(Voltages) == 0:
        print("These currents equal 0")
    print("The total voltages does not equal 0")
    print(sum(Voltages))


def findVoltage(Current, Resistance):
    """
    findVoltage (Calculates voltage from current and resistance)

    :param flaot Current: The current given
    :param float Resistance: The resistance given
    """
    print("Voltage:", Current*Resistance)


def findCurrent(Voltage, Resistance):
    """
    findCurrent (Calculates current from voltage and resistance)

    :param flaot Voltage: The voltage given
    :param float Resistance: The resistance given
    """
    print("Current:", Voltage/Resistance)


def findResistance(Voltage, Current):
    """
    findResistance (Calculates resistance from voltage and current)

    :param flaot Voltage: The voltage given
    :param float Current: The current given
    """
    print("Resistance:", Voltage/Current)


def findPower(Voltage, Current):
    """
    findPower (Calculates power from voltage and current)

    :param flaot Voltage: The voltage given
    :param float Current: The current given
    """
    print("Power", Voltage*Current)


def MatrixMult(Vector, *Matrix):
    """
    MatrixMult (Matrix Multiplication with a vector and main matrix to compute)

    :param array/list Vector: The sum of each equation/vector
    :param array/list Matrix: The matrix to be multiplied by the vector
    """
    V = np.array(Vector)
    M = np.array(Matrix)
    final = np.linalg.lstsq(M, V, rcond=None)
    print("Answer: ", final[0])


def findSerRes(*SerResis):
    """
    findSerRes (Finds the sum of all resistors in series)

    :param float SerResis: All resistors in series to compute sum
    """
    print("Total Resistance in Series: ", sum(SerResis))


def findParRes(*ParResis):
    """
    findParRes (Finds the sum of all resistors in parallel)

    :param float ParResis: All resistors in parallel to compute sum
    """
    final = 0
    for item in ParResis:
        final = (1/item) + final
    print("Total Resistance in Parallel: ", (1/final))


def findParSpecRes(R1, R2):
    """
    findParSpecRes (Find the parallel resistance of two resistors)

    :param float R1: Resistor R1
    :param float R2: Resistor R2
    """
    print("Total Parallel Resistance of R1 and R2: ", (R1*R2)/(R1+R2))


def VoltageDiv(Voltage_Source, Resistor, *allResistors):
    """
    VoltageDiv (Voltage Divider)

    :param float Voltage_Source: The Voltage Source
    :param float Resistor: The main resistor we want to find
    :param float allResistors: All of the resistors
    """
    print("Total Voltage Division: ", Voltage_Source*(Resistor/sum(allResistors)))


def CurrentDiv(Current_Source, Resistor, *allResistors):
    """
    CurrentDiv (Current Divider)

    :param float Current_Source: The Current Source
    :param float Resistor: The main resistor we want to find
    :param float allResistors: All of the resistors
    """
    final = 0.0
    for item in allResistors:
        final = 1/item + final
    print("Total Current Division: ", Current_Source*((1/Resistor)/(final)))



