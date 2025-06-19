import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Input

# Load the original model without compiling
model = load_model("D:/AI Virtual Dressing Room/model/mobilenetv2_clothing.h5", compile=False)

# Create a clean input layer without batch_shape dependency
new_input = Input(shape=model.input_shape[1:])  # Remove batch_size from shape

# Rebuild the model
new_model = tf.keras.Model(inputs=new_input, outputs=model(new_input))

# Save the cleaned-up model
new_model.save("D:/AI Virtual Dressing Room/model/mobilenetv2_cleaned.h5", save_format="h5")
print("Model successfully saved!")