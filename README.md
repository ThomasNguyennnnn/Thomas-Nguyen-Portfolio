# Thomas Nguyen | Data Science Portfolio

A professional, interactive data science portfolio built with **Python and Streamlit**, showcasing academic research, industry analytics, machine learning, computer vision, and business intelligence.

The portfolio features **four projects**, with an emphasis on practical problem-solving, evidence-based evaluation, data visualisation, and communicating analytical findings clearly.

**GitHub:** [ThomasNguyennnnn](https://github.com/ThomasNguyennnnn)  
**LinkedIn:** [Thomas Nguyen](https://www.linkedin.com/in/thomas-tuan-nguyen/)  
**Email:** thomas.nttn.au@gmail.com

---

## About This Portfolio

I am **Thomas Nguyen**, a graduate of the **Master of Data Science and Innovation at the University of Technology Sydney**, with a background in business analytics and experience across academic research and industry analytics.

My work spans predictive modelling, temporal data analysis, computer vision, interactive dashboards, and commercial reporting.

This portfolio is designed to provide an accessible overview of my work, with dedicated project pages explaining the objectives, methods, results, and limitations of each case study.

## Portfolio Pages

| Page | Description |
|---|---|
| **Home** | Concise portfolio introduction, selected project highlights, navigation, resume download, and contact links |
| **About Me** | Education, academic achievements, industry experience, research publications, technical capabilities, and professional direction |
| **Cyber Risk Modelling & Forecasting** | Two-phase cyber-risk research involving Hawkes processes, Transformer models, frequency prediction, severity calibration, and aggregate-loss analysis |
| **Sports Broadcast Analytics** | Industry analytics case study covering sponsorship visibility, broadcast exposure workflows, media monitoring, and commercial reporting |
| **Food101 CNN Transfer Learning** | Computer vision project evaluating frozen and fine-tuned ResNet50 models for food-image classification |
| **Retail Intelligence** | Interactive sales analytics and customer insights dashboard combining retail KPIs, RFM segmentation, and machine learning for purchasing-inactivity prediction |

## Featured Projects

### 1. Cyber Risk Modelling & Forecasting

A two-phase research project exploring temporal dependence, cyber-event prediction, and cyber-risk quantification.

**Phase 1 — Conference Research (AusDM 2026, Accepted)**

- Developed and evaluated models on a synthetic multivariate marked Hawkes benchmark.
- Compared Transformer Hawkes Process, Neural Hawkes approaches, recurrent models, and statistical baselines.
- Achieved **89.13% accuracy** for the primary top-risk entity prediction task using the Transformer Hawkes Process.

**Phase 2 — Journal Research (MDPI *Risks*, Accepted)**

- Reconstructed a system-wide event-frequency target from synthetic Hawkes event data.
- Compared frequency models using chronological evaluation.
- Combined the frequency component with independently calibrated cyber-loss severity assumptions.
- Investigated expected aggregate loss, Value at Risk (VaR), Tail Value at Risk (TVaR), and severity-tail sensitivity.
- Considered external evaluation using URLhaus data and discussed generalisability limitations.

**Technologies:** Python, Hawkes Processes, Transformers, GRU, LSTM, statistical modelling, probabilistic risk analysis.

**Research data:** [IEEE DataPort — DOI 10.21227/8drm-jz27](https://dx.doi.org/10.21227/8drm-jz27)

### 2. Sports Broadcast Analytics

An applied industry analytics case study based on my internship at **Futures Sport & Entertainment**.

The work involved supporting commercial sponsorship analytics, broadcast visibility assessment, data validation, and media monitoring.

Key activities included:

- Contributing to sponsorship exposure and broadcast-frame analysis workflows.
- Supporting data preparation and quality assurance using Excel.
- Reviewing sports sponsorship visibility across motorsport and marathon event contexts.
- Supporting athlete media monitoring and commercial reporting.

The broader Supercars analysis workflow involved **160,000+ broadcast frame outputs**. This figure describes the project workflow scope, not the number of frames personally reviewed.

**Technologies:** Excel, Power BI, TVEyes, data validation, reporting, sports analytics.

### 3. Food101 CNN Transfer Learning

A deep learning project investigating how selective fine-tuning affects the performance of a pretrained ResNet50 model on food-image classification.

Three reported experimental configurations were evaluated:

| Model configuration | Test accuracy |
|---|---:|
| Frozen ResNet50 backbone | 61.86% |
| Fine-tune layer4 | 81.75% |
| Fine-tune layer3 + layer4 | **85.07%** |

The strongest configuration improved test accuracy by **23.21 percentage points** over the frozen-backbone baseline.

The project demonstrates transfer learning, model evaluation, experimental comparison, and interpretation of deep learning results.

**Technologies:** Python, PyTorch, ResNet50, convolutional neural networks, transfer learning.

### 4. Retail Intelligence: Sales & Customer Analytics

An interactive business intelligence and machine learning project based on the **UCI Online Retail dataset**.

The dashboard integrates five components:

1. **Executive Overview:** Sales, order volume, customer counts, average order value, and revenue trends.
2. **Sales & Products:** Product rankings, quantity analysis, and market performance.
3. **Customer Insights:** Recency, Frequency, Monetary (RFM) analysis and purchasing behaviour.
4. **Inactivity Prediction:** Comparison of Logistic Regression, Random Forest, and Gradient Boosting models.
5. **Business Recommendations:** Interpretation of commercial performance and customer-risk findings.

The predictive component estimates whether a recently active customer will make **no further recorded purchase during the following 60 days**, using historical purchasing features and chronological model evaluation.

This is a **purchase-inactivity proxy**, not a verified contractual customer-churn label.

Sales metrics are calculated from the loaded transaction data. Machine learning training and evaluation can be initiated interactively within the Streamlit application; predictive scores are not fabricated or hardcoded.

**Technologies:** Python, pandas, NumPy, Plotly, Streamlit, scikit-learn, RFM analysis.

**Dataset:** [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)  
**Dataset citation:** Chen, D. (2015). *Online Retail*. UCI Machine Learning Repository. [DOI: 10.24432/C5BW33](https://doi.org/10.24432/C5BW33)

---

## Technical Skills

| Area | Tools and methods |
|---|---|
| **Programming & Data Analysis** | Python, SQL, R, pandas, NumPy, Excel, Power Query |
| **Machine Learning** | scikit-learn, PyTorch, Keras, classification, regression, CNNs, Transformers, GRU, LSTM |
| **Data Visualisation & BI** | Streamlit, Plotly, Matplotlib, Tableau, Power BI |
| **Statistical & Risk Modelling** | Statistical baselines, temporal modelling, probabilistic forecasting, frequency–severity analysis |
| **Professional Analytics** | Data cleaning, validation, KPI analysis, analytical reporting, research communication |

## Repository Structure

```text
Thomas-Nguyen-Portfolio/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   ├── profile_photo.jpg
│   ├── resume.pdf
│   └── Online Retail.xlsx
│
├── pages/
│   ├── 1_About_Me.py
│   ├── 2_Cyber_Risk_Forecasting.py
│   ├── 3_Sports_Broadcast_Analytics.py
│   ├── 4_Food101_CNN_Transfer_Learning.py
│   └── 5_Retail_Intelligence.py
│
├── Home.py
├── README.md
├── requirements.txt
└── .gitignore
```

**Important:** Keep `Home.py` at the repository root. Directory names `pages` and `assets` must use lowercase spelling because Streamlit Community Cloud runs on a case-sensitive filesystem.

The Retail Intelligence page can load `assets/Online Retail.xlsx` automatically or accept a compatible uploaded file. If the workbook is not stored in the repository, users will need to upload it.

## Run Locally

**Requirements:** Python 3.11 or 3.12, and the packages listed in `requirements.txt`.

Clone the repository:

```bash
git clone https://github.com/ThomasNguyennnnn/Thomas-Nguyen-Portfolio.git
cd Thomas-Nguyen-Portfolio
```

Create a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run Home.py
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Home.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

Use the Streamlit sidebar to navigate through the project pages.

## Deploy on Streamlit Community Cloud

1. Push the updated repository to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select the repository `ThomasNguyennnnn/Thomas-Nguyen-Portfolio`.
4. Select the `main` branch.
5. Set the application entry point to `Home.py`.
6. Select the appropriate Python version and deploy.
7. Test every page, especially Retail Intelligence's dataset loading and model evaluation functionality.

**Official documentation:** [Deploy a Streamlit app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)

## Reproducibility & Limitations

The portfolio combines research case studies and an interactive data application.

- **Cyber Risk:** Reported experimental results originate from the research studies. Charts illustrate documented findings rather than retraining the underlying models inside the portfolio.
- **Sports Broadcast:** The page describes industry workflow contributions and project scope. It does not claim independently verified sponsorship ROI or campaign impact.
- **Food101:** Model results reflect the reported transfer-learning experiments. The portfolio does not provide an interactive CNN training pipeline.
- **Retail Intelligence:** Sales and RFM metrics are calculated from transaction data. The predictive page trains and evaluates models on historical customer snapshots when requested.

For Retail Intelligence, the historical dataset does not establish contractual cancellation. Predictive results should therefore be interpreted as **purchase-inactivity risk estimates**, not confirmed customer churn or evidence of a causal retention benefit.

## Troubleshooting

| Issue | What to check |
|---|---|
| Only Home appears | Confirm that `pages/` is lowercase and located beside `Home.py` |
| Missing profile photo or resume | Verify `assets/profile_photo.jpg` and `assets/resume.pdf` |
| Retail dataset fails to load | Confirm `assets/Online Retail.xlsx` is a valid Excel workbook and `openpyxl` is installed |
| Machine learning training fails | Review the displayed exception and confirm sufficient historical customer data |
| Charts are difficult to read | Verify the Streamlit light-theme configuration and Plotly chart styling |
| Deployment fails | Check Cloud logs, `requirements.txt`, Python version, and case-sensitive file paths |
| Changes do not appear online | Confirm the latest commit was pushed to the branch used by the deployment |

## Final Publication Checklist

- [ ] All six Streamlit pages open correctly.
- [ ] Home links to the four current project pages.
- [ ] No references remain to the removed standalone Retail Sales or Customer Churn pages.
- [ ] Profile photo and resume download work.
- [ ] GitHub, LinkedIn, and email links are accurate.
- [ ] Charts and text are readable on desktop and mobile.
- [ ] Retail Intelligence loads the dataset and completes model evaluation.
- [ ] Research figures and publication statuses remain accurate.
- [ ] `requirements.txt` includes all required dependencies.
- [ ] No passwords, tokens, `.env` files, or Streamlit secrets are committed.
- [ ] The deployed application has been tested after the latest GitHub push.

---

## Contact

**Thomas Nguyen**  
Data Science · Machine Learning · Business Analytics

**Email:** thomas.nttn.au@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/thomas-tuan-nguyen/  
**GitHub:** https://github.com/ThomasNguyennnnn

*Thank you for exploring my portfolio.*