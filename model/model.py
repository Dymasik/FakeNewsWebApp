import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from os import path


MODEL_PATH = path.join(path.dirname(path.abspath(__file__)), "model.h5")
MAX_LEN = 64
MODEL = tf.keras.models.load_model(MODEL_PATH)


def predict(text: str) -> float:
    tokenizer = Tokenizer()
    sequences = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(sequences, maxlen=MAX_LEN)
    prediction = MODEL.predict(pad)
    return prediction[0][0]