#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    # Make the request to Reddit
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if subreddit doesn't exist
    if response.status_code == 404:
        print("OK")  # Output "OK" when subreddit is non-existent
        return
    
    # Check if the response is successful and contains data
    if response.status_code != 200:
        print("OK")  # Output "OK" for any other error (like server issues)
        return
    
    try:
        # Try parsing the JSON response
        results = response.json().get("data")
        if results and "children" in results:
            for c in results["children"]:
                print(c.get("data").get("title"))
        else:
            print("OK")  # Output "OK" if no data is available (e.g., empty subreddit)
    except ValueError:
        # If response cannot be parsed as JSON, output "OK"
        print("OK")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])  # Run the function with the subreddit name passed as a command-line argument
    else:
        print("Usage: python3 1-main.py <subreddit>")
