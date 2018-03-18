# Maxime Coutté, check my Github: maximecoutte, Twitter: maximecoutte
# Contain Gradiant descent stuff and Artifical neuron too

import math
import random

ACCURACY = 0.1

def MatrixVector_multiplication(vector, matrix):
    """ N dimensional. Return an Array as a Vector resulting from vector * matrix """
    result_vector = []

    for i in range(0, len(matrix[0])):
        element = 0
        for j in range(0, len(matrix)):
            element += matrix[j][i] * vector[j]
        result_vector.append(element)

    return result_vector

def VectorVector_additon(vectorA, vectorB):
    """ N diemnsional. Return an array as a vector resulting from vectorA + vectorB"""
    result_vector = []
    for i in range(0,len(vectorA)):
        result_vector.append(vectorA[i] + vectorB[i])

    return result_vector

def VectorVector_soustraction(vectorA, vectorB):
    """ N diemnsional. Return an array as a vector resulting from vectorA - vectorB"""
    result_vector = []
    for i in range(0,len(vectorA)):
        result_vector.append(vectorA[i] - vectorB[i])

    return result_vector

def VectorVector_scalar(vectorA, vectorB):
    """ N diemnsional. Return a float as a scalar resulting from vectorA * vectorB"""
    result = 0
    for i in range(0, len(vectorA)):
        result += vectorA[i] * vectorB[i]
    return result

def linear_hypothesis(matrix, vector):
    """ Linear hypothesis, just a vector-matrix multiplication. Return an Array as a Vector resulting from vector * matrix """
    return MatrixVector_multiplication(vector, matrix)

def cost_hypothesis(data, parameter, hypothesis):
    """ cost of the hypothesis for the given data"""
    m = len(data[0]) #Number of dataset's exemples

    unit_vector = [] # [1,1,1,1,1,...,m]
    for i in range(0, m):
        unit_vector.append(1)

    error = VectorVector_soustraction(hypothesis([unit_vector, data[0]], parameter) , data[1])

    squared_sum_error = 0

    for scalar in error:
        squared_sum_error += scalar ** 2

    return (1/(2*m))*squared_sum_error

def gradiant_descent_linear_hypothesis_2D(data, hypothesis):
    """ Perform a Gradiant descent, return theta0 and theta1 """

    theta0 = 0
    theta1 = 0

    m = len(data[0]) #Number of dataset's exemples

    unit_vector = [] # [1,1,1,1,1,...,m]
    for i in range(0, m):
        unit_vector.append(1)

    for i in range(0,100):
        error = VectorVector_soustraction(hypothesis([unit_vector, data[0]], [theta0, theta1]) , data[1])

        sum_error_theta0 = 0
        sum_error_theta1 = 0

        for i in range(0, len(error)):
            sum_error_theta0 = sum_error_theta0 + error[i]
            sum_error_theta1 = sum_error_theta1 + error[i] * data[0][i]

        theta0 = theta0 - (ACCURACY * (1/m) * sum_error_theta0)
        theta1 = theta1 - (ACCURACY * (1/m) * sum_error_theta1)

    return ([theta0, theta1])

def sigmoid(x):
    return 1/(1 + math.exp(-x))

class Neuron():
    """docstring for Neuron."""
    def __init__(self, activation_function):
        self.activation_function = activation_function
        self.weight = []

    def adjust_weight(self, weight):
        self.weight = weight

    def weight(self):
        return self.weight

    def compute(self, input_signal):
        return self.activation_function(VectorVector_scalar(input_signal, self.weight))

def train_Neuron_linear_classifier_2D(neuron, database):

    score = 0
    while (score < 11):
        score = 0
        neuron.adjust_weight([random.random() ,random.random()])

        output = 0.5
        for i in range(0, len(database[0])):

            if (neuron.compute([database[0][i],database[1][i]]) > 0.5):
                output = 1
            else:
                output = 0

            if (output == database[2][i]):
                score += 1

    return neuron

# Test database
database = [[1,3,5,7,5,9,10,11,5,7,3,8,10,14,1],[2,4,5,4,3,6,4,6,-1,1,-2,-2,1,3,-5],[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]]

neuron1 = Neuron(sigmoid)

hypothesis = train_Neuron_linear_classifier_2D(neuron1, database)

print(hypothesis.compute([11,-2]))
