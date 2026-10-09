# Thomas Nguyen | Data Science Portfolio

A Streamlit portfolio featuring data science research, applied analytics, and machine learning case studies.

## Pages

- **Home:** introduction, skills, project overview, contact links, and resume download.
- **About Me:** background, experience, and professional interests.
- **Cyber Risk Forecasting:** temporal modelling and research case study.
- **Sports Broadcast Analytics:** sports sponsorship and media exposure analytics.
- **Food101 CNN Transfer Learning:** computer vision and transfer learning case study.
- **Retail Sales Analytics Dashboard:** retail KPI and dashboard case study.
- **Customer Churn Prediction:** work in progress; displayed model scores are explicitly labelled demo results.

These pages present case studies; the portfolio does not train models or run the underlying project pipelines.

## Repository structure

```text
Home.py
requirements.txt
README.md
assets/
    profile_photo.jpg
    resume.pdf
pages/
    1_About_Me.py
    2_Cyber_Risk_Forecasting.py
    3_Sports_Broadcast_Analytics.py
    4_Food101_CNN_Transfer_Learning.py
    5_Retail_Sales_Analytics_Dashboard.py
    6_Customer_Churn_Prediction.py
```

Keep `Home.py` at the repository root. Folder names `pages` and `assets` must be lowercase: deployment runs on a case-sensitive filesystem. Asset paths are resolved relative to the source files.

## Run locally

From the repository root, with Python 3.11 or 3.12:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m streamlit run Home.py
```

Open the local URL printed by Streamlit. Visit every sidebar page and check the photo and resume download on Home and About Me.

## Deploy on Streamlit Community Cloud

1. Review and commit the repository changes, then push to GitHub.
2. Select repository `ThomasNguyennnnn/Thomas-Nguyen-Portfolio`.
3. Select branch `main` and main file path `Home.py`.
4. Select the same Python version used for local testing.
5. Deploy and inspect the build logs if startup fails.

If an existing deployment uses `Pages/Home.py`, change its entrypoint to `Home.py` (or redeploy with the correct entrypoint).

Official guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app

## Troubleshooting

- **Only Home appears:** ensure lowercase `pages/` is beside root `Home.py`, and its six Python files are committed. Do not start `pages/Home.py`.
- **Missing photo or resume:** check the exact tracked paths `assets/profile_photo.jpg` and `assets/resume.pdf`.
- **Sidebar cannot reopen:** keep Streamlit's header visible, especially on narrow screens.
- **Local app works but deployment fails:** inspect Git's tracked filenames using `git ls-files`; Windows can conceal case mismatches. Check the Cloud logs and installed dependencies.
- **Changes are missing online:** verify the deployed branch and latest pushed commit. A clean working tree alone does not prove deployment succeeded.

## Publication checklist

- Verify every page on desktop and mobile, including navigation and resume download.
- Check GitHub, LinkedIn, and email details.
- Confirm project claims and metrics against the underlying work; retain demo labels until results are validated.
- Add public project repositories, screenshots, and reproducibility instructions as they become available.
- Add the live app URL here after deployment is verified.
- Keep private data, credentials, `.env`, and Streamlit secrets out of Git.
