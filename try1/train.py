import numpy as np
import matplotlib.pyplot as plt
import argparse
from perceptron import Perceptron

def main(args):
    # AND gate input and target output
    X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
    Y = np.array([1, 1, 1, 0])

    # Initialize the Perceptron model
    model = Perceptron(input_size=2, learning_rate=args.learning_rate, epochs=args.epochs)

    # Train the model
    model.train(X, Y)

    # Test the model
    predictions = model.predict(X)
    print('Predicted outputs:')
    print(predictions)

    # Print the learned weights and bias
    print('Weights:', model.weight)
    print('Bias:', model.bias)

    # Plot the error graph
    plt.plot(range(model.epochs), model.error)
    plt.xlabel('Epoch')
    plt.ylabel('Total Error')
    plt.title('Error vs. Epoch')
    plt.savefig(args.output_file)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a Perceptron for the AND gate.')
    parser.add_argument('--learning_rate', type=float, default=0.1, help='Learning rate for the perceptron')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train the perceptron')
    parser.add_argument('--output_file', type=str, default='mse_plot.png', help='Filename to save the plot image')  
    args = parser.parse_args()
    main(args)
