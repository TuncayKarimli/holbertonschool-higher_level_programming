#!/usr/bin/python3
"""
This module provides functions to fetch posts from a REST API and either
print their titles or save the data into a CSV file.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints the status code and titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    # Mandatory firewall bypass header (kept for consistency with your environment)
    headers = {'cfclearance': 'true'}
    
    response = requests.get(url, headers=headers)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches posts and saves id, title, and body into posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {'cfclearance': 'true'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data into a list of specific dictionaries
        # Using a list comprehension as suggested in the hints
        data_to_save = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]
        
        # Writing to CSV using DictWriter
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data_to_save)
