import numpy as np
from tensorflow.keras.models import load_model # type: ignore

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'c_model.h5')

nn = load_model(model_path)



def predict_img(img_path):
    from tensorflow.keras.preprocessing import image # type: ignore
    test_image = image.load_img(img_path, target_size = (128, 128),color_mode='grayscale')
    test_image = image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis = 0)
    result = nn.predict(test_image)
    print(result)
    if result[0][0]>result[0][1] and result[0][0]>result[0][2]:
        return 'benign'
    elif result[0][1]>result[0][0] and result[0][1]>result[0][2]:
        return 'malignant'
    else:
        return 'normal'

