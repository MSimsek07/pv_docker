import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
import plotly.express as px
import os

def load_model():
    """
    Loads the pre-trained model from the path specified in the environment variable.
    """
    model_path = os.getenv('MODEL_PATH', 'model_efficientnet.h5')
    return tf.keras.models.load_model(model_path)

def process_image(uploaded_image):
    """
    Preprocesses the uploaded image for prediction.
    """
    img = image.load_img(uploaded_image, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return preprocess_input(img)

def predict_image(model, img):
    """
    Predicts the class label for the input image.
    """
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    return predicted_class, prediction

def display_results(uploaded_image, predicted_class, waste_labels, prediction):
    """
    Displays the uploaded image, predicted class, and probability distribution.
    """
    st.image(uploaded_image, caption='Yüklenen Görüntü', width=100)
    st.write(f"Tahmin Edilen Sınıf: {waste_labels[predicted_class]}")
    
    st.write("Tahmin İhtimalleri:")
    labels = list(waste_labels.values())
    probabilities = prediction[0] * 100  # İhtimalleri yüzde olarak hesapla

    # Çubuk grafik
    fig_bar = px.bar(x=labels, y=probabilities, labels={'x': 'Sınıf', 'y': 'Yüzde (%)'},
                     title="Tahmin İhtimalleri (Çubuk Grafik)")
    st.plotly_chart(fig_bar)

    # Pasta grafiği
    fig_pie = px.pie(values=probabilities, names=labels, title="Tahmin İhtimalleri (Pasta Grafiği)")
    st.plotly_chart(fig_pie)

def main():
    """
    Main function to run the Streamlit application.
    """
    # Etiketler
    #"Cell", "Cell-Multi", "Cracking","Diode", "Diode-Multi", "Hot-Spot", "Hot-Spot-Multi", "No-Anomaly", "Offline-Module", "Shadowing", "Soiling", "Vegetation"
    waste_labels = {0: 'Cell', 1: 'Cell-Multi', 2: 'Cracking', 3: 'Diode', 4: 'Diode-Multi', 5: 'No-Anomaly', 6: 'Offline-Module', 7: 'Shadowing', 8: 'Soiling', 9: 'Vegetation'}
    
    # model yükle
    model = load_model()
    
    # uygulama yükle
    st.title("PV Panels Anomaly Detection☀️")
    st.write("Bu uygulama, güneş paneli görüntülerindeki anomalileri tespit etmek için eğitilmiş bir CNN derin öğrenme model kullanır. Lütfen bir görüntü yükleyin ve sonuçları görün!")
    
    # giriş yap
    uploaded_image = st.file_uploader("Lütfen resim giriniz ", type=["jpg", "png", "jpeg"])
    
    if uploaded_image is not None:
        img = process_image(uploaded_image)
        predicted_class, prediction = predict_image(model, img)
        display_results(uploaded_image, predicted_class, waste_labels, prediction)

if __name__ == "__main__":
    main()
