# Text-classification-for-social-media-posts
 🚀 Social Media Post Topic Classifier

This is a simple Python application that uses Hugging Face's `transformers` library to classify social media posts into a wide range of possible topics **without any training data**. It leverages the power of **zero-shot learning** to determine the most relevant topic for any given post.

🔍 Features
- 🔗 Zero-shot classification using pre-trained NLP models
- ✅ No need for labeled data or training
- 🧠 Classifies posts into broad categories like sports, politics, entertainment, etc.
- 🖥️ Easy-to-use command-line interface


🧰 Requirements
Make sure you have Python installed, then install the following dependencies:
pip install transformers torch

How to Use
Clone this repository or copy the Python script.
Run the script using Python:
python classify_posts.py
Type or paste any social media post (tweet, Instagram caption, etc.).
Get the predicted topic with confidence score.
Type exit to quit the program.

📚 Example
Input:
Enter social media post: The new iPhone 15 Pro camera is insane! 📱📷
Output:
🏷️ Predicted Topic: technology (confidence: 0.92)
