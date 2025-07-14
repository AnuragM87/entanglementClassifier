# Entanglement Classifier

A full-stack application for classifying quantum states as entangled or separable using machine learning, inspired by the paper:

> Transforming Bell's inequalities into state classifiers with machine learning  
> Yue-Chi Ma and Man-Hong Yung, npj Quantum Information (2018)

## Features
- **Quantum State Generation:** Generate random two-qubit quantum states.
- **Feature Extraction:** Compute CHSH/Bell-like features for each state.
- **Entanglement Labeling:** Label states using the PPT criterion.
- **Machine Learning Classifier:** Neural network trained to classify states as entangled or separable.
- **REST API:** FastAPI backend for state generation and classification.
- **Frontend UI:** React app for user interaction and visualization.

---

## Project Structure
```
entanglementClassifier/
├── backend/           # Python FastAPI backend, ML, quantum logic
│   ├── data/
│   ├── models/
│   ├── utils/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── frontend/          # React frontend
│   ├── src/
│   ├── public/
│   └── ...
├── README.md
└── ...
```

---

## Setup Instructions

### 1. Backend (FastAPI + ML)

#### a. Install Python dependencies
```bash
pip install -r backend/requirements.txt
```

#### b. Train the ML model
```bash
python -m backend.models.train_model
```
This will generate and save a neural network model at `backend/models/entanglement_classifier.h5`.

#### c. Start the FastAPI server
```bash
uvicorn backend.main:app --reload
```
The API will be available at `http://localhost:8000`.

### 2. Frontend (React)

#### a. Install Node dependencies
```bash
cd frontend
npm install
```

#### b. Start the React development server
```bash
npm start
```
The app will be available at `http://localhost:3000`.

---

## Usage
- **Generate State:** Click "Generate State" to get a random quantum state, its features, and entanglement label.
- **Classify Custom State:** Enter four CHSH features and click "Classify" to get a prediction from the ML model.

---

## Deployment
- **Frontend:** Can be deployed to Vercel, Netlify, or any static hosting.
- **Backend:** Can be deployed to platforms like Render, Railway, or as a serverless function (with adaptation).
- Update API URLs in the frontend as needed for production.

---

## References
- [Transforming Bell's inequalities into state classifiers with machine learning (npj Quantum Information, 2018)](https://www.nature.com/articles/s41534-018-0081-3)
- [QuTiP: Quantum Toolbox in Python](http://qutip.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)

---

## License
This project is for academic and research purposes. See the original paper for scientific credit.
