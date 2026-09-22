import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# Load books
books = pd.read_csv(
    "Books.csv",
    usecols=[
        "ISBN",
        "Book-Title",
        "Book-Author",
        "Year-Of-Publication",
        "Publisher",
        "Image-URL-S",
        "Image-URL-M",
        "Image-URL-L"
    ],
    low_memory=False
)

# Load ratings
ratings = pd.read_csv(
    "Ratings.csv",
    usecols=["User-ID", "ISBN", "Book-Rating"]
)

# Remove books with zero ratings
ratings = ratings[ratings["Book-Rating"] > 0]

# Combine ratings with book information
df = ratings.merge(books, on="ISBN")

# Keep users who have rated at least 5 books
user_counts = df["User-ID"].value_counts()
active_users = user_counts[user_counts >= 5].index
df = df[df["User-ID"].isin(active_users)]

# Keep the 2000 most-rated books
book_counts = df["Book-Title"].value_counts()
popular_books = book_counts.head(2000).index
df = df[df["Book-Title"].isin(popular_books)]

# Create user-book matrix
pivot = df.pivot_table(
    index="Book-Title",
    columns="User-ID",
    values="Book-Rating"
).fillna(0)

# Calculate similarity
similarity = cosine_similarity(pivot)

similarity_df = pd.DataFrame(
    similarity,
    index=pivot.index,
    columns=pivot.index
)


def recommend(book_name="", mood="", n=8):

    # If a book name is provided, recommend similar books
    if book_name.strip():

        matches = [
            book for book in similarity_df.index
            if book_name.lower() in book.lower()
        ]

        if matches:
            selected_book = matches[0]

            recommendations = similarity_df[
                selected_book
            ].sort_values(ascending=False)[1:n + 1]

            result = []

            for title in recommendations.index:

                info = books[
                    books["Book-Title"] == title
                ].iloc[0]

            result.append({
                   "title": title,
                   "author": info["Book-Author"],
                   "year": info["Year-Of-Publication"],
                   "publisher": info["Publisher"],
                   "image": info["Image-URL-M"]
             })

            return result

    # If no book is entered, recommend popular books
    # based on the selected mood.

    mood_keywords = {

        "Happy": [
            "love", "happy", "friend", "family",
            "summer", "holiday", "fun", "life"
        ],

        "Sad": [
            "death", "loss", "alone", "sad",
            "memory", "heart", "cry"
        ],

        "Thriller": [
            "murder", "killer", "crime", "dead",
            "secret", "detective", "dark", "death"
        ],

        "Motivational": [
            "success", "life", "dream", "power",
            "change", "future", "work", "leadership"
        ]
    }

    # Start with popular books
    popular = (
        df.groupby("Book-Title")["Book-Rating"]
        .agg(["mean", "count"])
        .reset_index()
    )

    popular["score"] = (
        popular["mean"] * 0.7 +
        popular["count"] * 0.3
    )

    # Apply mood filtering
    if mood in mood_keywords:

        keywords = mood_keywords[mood]

        pattern = "|".join(keywords)

        mood_books = popular[
            popular["Book-Title"]
            .str.lower()
            .str.contains(pattern, na=False)
        ]

        # If enough mood books are found, use them
        if len(mood_books) >= n:
            popular = mood_books

    # Sort by recommendation score
    popular = popular.sort_values(
        "score",
        ascending=False
    )

    result = []

    for title in popular["Book-Title"].head(n):

        info = books[
            books["Book-Title"] == title
        ].iloc[0]

        result.append({
           "title": title,
           "author": info["Book-Author"],
           "year": info["Year-Of-Publication"],
           "publisher": info["Publisher"],
         "image": info["Image-URL-M"]
})
    return result