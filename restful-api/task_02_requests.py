import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetch posts and print their titles."""
    try:
        response = requests.get(API_URL)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get("title"))
    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_and_save_posts():
    """Fetch posts and save them to posts.csv (id, title, body)."""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            posts = response.json()
            # Extract id, title, and body only
            data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

            # Write to CSV
            with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

