## Güneş Paneli Anomali Tespiti Uygulaması - Teknik Dökümantasyon

### 1. Giriş

Bu doküman, **Python** programlama dili kullanılarak geliştirilen bir Güneş Paneli Anomali Tespiti uygulamasının teknik dökümantasyonunu sunmaktadır. Uygulama, yüklenen güneş paneli görüntülerindeki anomalileri tespit etmek için önceden eğitilmiş bir Evrişimli Sinir Ağı (CNN) modelini kullanır. Streamlit framework'ü, kullanıcı dostu bir web arayüzü oluşturmak için kullanılır.

### 2. Genel Bakış

Uygulama, kullanıcının bir güneş paneli görüntüsü yüklemesini, modelin görüntüyü analiz etmesini ve olası anomalileri tahmin etmesini sağlar. Tahmin edilen anomali sınıfı ve her sınıf için olasılık dağılımı, kullanıcı arayüzünde görüntülenir.

### 3. Kod Yapısı ve Mimari

Kod, modüler bir yapı izler ve aşağıdaki temel bileşenleri içerir:

#### 3.1. `load_model()` Fonksiyonu

Bu fonksiyon, önceden eğitilmiş derin öğrenme modelini diskten yükler. Model dosyasının yolu, `MODEL_PATH` ortam değişkeninden alınır. 

#### 3.2. `process_image()` Fonksiyonu

Yüklenen görüntü, model tarafından işlenmeden önce bu fonksiyon tarafından ön işlenir. Ön işleme adımları şunları içerir:

- Görüntüyü modelin beklediği boyuta (224x224) yeniden boyutlandırma.
- Görüntüyü NumPy dizisine dönüştürme.
- Modele giriş olarak vermeden önce dizi boyutlarını ayarlama.
- Önceden eğitilmiş modelin gerektirdiği spesifik ön işleme adımlarını uygulama (`preprocess_input()`).

#### 3.3. `predict_image()` Fonksiyonu

Bu fonksiyon, önceden işlenmiş görüntüyü modele besler ve tahmini sınıf etiketini döndürür. Tahmin edilen sınıf, model çıktısındaki en yüksek olasılığa sahip sınıfa karşılık gelir.

#### 3.4. `display_results()` Fonksiyonu

Bu fonksiyon, yüklenen görüntüyü, tahmin edilen sınıf etiketini ve her sınıf için olasılık dağılımını görüntüler. Olasılık dağılımı, kullanıcıların modelin tahminine olan güvenini yorumlamalarına yardımcı olmak için hem çubuk grafik hem de pasta grafik olarak görüntülenir.

#### 3.5. `main()` Fonksiyonu

Bu fonksiyon, uygulamanın ana giriş noktasıdır. Streamlit arayüzünü başlatır, yüklenen görüntüleri işler, tahminleri alır ve sonuçları görüntüler.

### 4. Kullanılan Teknolojiler

Uygulama, aşağıdaki teknolojileri kullanır:

- **Python:** Uygulamanın geliştirildiği temel programlama dilidir.
- **Streamlit:** Kullanıcı dostu bir web arayüzü oluşturmak için kullanılan açık kaynaklı bir Python kütüphanesidir.
- **TensorFlow:** Derin öğrenme modelleri oluşturmak ve eğitmek için kullanılan açık kaynaklı bir kütüphanedir.
- **Keras:** TensorFlow'un üstünde çalışan ve derin öğrenme modellerini tanımlamayı ve eğitmeyi kolaylaştıran üst düzey bir API'dir.
- **NumPy:** Python'da bilimsel hesaplama için kullanılan temel bir kütüphanedir.
- **Plotly:** Etkileşimli grafikler oluşturmak için kullanılan bir Python kütüphanesidir.

