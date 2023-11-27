import numpy as np

class Perceptron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        # Aplica a função degrau para determinar a saída
        y_predicted = self.activation_function(linear_output)
        return y_predicted

def main():
    perceptron = Perceptron(weights=[0.3, 0.5, 0.2], threshold=1)

    weather = float(input("Is the weather good? (1/0): "))
    company = float(input("Does my girlfriend/boyfriend want to accompany me? (1/0): "))
    transport = float(input("Is the festival near public transport? (1/0): "))

    inputs = np.array([weather, company, transport])

    y_predicted = perceptron.predict(inputs)

    print("Do I want to go to the festival? {}".format(y_predicted))

if __name__ == "__main__":
    main()