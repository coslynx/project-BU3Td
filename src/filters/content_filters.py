# File: src/filters/content_filters.py (Python)

# Import necessary packages
import json
import logging

# Function to filter inappropriate content in messages
def filter_inappropriate_content(message):
    inappropriate_words = ["bad_word1", "bad_word2", "bad_word3"]
    for word in inappropriate_words:
        if word in message:
            return True
    return False

# Function to log filtered messages
def log_filtered_message(user_id, message):
    logging.info(f"Inappropriate content filtered for user {user_id}: {message}")

# Function to apply content filters to messages
def apply_content_filters(user_id, message):
    if filter_inappropriate_content(message):
        log_filtered_message(user_id, message)
        return "Your message contains inappropriate content and has been filtered."
    return None