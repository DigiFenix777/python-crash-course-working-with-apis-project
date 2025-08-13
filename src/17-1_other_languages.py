import requests
import random

# Make an API call for a random programming language and check the response.
langs = ['python', 'java', 'go', 'javascript', 'ruby', 'c++']
rand_lang = random.choice(langs)
url = "https://api.github.com/search/repositories"
url += f"?q=language:{rand_lang}+sort:stars+stars:>10000"
print(f"Language: {rand_lang}")

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response to a dictionary.
response_dict = r.json()

# Process results.
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about each repository.")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
