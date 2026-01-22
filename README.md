# 📊 Customer Review Analyzer using Data Analytics & GenAI

A simple Python project that combines Data Analytics, Visualization, and Generative AI to analyze customer reviews and generate AI-based summaries.

---

## 🚀 Project Overview

This project performs end-to-end customer review analysis by combining traditional data analytics techniques with Generative AI. It helps in understanding customer feedback, visualizing trends, and generating concise summaries automatically.

This project is ideal for college mini-projects, internships, and GitHub portfolios.

---

## 🛠️ Tech Stack

- Python
- Pandas
- Matplotlib
- WordCloud
- OpenAI API

---

## 📁 Project Structure

Customer-Review-Analyzer/
│
├── customer_review_analyzer.py   # Main Python script (EDA + GenAI)
├── requirements.txt              # Required Python libraries
├── README.md                     # Project documentation
│
└── data/
    └── reviews.csv               # Customer reviews dataset

---

## 📄 Dataset Description

The dataset (reviews.csv) contains customer feedback data used for analysis and summarization.

Columns:
- review_text – Customer review content
- rating – Rating given by the customer (1 to 5)

Sample Data:
review_text,rating
"The product is amazing! Battery lasts long.",5
"Terrible quality, broke in two days.",1

---

## ⚙️ Installation and Setup

Step 1: Clone the Repository
git clone https://github.com/your-username/Customer-Review-Analyzer.git
cd Customer-Review-Analyzer

Step 2: Install Required Dependencies
pip install -r requirements.txt

---

## 🔑 OpenAI API Key Configuration

Open the file customer_review_analyzer.py and replace the placeholder with your OpenAI API key

---

## ▶️ How to Run the Project

Run the following command from the project directory:

python customer_review_analyzer.py

---

## 📊 Output and Results

After running the project, the following outputs are generated:

- Bar chart showing rating distribution
- Word cloud visualizing common words in reviews
- AI-generated one-line summaries for customer reviews

Example:
Review: Terrible quality, broke in two days.
Summary: The customer is dissatisfied with the product quality and durability.

---

## 🎯 Use Cases

- Customer feedback and review analysis
- Automated review summarization using GenAI
- Beginner-friendly Data Analytics and AI integration project
- Resume and GitHub portfolio project

---

## 🔮 Future Enhancements

- Streamlit-based interactive dashboard
- Sentiment classification (Positive/Negative)
- Multi-language review support
- Offline GenAI models using HuggingFace

---

## 👩‍💻 Author

Bhoomika Rai  
Python | Data Analytics | Generative AI

---

## ⭐ Acknowledgements

- OpenAI
- Pandas and Matplotlib community
- Kaggle (dataset inspiration)
