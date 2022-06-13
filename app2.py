import streamlit as st
import numpy as np
from tensorflow import keras
from PIL import Image
from keras.models import load_model
import pickle
import pandas as pd



labels = pickle.load(open('./labels', 'rb'))


st.title("Dog classifier")
st.header('Upload a picture!')

model = load_model('./model_data_softmax')
#labels = get_labels()

img = st.file_uploader('Upload your image here', type=(['jpg','jpeg']),)
img = Image.open(img)
st.image(img)
img = img.resize((224, 224))

img_arr = np.array(img)
img_arr = img_arr.reshape(1, 224, 224, 3)
img_arr = img_arr / 255

if img:
    with st.spinner('Predicting...'):
        pred = model.predict(img_arr)
        prediction = labels[np.argmax(pred)]
        sorted = np.argsort(pred)
        top_ten = [labels[sorted[0][-1]], labels[sorted[0][-2]],labels[sorted[0][-3]], labels[sorted[0][-4]], labels[sorted[0][-5]]]
        list_5 = [0, 1, 2, 3, 4]

st.write(f'The models prediction is...{prediction}')
st.write('If you are predicting breeds for mixed dogs, please see the tabel below for the top five predictions')
st.dataframe(pd.DataFrame(top_ten, columns=['Top_Five'], index=list_5))

# st.write(prediction)
#
# if prediction > .5:
#     st.write('Sorry not a hot dog')
# else:
#     st.write('It\'s a hot dog!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
