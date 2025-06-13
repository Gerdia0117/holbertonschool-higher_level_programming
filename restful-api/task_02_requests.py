#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Print the status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()

        # Print all post titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()

        # Structure the data into a list of dictionaries
        structured_posts = [{
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        } for post in posts]

        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
