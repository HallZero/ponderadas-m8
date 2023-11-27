import numpy as np

data = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
and_labels = np.array([[0],[0],[0],[1]])
or_labels = np.array([[0],[1],[1],[1]])
xor_labels = np.array([[0],[1],[1],[0]])

class Perceptron:
    def __init__(self, weights, threshold, learning_rate=0.1, n_iterations=100):
        self.weights = np.array(weights)
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        # Aplica a função degrau para determinar a saída
        y_predicted = self.activation_function(linear_output)
        return y_predicted
    
    def train(self, training_inputs, labels):
        for _ in range(self.n_iterations):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights += self.learning_rate * (label - prediction) * inputs
                self.bias += self.learning_rate * (label - prediction)
    
def main():
    perceptron = Perceptron(weights=[0.25, 0.25], threshold=0.5)

    perceptron.train(data, xor_labels)

    print(perceptron.predict([1, 1]))
    

if __name__ == '__main__':
    main()