# 📘 Week 1: Foundations & Python Primer

## 📌 Project Status
Initial setup and foundational logic for the **PlacementPredict** anchor project.

### 📊 Data Preview (Placement Predict 50k)

#### Dataset Summary
- **Rows:** 50000
- **Columns:** 32
- **Features:** StudentID, Gender, City, CollegeTier, Stream, Specialisation, Hostel, HistoryOfBacklogs, SGPA_Sem1, SGPA_Sem2, SGPA_Sem3, SGPA_Sem4, SGPA_Sem5, SGPA_Sem6, SGPA_Sem7, SGPA_Sem8, CGPA, AttendancePercent, Internships, Projects, Workshops, Certifications, Publications, AptitudeTestScore, SoftSkillsRating, CodingTestScore, MockInterviewScore, ExtraCurricular, CGPA_Tier, PlacementStatus, IsAnomaly, Salary Package

#### First 5 Rows
|   StudentID | Gender   | City      | CollegeTier   | Stream   | Specialisation   | Hostel   | HistoryOfBacklogs   |   SGPA_Sem1 |   SGPA_Sem2 |   SGPA_Sem3 |   SGPA_Sem4 |   SGPA_Sem5 |   SGPA_Sem6 |   SGPA_Sem7 |   SGPA_Sem8 |   CGPA |   AttendancePercent |   Internships |   Projects |   Workshops |   Certifications |   Publications |   AptitudeTestScore |   SoftSkillsRating |   CodingTestScore |   MockInterviewScore |   ExtraCurricular | CGPA_Tier   |   PlacementStatus |   IsAnomaly |   Salary Package |
|------------:|:---------|:----------|:--------------|:---------|:-----------------|:---------|:--------------------|------------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|-------:|--------------------:|--------------:|-----------:|------------:|-----------------:|---------------:|--------------------:|-------------------:|------------------:|---------------------:|------------------:|:------------|------------------:|------------:|-----------------:|
|           1 | Male     | Ahmedabad | Tier2         | ECE      | Networking       | No       | No                  |        6.02 |        6.54 |        6.52 |        6    |        6.47 |        5.91 |        6.49 |        5.5  |   6.29 |                73.3 |             1 |          2 |         nan |                2 |              0 |                66.7 |                2.2 |              49.4 |                 47.8 |                 0 | Low         |                 0 |           0 |             0    |
|           2 | Female   | Mumbai    | Tier2         | ECE      | DataScience      | Yes      | Yes                 |        5.84 |        5.12 |        5.34 |        5.18 |        5.03 |        4.93 |        5.4  |        5.13 |   5.23 |                54.5 |             0 |          1 |           0 |                1 |              0 |                48.2 |                2.4 |              26.7 |                 25.8 |                 0 | Low         |                 0 |           0 |             0    |
|           3 | Male     | Kolkata   | Tier2         | IT       | DataScience      | Yes      | No                  |        4.91 |        5.29 |        5.49 |        5.73 |        5.33 |        5.88 |        5.82 |        5.67 |   5.52 |                77.6 |             1 |          3 |           1 |                1 |              0 |                73.8 |                2.8 |              67.7 |                 41.5 |                 0 | Low         |                 1 |           0 |             3.89 |
|           4 | Male     | Jaipur    | Tier1         | CS       | AI               | No       | No                  |        7.67 |        8.03 |        8.08 |        7.64 |        6.86 |        7.1  |        7.56 |        7.39 |   7.51 |                68.8 |             1 |          2 |           1 |                2 |              0 |                69.8 |                2.7 |              66.9 |                 48   |                 0 | Mid         |                 1 |           0 |             8.37 |
|           5 | Male     | Pune      | Tier2         | IT       | DataScience      | Yes      | No                  |        8.14 |        8.97 |        8.36 |        8.55 |        8.55 |        8.38 |        9.1  |        8.86 |   8.65 |                95.8 |             2 |          3 |         nan |                4 |              1 |                73.1 |                2.1 |              71.7 |                 61.7 |                 1 | High        |                 1 |           0 |            18.99 |

### ✅ Completed Tasks
- [x] Initial Python logic implementation.
- [x] Dataset ingestion and verification.
- [x] Repository structure initialization.

### 📊 Analysis Reports
- [Week 1 EDA Report](./Week1_EDA_Report.md)

### 🔜 Upcoming Work
- [x] Exploratory Data Analysis (Visuals generated).
- [x] Outlier detection scripts (Report generated).

## 📂 Folder Contents
- `Experiment_0_Python_Primer.ipynb`: Introductory Python exercises.
- `experiment_0_logic.py`: Core logic scripts.
- `placement_predict_50k Dataset.csv`: Primary dataset for the course.
- `Outlier_Report.md`: List of detected anomalies.

- `performance_analysis.png`: Visual correlation of student metrics.
- `placement_predict_engineered.csv`: Dataset with engineered performance features.
