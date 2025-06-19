import tensorflow as tf
import tensorflowjs as tfjs

model = tf.keras.models.load_model("D:/AI_Virtual_Dressing_Room/model/mobilenetv2_legacy.h5", compile=False)

# Convert to TensorFlow.js format
tfjs.converters.save_keras_model(model, "D:/AI_Virtual_Dressing_Room/web_model/")
print("Model successfully converted to TensorFlow.js format!")
