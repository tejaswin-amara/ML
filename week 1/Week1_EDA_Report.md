# 📊 Week 1: Exploratory Data Analysis Report - PlacementPredict

## 📝 Executive Summary
This report summarizes the initial exploration of the 50,000 record PlacementPredict dataset.

### 📈 Statistical Summary
|       |   StudentID |   SGPA_Sem1 |   SGPA_Sem2 |   SGPA_Sem3 |   SGPA_Sem4 |   SGPA_Sem5 |   SGPA_Sem6 |   SGPA_Sem7 |   SGPA_Sem8 |        CGPA |   AttendancePercent |   Internships |    Projects |   Workshops |   Certifications |   Publications |   AptitudeTestScore |   SoftSkillsRating |   CodingTestScore |   MockInterviewScore |   ExtraCurricular |   PlacementStatus |    IsAnomaly |   Salary Package |
|:------|------------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|--------------------:|--------------:|------------:|------------:|-----------------:|---------------:|--------------------:|-------------------:|------------------:|---------------------:|------------------:|------------------:|-------------:|-----------------:|
| count |     50000   | 50000       | 50000       | 50000       | 50000       | 50000       | 50000       | 50000       | 50000       | 50000       |          50000      |  50000        | 50000       | 45512       |      50000       |   50000        |          45971      |       46474        |        47024      |           45043      |      50000        |      50000        | 50000        |      50000       |
| mean  |     25000.5 |     7.21058 |     7.22224 |     7.2354  |     7.24729 |     7.25864 |     7.27451 |     7.28272 |     7.2937  |     7.24615 |             76.7099 |      1.12774  |     2.10952 |     1.80447 |          1.93142 |       0.73546  |             68.8593 |           3.15421  |           57.4113 |              55.4085 |          0.533    |          0.65712  |     0.035    |          9.53612 |
| std   |     14433.9 |     1.51785 |     1.53201 |     1.55163 |     1.57063 |     1.58783 |     1.60326 |     1.62161 |     1.63811 |     1.61569 |             12.4744 |      0.813631 |     1.20761 |     1.03619 |          1.17539 |       0.717167 |             15.3652 |           0.981333 |           20.9797 |              17.5222 |          0.498915 |          0.474677 |     0.183782 |          8.82456 |
| min   |         1   |     4       |     4       |     4       |     4       |     4       |     4       |     4       |     4       |     4       |             50      |      0        |     0       |     0       |          0       |       0        |             30      |           1        |            0      |              15.9    |          0        |          0        |     0        |          0       |
| 25%   |     12500.8 |     6.09    |     6.09    |     6.08    |     6.07    |     6.07    |     6.08    |     6.06    |     6.06    |     6.04    |             67.6    |      1        |     1       |     1       |          1       |       0        |             58.5    |           2.4      |           45.9    |              44.2    |          0        |          0        |     0        |          0       |
| 50%   |     25000.5 |     7.19    |     7.21    |     7.22    |     7.24    |     7.26    |     7.28    |     7.3     |     7.31    |     7.25    |             77.2    |      1        |     2       |     2       |          2       |       1        |             69.9    |           3.2      |           57.7    |              54.7    |          1        |          1        |     0        |          8.43    |
| 75%   |     37500.2 |     8.34    |     8.36    |     8.4     |     8.43    |     8.46    |     8.5     |     8.52    |     8.56    |     8.48    |             85.9    |      2        |     3       |     3       |          3       |       1        |             79.7    |           3.9      |           73.3    |              69.2    |          1        |          1        |     0        |         18.41    |
| max   |     50000   |    10       |    10       |    10       |    10       |    10       |    10       |    10       |    10       |    10       |            100      |      3        |     5       |     4       |          5       |       3        |            100      |           5        |          100      |             100      |          1        |          1        |     1        |         26       |

### 🔍 Data Quality Check (Missing Values)
|                    |   Missing Values |
|:-------------------|-----------------:|
| StudentID          |                0 |
| Gender             |                0 |
| City               |                0 |
| CollegeTier        |                0 |
| Stream             |                0 |
| Specialisation     |                0 |
| Hostel             |                0 |
| HistoryOfBacklogs  |                0 |
| SGPA_Sem1          |                0 |
| SGPA_Sem2          |                0 |
| SGPA_Sem3          |                0 |
| SGPA_Sem4          |                0 |
| SGPA_Sem5          |                0 |
| SGPA_Sem6          |                0 |
| SGPA_Sem7          |                0 |
| SGPA_Sem8          |                0 |
| CGPA               |                0 |
| AttendancePercent  |                0 |
| Internships        |                0 |
| Projects           |                0 |
| Workshops          |             4488 |
| Certifications     |                0 |
| Publications       |                0 |
| AptitudeTestScore  |             4029 |
| SoftSkillsRating   |             3526 |
| CodingTestScore    |             2976 |
| MockInterviewScore |             4957 |
| ExtraCurricular    |                0 |
| CGPA_Tier          |                0 |
| PlacementStatus    |                0 |
| IsAnomaly          |                0 |
| Salary Package     |                0 |

### 🔗 Feature Correlation with Placement Status
|                    |   PlacementStatus |
|:-------------------|------------------:|
| PlacementStatus    |       1           |
| Salary Package     |       0.774443    |
| SGPA_Sem8          |       0.707147    |
| SGPA_Sem7          |       0.701972    |
| SGPA_Sem6          |       0.695881    |
| SGPA_Sem5          |       0.690914    |
| SGPA_Sem4          |       0.683972    |
| SGPA_Sem3          |       0.67778     |
| SGPA_Sem2          |       0.672252    |
| MockInterviewScore |       0.668       |
| SGPA_Sem1          |       0.665039    |
| CGPA               |       0.648926    |
| SoftSkillsRating   |       0.624788    |
| CodingTestScore    |       0.612832    |
| Certifications     |       0.601315    |
| Workshops          |       0.581535    |
| Projects           |       0.580122    |
| AptitudeTestScore  |       0.577749    |
| AttendancePercent  |       0.554024    |
| Internships        |       0.526197    |
| Publications       |       0.469351    |
| ExtraCurricular    |       0.239572    |
| IsAnomaly          |       9.17062e-06 |
| StudentID          |      -0.00129646  |

## 💡 Key Observations
- The dataset is well-populated with no major missing values in key columns.
- CGPA and Coding Test Scores show significant correlation with placement outcomes.
