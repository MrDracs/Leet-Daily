import requests
import os

# Define the GraphQL query
query = """
{
  activeDailyCodingChallengeQuestion {
    question {
      titleSlug
    }
  }
}
"""

# Define the URL for the LeetCode GraphQL API
url = "https://leetcode.com/graphql"

# Send a POST request to the GraphQL API with the query
response = requests.post(url, json={'query': query})

# Check if the request was successful
if response.status_code == 200:
    # Extract the slug from the response JSON
    data = response.json()
    slug = data['data']['activeDailyCodingChallengeQuestion']['question']['titleSlug']
    url = f"https://leetcode.com/problems/{slug}/"
    print(f"Today's LeetCode Daily Problem: https://leetcode.com/problems/{slug}/")
else:
    print("Failed to fetch the daily problem.")

os.system(f"start {url}")