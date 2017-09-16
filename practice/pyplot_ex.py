import matplotlib.pyplot as plt
import numpy as np
# from keras.datasets import imdb

# (train_data, train_labels),(test_data, test_labels) = imdb.load_data(num_words=10000)
# print(train_data[:10])
# print(train_labels[:10])

# def vectorize_sequences(sequences, dimension=10):
#     results = np.zeros((len(sequences), dimension))
#     for i, sequence in enumerate(sequences):
#         results[i, sequence] = 1.
#     return results

train_targets = [10,11,12,13,14,15,16,17,18,19,20,21]
train_data = [[0,5,8,4,2,1,4,8,6,4,3,2],
              [1,4,6,7,2,3,6,3,2,1,4,2],
              [2,4,6,7,2,3,6,3,2,1,4,2],
              [3,4,6,7,2,3,6,3,2,1,4,2],
              [4,4,6,7,2,3,6,3,2,1,4,2],
              [5,4,6,7,2,3,6,3,2,1,4,2],
              [6,4,6,7,2,3,6,3,2,1,4,2],
              [7,4,6,7,2,3,6,3,2,1,4,2],
              [8,4,6,7,2,3,6,3,2,1,4,2],
              [9,4,6,7,2,3,6,3,2,1,4,2],
              [10,4,6,7,2,3,6,3,2,1,4,2],
              [11,9,8,6,4,6,3,7,4,3,4,3]]
k = 4
num_val_samples = len(train_data) // k
print(num_val_samples)
num_epochs = 100
all_scores = []
for i in range(k):
    print('processing fold #', i)
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    # val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]

    a = np.array(train_data[:i * num_val_samples]).reshape(i * num_val_samples,12)
    b = np.array(train_data[(i+1) * num_val_samples:]).reshape((k-i-1) * num_val_samples, 12)
    print(a.shape)
    print(b.shape)
    partial_train_data = np.concatenate(
         [np.array(train_data[:i * num_val_samples]).reshape(i * num_val_samples, 12),
         np.array(train_data[(i+1) * num_val_samples:]).reshape((k-i-1) * num_val_samples, 12)],
        axis=0)
    print('partial train data')
    print(partial_train_data)
# print(training_data[:2])
# test = vectorize_sequences(training_data)
# print(test[:3])
# test_label = vectorize_sequences(training_labels)
# print(test_label)
# plt.matshow(test)
# plt.show()
