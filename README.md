# MLNG · Machine Learning (PBL Track)

## Course Overview
**Machine Learning (25SC2107E)** follows an **Outside-in · Project-driven** pedagogy. Students build, evaluate, and deploy real ML systems, starting from a deployed prediction service and unfolding each layer beneath it.

### Course Outcomes (COs)
- **CO1**: Analyze end-to-end ML system lifecycles.
- **CO2**: Apply linear supervised-learning models and regularization.
- **CO3**: Apply tree-based models (Random Forests, XGBoost, LightGBM).
- **CO4**: Apply unsupervised-learning techniques (Clustering, PCA, UMAP).
- **CO5**: Analyze model performance using CV and advanced metrics.
- **CO6**: Apply ML-engineering practices for production deployment.

### Repository Structure
- **[week 1/](week%201/)**: Foundations, Python Primer, and initial datasets.
- **[week 2/](week%202/)**: Titanic Analysis and data pipeline initiation.

### Anchor Project: PlacementPredict
A deployed ML system predicting student placement outcomes (~50k records). The project spans 12 weeks covering the full pipeline from ingestion to FastAPI serving and drift monitoring.

### Tool Stack
- **Core**: Python 3.11, pandas, NumPy, scikit-learn
- **Advanced**: XGBoost, LightGBM, Optuna
- **Deployment**: FastAPI, Docker, MLflow
