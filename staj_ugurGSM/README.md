# UgurGSM - Django Web Projesi

Bu proje, Django framework kullanılarak geliştirilmiş bir web uygulamasıdır.  
Özellikler arasında **kullanıcı yönetimi (kayıt & giriş), ürün listesi/ekleme, iletişim formu** ve basit bir admin paneli bulunmaktadır.  

---

## 🚀 Başlangıç

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/kullanici/ugurGSM.git
cd ugurGSM
```

### 2. Sanal Ortam Oluşturun
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Veritabanını Hazırlayın
```bash
python manage.py migrate
```

### 5. Yönetici Kullanıcı Oluşturun
```bash
python manage.py createsuperuser
```

### 6. Sunucuyu Çalıştırın
```bash
python manage.py runserver
```

### 7. Tarayıcıdan Açın
```
http://127.0.0.1:8000/
```

---

## 📦 Kullanılan Teknolojiler
- [Python 3.x](https://www.python.org/)  
- [Django 4.x](https://www.djangoproject.com/)  
- [SQLite3](https://www.sqlite.org/) (varsayılan veritabanı)  
- [Bootstrap](https://getbootstrap.com/) (opsiyonel, front-end için)  

---

## ⚙️ Önemli Notlar
- `db.sqlite3`, `venv/` ve `media/` klasörleri repoya dahil edilmemelidir.  
- Paket bağımlılıkları `requirements.txt` içinde yer almaktadır.  
- Gerekirse kendi `.env` dosyanızı oluşturabilirsiniz (ör. gizli anahtar, DB şifreleri).  

---


## 📜 Lisans
Bu proje kişisel bir çalışma olup eğitim/deneme amaçlı staj projesidir. 
