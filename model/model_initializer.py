import json
from typing import Any, Tuple
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from os import path
from keras.preprocessing.text import tokenizer_from_json


def init_model() -> Tuple[Any, Tokenizer]:
    model_path = path.join(path.dirname(path.abspath(__file__)), "model.h5")
    model = tf.keras.models.load_model(model_path)

    tokenizer_path = path.join(path.dirname(path.abspath(__file__)), "tokenizer.json")
    with open(tokenizer_path) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    return (model, tokenizer)