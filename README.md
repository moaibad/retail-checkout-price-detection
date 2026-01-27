# Retail Checkout Price Detection

Sistem deteksi produk retail menggunakan YOLOv7 untuk menghitung total harga belanjaan secara otomatis.

## Overview

### Halaman Home
Halaman yang pertama kali tampil saat membuka website.

![Halaman Home](docs/screenshots/home.png)

### Halaman Deteksi
Halaman untuk pengguna mengupload gambar dengan cara mengklik button select file maupun drag and drop image.

![Halaman Deteksi](docs/screenshots/deteksi.png)

### Hasil Deteksi
Setelah klik deteksi akan tampil hasil gambar yang telah dilakukan deteksi beserta detail nama, harga setiap produk, dan total harga.

![Hasil Deteksi](docs/screenshots/hasil.png)

## Tech Stack

- Python 3.8+ (Ultralytics YOLOv7, OpenCV)
- PHP 7.4+
- MySQL
- Bootstrap 3

## Dataset & Model

- **Dataset**: [Grocery Dataset](https://universe.roboflow.com/new-workspace-wfzw3/grocery-dataset-q9fj2) dari Roboflow
- **Base Model**: YOLOv7
- **Epochs**: 10

## Struktur Proyek

```
├── web/              
│   ├── index.php     
│   ├── connection.php
│   └── upload.php
├── yolo/             
│   ├── best.pt       
│   └── opencv.py     
└── app/              
```

## Instalasi

### 1. Clone & Pindahkan ke htdocs
```bash
git clone https://github.com/moaibad/retail-checkout-price-detection.git
cp -r retail-checkout-price-detection /xampp/htdocs/
```

### 2. Install Python Dependencies
```bash
pip install ultralytics opencv-python
```

### 3. Setup Database
```sql
CREATE DATABASE data;
USE data;

CREATE TABLE produk (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255) NOT NULL,
  harga INT NOT NULL
);

-- Data produk (25 produk yang didukung model)
INSERT INTO produk (nama, harga) VALUES
('Bisconni Chocolate Chip Cookies 46.8gm', 15000),
('Coca Cola Can 250ml', 8000),
('Colgate Maximum Cavity Protection 75gm', 18000),
('Fanta 250ml', 7000),
('Fresher Guava Nectar 500ml', 12000),
('Fruita Vitals Red Grapes 200ml', 10000),
('Islamabad Tea 238gm', 35000),
('Kolson Slanty Jalapeno 18gm', 5000),
('Kurkure Chutney Chaska 62gm', 8000),
('LU Candi Biscuit 60gm', 7000),
('LU Oreo Biscuit 19gm', 6000),
('LU Prince Biscuit 55.2gm', 7500),
('Lays Masala 34gm', 10000),
('Lays Wavy Mexican Chili 34gm', 10000),
('Lifebuoy Total Protect Soap 96gm', 12000),
('Lipton Yellow Label Tea 95gm', 22000),
('Meezan Ultra Rich Tea 190gm', 38000),
('Peek Freans Sooper Biscuit 13.2gm', 3000),
('Safeguard Bar Soap Pure White 175gm', 15000),
('Shezan Apple 250ml', 9000),
('Sunsilk Shampoo Soft - Smooth 160ml', 35000),
('Super Crisp BBQ 30gm', 5000),
('Supreme Tea 95gm', 20000),
('Tapal Danedar 95gm', 21000),
('Vaseline Healthy White Lotion 100ml', 32000);
```

### 4. Konfigurasi Path
Edit `yolo/opencv.py` sesuaikan path ke lokasi instalasi.

## Cara Pakai

1. Akses `http://localhost/retail-checkout-price-detection/web/`
2. Upload gambar produk
3. Klik **Deteksi**
4. Lihat hasil & total harga

## Troubleshooting

- **Deteksi tidak jalan**: Uncomment `shell_exec` di `index.php` dan pastikan Python terinstall
- **Upload gagal**: Cek permission folder `yolo/`
- **Database error**: Pastikan MySQL running dan database `data` sudah dibuat

---