import matplotlib.pyplot as plt
import numpy as np
# from keras.datasets import imdb

# (train_data, train_labels),(test_data, test_labels) = imdb.load_data(num_words=10000)
# print(train_data[:10])
# print(train_labels[:10])

def vectorize_sequences(sequences, dimension=10):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results
training_labels = [0,1,0]
training_data = [list([5,5,8,4,2,1,4]),
                 list([3,4,6,7,2]),
                 list([1,9,8,6,4,6,3,7,4,3])]
print(training_data[:2])
test = vectorize_sequences(training_data)
print(test[:1])
test_label = vectorize_sequences(training_labels)
print(test_label)
# plt.matshow(test)
# plt.show()
