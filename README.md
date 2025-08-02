# 📱 Online Lending Platform Scrape Reviews and  Sentiment Analysis (Google Play Store)

*Tidak ada ajakan untuk melakukan Pinjaman Online (Pinjol) atau merekomendasikan aplikasi atau platform yang ada ⛔

<p align="center">
  <img src="https://github.com/user-attachments/assets/58129e6a-0b4f-482a-b3e3-b46c1fb2914f" alt="SelfieSatpamGIF" />
</p>



## 📌 Project Overview

This project aims to analyze user reviews from **Google Play Store** for various **online lending (pinjaman online / pinjol)** applications in Indonesia. The reviews were scraped using the **Google Play Scraper** by passing the application ID from the Play Store URL, and **1000 newest reviews** were collected for each lending platform.

The list of Indonesia's Online Lending Platforms :
- JULO
- IndoDana
- Kredivo
- RupiahCepat

We then performed **text preprocessing** and conducted **Sentiment Analysis** using a **pre-trained BERT model**:  
[`w11wo/indonesian-roberta-base-sentiment-classifier`](https://huggingface.co/w11wo/indonesian-roberta-base-sentiment-classifier)

## 🔄 Workflow Summary

### 1. 🔍 Data Scraping
- Source: Google Play Store
- Tool: [`google-play-scraper`](https://pypi.org/project/google-play-scraper/)
- Method: Scraping the 1000 newest user reviews by app ID
- Extracted fields:
  - `reviewContent`: The actual review text
  - `at`: The date of the review
  - `score`: User rating (1–5)

### 2. 🧹 Preprocessing
- Lowercasing text
- Removing punctuation, symbols, and stopwords
- Tokenization and cleaning to suit model input format

### 3. 🧠 Sentiment Analysis
- Model used: `w11wo/indonesian-roberta-base-sentiment-classifier`
- Output sentiment classes:
  - `Positive`
  - `Neutral`
  - `Negative`

### 4. 📊 Exploratory Data Analysis (EDA)
- Visualizations:
  - Sentiment distribution (Bar Chart & Pie Chart)
  - Correlation analysis between sentiment and score
  - WordClouds for each sentiment class
- Libraries: `matplotlib`, `seaborn`, `wordcloud`, `pandas`, `plotly`, etc.

---

## 💡 Key Insights

- ✅ **Scraping from Google Play is easier and less restricted** compared to scraping e-commerce websites (which often require Selenium/BeautifulSoup) or Twitter (which now has strict API limits). As long as you have the correct `app_id`, the review data can be accessed efficiently.
- ✅ The sentiment analysis shows a clear view of how **customers feel** about the service (positive, negative, neutral).
- ✅ There are interesting mismatches observed between `score` and `sentiment`, e.g.,:
  - 5-star rating with negative comments
  - 1-star rating with positive praise
  This could imply **user misunderstanding**, **accidental rating**, or **rating bias**, which can be crucial feedback for companies.
- ✅ The results can be valuable for **online lending companies** to:
  - Understand what customers are **complaining about** (e.g., approval process, collection behavior, app bugs)
  - See what **aspects customers appreciate**, to help maintain and improve features

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/052403ce-45a7-429a-949c-7df99d2c97bc" alt="PinjemSeratusPinjemDuluSeratusGIF" />
  <br/>
  <i>Hati-hati sama kata" ini ges 😂</i>
</p>


## 🚀 Future Development

In the next stage, this project can be extended with:

- 🔬 **Multi-class Classification**:
  - Group sentiments into specific topics such as:
    - Loan approval issues
    - Customer service complaints
    - App UI/UX problems
    - Repayment issues
    - Collection or billing behavior
- 🧠 Use topic modeling (e.g., LDA) or manually labeled training sets to detect these themes.
- 📅 Time series analysis: Tracking sentiment evolution over time
- 📲 Dashboard integration using Streamlit or Dash for interactive review monitoring

---

## 🛠️ Tech Stack & Libraries

- Python
- `google-play-scraper`
- `transformers`, `torch`
- `pandas`, `numpy`
- `matplotlib`, `seaborn`, `plotly`
- `wordcloud`
- `scikit-learn`

---
