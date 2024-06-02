import requests
import csv

def fetch_and_print_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print status code
    print(f"Status Code: {response.status_code}")

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse fetched data into JSON
        posts = response.json()
        
        # Iterate through the parsed JSON data and print titles of all the posts
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse fetched data into JSON
        posts = response.json()
        
        # Create a list to store post data
        post_data = []
        
        # Structure the data into a list of dictionaries
        for post in posts:
            post_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        
        # Write data into a CSV file
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data rows
            for post in post_data:
                writer.writerow(post)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
