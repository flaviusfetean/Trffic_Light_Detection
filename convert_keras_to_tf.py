import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("model")

model.save("model.h5")