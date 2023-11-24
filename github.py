import requests

# Ersetzen Sie YOUR_ACCESS_TOKEN durch Ihren GitHub-Personal-Access-Token
headers = {
    "Authorization": "token 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",
    "Accept": "application/vnd.github.v3+json"
}


def get_top_repos_by_topic(topic):
    url = f"https://api.github.com/search/repositories?q=topic:{topic}&sort=stars&order=desc"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()['items']
    else:
        response.raise_for_status()

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_user_contributions(username):
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        contributions = [event for event in response.json() if event['type'] in ['PushEvent', 'PullRequestEvent']]
        return len(contributions)
    else:
        response.raise_for_status()