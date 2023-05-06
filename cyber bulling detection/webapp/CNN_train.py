import time
import pickle
import tensorflow as tf
import pandas as pd
import tqdm
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.model_selection import train_test_split
#from tensorflow.keras.layers import Embedding, Dropout, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.metrics import Recall, Precision
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D, Dropout, Dense, Input, Embedding, MaxPooling1D, Flatten

SEQUENCE_LENGTH = 100 # the length of all sequences (number of words per sample)
EMBEDDING_SIZE = 100  # Using 100-Dimensional GloVe embedding vectors
TEST_SIZE = 0.25 # ratio of testing set

BATCH_SIZE = 64
EPOCHS = 10 # number of epochs


def load_data():
    data = pd.read_csv("cyberbullying_tweets.csv")
    texts = data['tweet_text'].values
    labels=data['cyberbullying_type'].values
    return texts, labels



def model():
    print("loading data")
    X, y = load_data()
    # Text tokenization
    # vectorizing text, turning each text into sequence of integers
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X)
    # lets dump it to a file, so we can use it in testing
    pickle.dump(tokenizer, open("tokenizer.pickle", "wb"))
    # convert to sequence of integers
    X = tokenizer.texts_to_sequences(X)


    # convert to numpy arrays
    X = np.array(X)
    y = np.array(y)
    # pad sequences at the beginning of each sequence with 0's
    # for example if SEQUENCE_LENGTH=4:
    # [[5, 3, 2], [5, 1, 2, 3], [3, 4]]
    # will be transformed to:
    # [[0, 5, 3, 2], [5, 1, 2, 3], [0, 0, 3, 4]]
    X = pad_sequences(X, maxlen=SEQUENCE_LENGTH)

    # One Hot encoding labels
    # [spam, ham, spam, ham, ham] will be converted to:
    # [1, 0, 1, 0, 1] and then to:
    # [[0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]



    # split and shuffle
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=7)
    # print our data shapes
    print("X_train.shape:", X_train.shape)
    print("X_test.shape:", X_test.shape)
    print("y_train.shape:", y_train.shape)
    print("y_test.shape:", y_test.shape)


    def get_embedding_vectors(tokenizer, dim=100):
        embedding_index = {}
        with open(f"data/glove.6B.{dim}d.txt", encoding='utf8') as f:
            for line in tqdm.tqdm(f, "Reading GloVe"):
                values = line.split()
                word = values[0]
                vectors = np.asarray(values[1:], dtype='float32')
                embedding_index[word] = vectors

        word_index = tokenizer.word_index
        embedding_matrix = np.zeros((len(word_index) + 1, dim))
        for word, i in word_index.items():
            embedding_vector = embedding_index.get(word)
            if embedding_vector is not None:
                # words not found will be 0s
                embedding_matrix[i] = embedding_vector

        return embedding_matrix
    print("EMD Matrix")
    embedding_matrix = get_embedding_vectors(tokenizer)
    print("Starting...")



    model = Sequential()
    model.add(Embedding(len(tokenizer.word_index) + 1,
                        EMBEDDING_SIZE,
                        weights=[embedding_matrix],
                        trainable=False,
                        input_length=SEQUENCE_LENGTH))
    model.add(Conv1D(128,5,activation='relu'))
    model.add(GlobalMaxPooling1D())
    model.add(Dense(6, activation="softmax"))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

    model.fit(X_train, y_train, epochs=6, verbose=1, validation_data=(X_test, y_test), batch_size=4)
    model.save('cnn_model.model')


#model()