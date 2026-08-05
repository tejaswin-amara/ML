# 🚢 Week 2: Titanic Analysis

## 📌 Project Status
This module focuses on the initial data ingestion and cleaning phase of the **PlacementPredict** anchor project.

### 📊 Data Preview

#### Dataset Summary
- **Rows:** 891
- **Columns:** 15
- **Features:** survived, pclass, sex, age, sibsp, parch, fare, embarked, class, who, adult_male, deck, embark_town, alive, alone

#### First 5 Rows
|   survived |   pclass | sex    |   age |   sibsp |   parch |    fare | embarked   | class   | who   | adult_male   | deck   | embark_town   | alive   | alone   |
|-----------:|---------:|:-------|------:|--------:|--------:|--------:|:-----------|:--------|:------|:-------------|:-------|:--------------|:--------|:--------|
|          0 |        3 | male   |    22 |       1 |       0 |  7.25   | S          | Third   | man   | True         | nan    | Southampton   | no      | False   |
|          1 |        1 | female |    38 |       1 |       0 | 71.2833 | C          | First   | woman | False        | C      | Cherbourg     | yes     | False   |
|          1 |        3 | female |    26 |       0 |       0 |  7.925  | S          | Third   | woman | False        | nan    | Southampton   | yes     | True    |
|          1 |        1 | female |    35 |       1 |       0 | 53.1    | S          | First   | woman | False        | C      | Southampton   | yes     | False   |
|          0 |        3 | male   |    35 |       0 |       0 |  8.05   | S          | Third   | man   | True         | nan    | Southampton   | no      | True    |

### ✅ Completed Tasks
- [x] Load raw Titanic CSV data.
- [x] Initial data inspection and structure analysis.
- [x] Integrated data summary into README.

### 🔜 Upcoming Work
- [x] Exploratory Data Analysis (EDA) (Report Added).
- [ ] Missing Value Treatment.
- [ ] Feature engineering pipeline.

## 📂 Folder Contents
- `titanic.csv`: Raw passenger data.
- `analysis.py`: Data loading script.
- `Titanic_EDA_Report.pdf`: Detailed exploratory data analysis report.
- `Experiment_2_Titanic_Analysis.ipynb`: Comprehensive notebook for Titanic data exploration.
