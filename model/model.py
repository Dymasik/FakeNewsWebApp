from typing import Any
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


MAX_LEN = 64


def predict(model: Any, tokenizer: Tokenizer, text: str) -> float:
    sequences = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(sequences, maxlen=MAX_LEN)
    prediction = model.predict(pad)
    return prediction[0][0]