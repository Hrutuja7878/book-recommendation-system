# 📚 AI-Based Book Recommendation System

An AI-based web application that recommends books based on user preferences and mood. The system uses Python, Flask, Pandas and Scikit-learn to generate personalized book recommendations.

## ✨ Features

* 📖 Book recommendations based on a selected book
* 😊 Mood-based recommendations
* 🔍 Book similarity using collaborative filtering
* 📊 Rating-based book analysis
* 🌐 Simple and attractive web interface
* 📚 Book information including title, author, publisher and publication year

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* HTML
* CSS
* JavaScript
* CSV Dataset

## 🧠 How It Works

The system uses the Book-Crossing dataset containing books, users and ratings.

For book-based recommendations, the system creates a user-book rating matrix and uses cosine similarity to find books that are similar based on user rating patterns.

For mood-based recommendations, the system uses predefined keywords related to different moods and combines them with book popularity and ratings.

## 📂 Project Structure

```text
book-recommendation-system/
│
├── app.py
├── book_recommendation.py
├── Books.csv
├── Ratings.csv
├── Users.csv
│
├── templates/
│   ├── index.html
│   └── explore.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        ├── main.jpg
        └── reading.jpg
```

## ▶️ How to Run

### 1. Install the required libraries

```bash
pip install flask pandas scikit-learn
```

### 2. Run the application

```bash
python app.py
```

### 3. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 🎯 Project Objective

The objective of this project is to demonstrate how machine learning concepts such as collaborative filtering and cosine similarity can be used to build a book recommendation system.

## 👩‍💻 Author

**Hrutuja Shejwal**

MCA Engineering Student
