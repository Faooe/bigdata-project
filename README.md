
# 🚀 Big Data Technology – Praktikum 1

## Spark + Cloud (Industry Ready)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PySpark](https://img.shields.io/badge/PySpark-Latest-orange)
![MongoDB Atlas](https://img.shields.io/badge/Database-MongoDB%20Atlas-green)
![Git](https://img.shields.io/badge/Version%20Control-Git-black)
![License](https://img.shields.io/badge/Status-Academic%20Project-lightgrey)

---

## 📌 Project Overview

Praktikum ini membangun **fondasi environment Data Engineer modern** dengan pendekatan industry-ready workflow.

Fokus utama:

* ✅ Environment reproducibility
* ✅ Cloud readiness
* ✅ Distributed processing
* ✅ Professional Git workflow
* ✅ Clean project structure

---

## 🎯 Learning Objectives

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

* Mengonfigurasi VS Code + PowerShell sebagai dev environment
* Menginstal & menjalankan PySpark
* Mengelola cluster cloud di MongoDB Atlas
* Menggunakan Git & GitHub secara profesional
* Membuat struktur proyek sesuai standar industri

---

## 🧰 Technology Stack

| Layer             | Technology    | Purpose                             |
| ----------------- | ------------- | ----------------------------------- |
| Editor            | VS Code       | Industry-standard development       |
| CLI               | PowerShell    | Environment & dependency management |
| Language          | Python 3.10+  | Stable & Spark compatible           |
| Processing Engine | PySpark       | Distributed data processing         |
| Cloud Database    | MongoDB Atlas | Cloud-native simulation             |
| Version Control   | Git & GitHub  | Professional workflow               |

---

# 📂 Project Structure

```bash
bigdata-project/
│
├── data/               # Local dataset storage
├── cloud_storage/      # Cloud storage simulation
├── scripts/            # Spark jobs & connection scripts
│   └── simple_job.py
├── notebooks/          # Jupyter exploration
├── reports/            # Processing reports
├── requirements.txt
└── README.md
```

---

# ⚙️ Environment Setup (Best Practice)

## 1️⃣ Clone Repository

```bash
git clone https://github.com/username/bigdata-project.git
cd bigdata-project
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

Buat file `requirements.txt`:

```txt
pyspark
pymongo
jupyter
```

Lalu install:

```bash
pip install -r requirements.txt
```

---

# ☁️ MongoDB Atlas Setup

1. Buat akun MongoDB Atlas
2. Pilih **M0 Free Tier**
3. Region: Singapore
4. Buat Database User (username & password)
5. Network Access → Allow Access from Anywhere
6. Pastikan status cluster: **ACTIVE**

---

# 🔥 Running Spark Job

File: `scripts/simple_job.py`

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

df = spark.createDataFrame(data, columns)

df.groupBy("category").sum("value").show()

spark.stop()
```

Run command:

```bash
python scripts/simple_job.py
```

Expected Output:

```
+--------+----------+
|category|sum(value)|
+--------+----------+
|       B|        20|
|       A|        40|
+--------+----------+
```

---

# 📊 Professional Git Workflow

### Initialize Git (if new project)

```bash
git init
git add .
git commit -m "Initial commit - Spark environment setup"
```

### Push to GitHub

```bash
git remote add origin https://github.com/username/bigdata-project.git
git branch -M main
git push -u origin main
```

---

# 📈 Industry Insight

Praktikum ini mensimulasikan workflow Data Engineer:

* Local development
* Distributed processing
* Cloud integration
* Version control discipline
* Structured project architecture

Ini adalah fondasi sebelum masuk ke:

* Spark cluster production
* Data pipeline orchestration
* Cloud data warehouse
* CI/CD integration

---

# 👨‍💻 Author

**Nama:** (Husin Nafarin Ramadhani)
* Program Studi: Teknologi Informasi
* Universitas: UIN Antasari
* Tahun: 2026
