# 🏎️ F1 Top-10 Finish Predictor  
### *Machine Learning + Streamlit | Predict real F1 race outcomes in seconds*

![banner](assets/logo.png)

A Formula 1–themed machine learning project that predicts the **probability that a driver finishes inside the top 10** in any Grand Prix.  
The system uses **20+ years of F1 results**, engineered features (recent form, pit stops, standings, circuit type), and a tuned **Random Forest model (ROC-AUC: 0.92)**.

This repo also contains a **Streamlit web application** with a custom **F1-style dark theme UI**.

---

## 🚀 Features
- Predict top-10 probability for any race scenario  
- Modern F1-inspired UI (dark mode, racing stripes, gradient accents)  
- Full pipeline: data → feature engineering → model → app  
- Cached model + feature loading for fast predictions  
- CSV lookup integration (drivers, constructors, circuits, etc.)  
- Works completely offline

---

## 🧠 Model Performance
- **Algorithm:** Random Forest Classifier  
- **ROC-AUC:** 0.92  
- **Best features:**  
  - Grid & Qualifying  
  - Driver/Constructor season points  
  - Recent form (last 3 races)  
  - Pit time patterns  
  - Street vs permanent circuit  

Example diagnostic (ROC curve):

![roc](assets/roc_example.png)

---

## 📦 Repository Structure

# 🏎️ F1 Top-10 Finish Predictor  
### *Machine Learning + Streamlit | Predict real F1 race outcomes in seconds*

![banner](assets/logo.png)

A Formula 1–themed machine learning project that predicts the **probability that a driver finishes inside the top 10** in any Grand Prix.  
The system uses **20+ years of F1 results**, engineered features (recent form, pit stops, standings, circuit type), and a tuned **Random Forest model (ROC-AUC: 0.92)**.

This repo also contains a **Streamlit web application** with a custom **F1-style dark theme UI**.

---

## 🚀 Features
- Predict top-10 probability for any race scenario  
- Modern F1-inspired UI (dark mode, racing stripes, gradient accents)  
- Full pipeline: data → feature engineering → model → app  
- Cached model + feature loading for fast predictions  
- CSV lookup integration (drivers, constructors, circuits, etc.)  
- Works completely offline

---

## 🧠 Model Performance
- **Algorithm:** Random Forest Classifier  
- **ROC-AUC:** 0.92  
- **Best features:**  
  - Grid & Qualifying  
  - Driver/Constructor season points  
  - Recent form (last 3 races)  
  - Pit time patterns  
  - Street vs permanent circuit  

Example diagnostic (ROC curve):

![roc](assets/roc_example.png)

---

## 📦 Repository Structure

# 🏎️ F1 Top-10 Finish Predictor  
### *Machine Learning + Streamlit | Predict real F1 race outcomes in seconds*

![banner](assets/logo.png)

A Formula 1–themed machine learning project that predicts the **probability that a driver finishes inside the top 10** in any Grand Prix.  
The system uses **20+ years of F1 results**, engineered features (recent form, pit stops, standings, circuit type), and a tuned **Random Forest model (ROC-AUC: 0.92)**.

This repo also contains a **Streamlit web application** with a custom **F1-style dark theme UI**.

---

## 🚀 Features
- Predict top-10 probability for any race scenario  
- Modern F1-inspired UI (dark mode, racing stripes, gradient accents)  
- Full pipeline: data → feature engineering → model → app  
- Cached model + feature loading for fast predictions  
- CSV lookup integration (drivers, constructors, circuits, etc.)  
- Works completely offline

---

## 🧠 Model Performance
- **Algorithm:** Random Forest Classifier  
- **ROC-AUC:** 0.92  
- **Best features:**  
  - Grid & Qualifying  
  - Driver/Constructor season points  
  - Recent form (last 3 races)  
  - Pit time patterns  
  - Street vs permanent circuit  

Example diagnostic (ROC curve):

![roc]()
![alt text](image.png)
---

## 📦 Repository Structure

f1_world_championship_data/
│ app.py # Streamlit app
│ README.md
│ requirements.txt
│ LICENSE
│
├─ processed/ # Required CSV lookup data
│ drivers.csv
│ races.csv
│ constructors.csv
│ circuits.csv
│ ...
│
├─ models/ # ML model files
│ rf_top10_model.joblib
│ feature_list.joblib
│
├─ assets/ # Images, logos, screenshots
│ logo.png
│ roc_example.png
│
└─ notebooks/
01_load_and_explore.ipynb


---

## 🛠️ Installation

### **1. Clone the repo**
```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
cd <YOUR_REPO>


2.install dependencies 
pip install -r requirements.txt


3.run the Streamlit app

streamlit run app.py


📁 Required Files

The app needs the following folders:

✔ processed/ (CSV datasets)

These include:

-->drivers.csv

-->constructors.csv

-->races.csv

-->circuits.csv

--->results.csv

(and others)

✔ models/ (trained ML files)

-->rf_top10_model.joblib

-->feature_list.joblib



🧳 If You Want to Ship the Model Separately

git lfs install
git lfs track "models/*.joblib"
git add .gitattributes
git add models/
git commit -m "Track model files with LFS"

Or instruct users:


Download model files from the release page and place them into /models/.



🧩 How the Model Works (Short Explanation)

We built a pipeline that:

1.Reads all F1 race data from 1950–present

2.Merges:

->results

->qualifying

->pit stops

->driver standings

->constructor standings

2.Creates rolling/seasonal features:

->Recent finish average

->Recent top-10 rate

->Pit stop patterns

->Driver/constructor season form

4.Includes circuit metadata (street vs non-street)

5.Trains & validates a Random Forest with time-aware train/test split

6.Evaluates with ROC-AUC (0.92)

7.Saves model + feature list for inference

The Streamlit app reconstructs those features from your inputs and predicts the probability.

🎨 Streamlit UI – F1 Themed

The app uses:

->custom CSS for F1 branding

->gradient red headers

->modified buttons

->carbon-fiber-inspired backgrounds

->racing-stripe decorator elements


📸 Screenshots

![alt text](image-1.png)



🤝 Contributing

Pull requests welcome!
Ideas:

Add SHAP explainability

Add per-track performance profiling

Add live telemetry API integration



📄 License

MIT License — feel free to use or modify.

⭐ Support

If you like this project, consider starring ⭐ the repo!



