#!/usr/bin/python3
"""Python script to fetch posts from JSONPlaceholder using requests.get()"""
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        formatted_posts = []

        for post in posts:
            new_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            formatted_posts.append(new_post)


        with open("posts.csv", mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted_posts)
