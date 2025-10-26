"""Generate team page from template using Jinja2."""

import os
from jinja2 import Environment, FileSystemLoader
import json
import datetime
import os
from collections import defaultdict
from typing import Dict, List, Any

import requests


class GitHubContributionsAnalyzer:
    def __init__(self, org_name: str, token: str = None):
        """
        Initialize the analyzer with organization name and optional GitHub token.

        Args:
            org_name (str): Name of the GitHub organization
            token (str, optional): GitHub Personal Access Token
        """
        self.org_name = org_name
        self.headers = {
            'Accept': 'application/vnd.github.v3+json'
        }
        if token:
            self.headers['Authorization'] = f'token {token}'
        self.base_url = 'https://api.github.com'

    def get_org_repos(self) -> List[str]:
        """Fetch all repositories in the organization."""
        repos = []
        page = 1
        while True:
            response = requests.get(
                f'{self.base_url}/orgs/{self.org_name}/repos',
                headers=self.headers,
                params={'page': page, 'per_page': 100}
            )
            response.raise_for_status()
            data = response.json()
            if not data:
                break
            repos.extend([repo['name'] for repo in data])
            page += 1
        return repos

    def get_repo_commits(self, repo_name: str, username: str) -> datetime.datetime:
        """Get the most recent commit date for a user in a repository."""
        try:
            response = requests.get(
                f'{self.base_url}/repos/{self.org_name}/{repo_name}/commits',
                headers=self.headers,
                params={'author': username, 'per_page': 1}
            )
            response.raise_for_status()
            commits = response.json()
            if commits:
                return datetime.datetime.strptime(
                    commits[0]['commit']['committer']['date'],
                    '%Y-%m-%dT%H:%M:%SZ'
                )
        except:
            pass
        return datetime.datetime.min

    def get_repo_contributors(self, repo_name: str) -> List[Dict[str, Any]]:
        """Fetch contributors for a specific repository."""
        contributors = []
        page = 1
        while True:
            response = requests.get(
                f'{self.base_url}/repos/{self.org_name}/{repo_name}/contributors',
                headers=self.headers,
                params={'page': page, 'per_page': 100}
            )
            if response.status_code == 404:
                return []
            response.raise_for_status()
            try:
                data = response.json()
            except json.JSONDecodeError:
                break
            if not data:
                break
            contributors.extend(data)
            page += 1
        return contributors
    
    def get_user_name(self, username: str) -> str:
        """Fetch the name of a user from their GitHub profile."""
        try:
            response = requests.get(
                f'{self.base_url}/users/{username}',
                headers=self.headers
            )
            response.raise_for_status()
            data = response.json()
            return data.get('name', username)
        except requests.RequestException:
            return username

    def analyze_contributions(self) -> Dict[str, Dict[str, Any]]:
        """Analyze contributions across all repositories."""
        repos = self.get_org_repos()
        contributions = defaultdict(lambda: {
            'total_commits': 0,
            'repos_contributed': {},  # Changed to dict to store dates
            'profile_url': ''
        })

        for repo in repos:
            print(f"Analyzing repository: {repo}")
            contributors = self.get_repo_contributors(repo)

            for contributor in contributors:
                username = contributor['login']
                if '[bot]' in username:
                    continue

                contrib_count = contributor['contributions']

                # Get the most recent commit date for this user in this repo
                last_commit_date = self.get_repo_commits(repo, username)

                contributions[username]['total_commits'] += contrib_count
                contributions[username]['repos_contributed'][repo] = last_commit_date
                contributions[username]['profile_url'] = contributor['html_url']

        for username in contributions:
            name = self.get_user_name(username)
            print(f"Fetching name for {username}: {name}")
            contributions[username]['name'] = self.get_user_name(username)
        return contributions

    def generate_repo_link(self, repo_name: str) -> str:
        """Generate an italicized markdown link for a repository."""
        return f"*[{repo_name}](https://github.com/{self.org_name}/{repo_name})*"

    def generate_markdown(self, contributions: Dict[str, Dict[str, Any]]) -> str:
        """Generate a markdown report of contributions."""
        markdown = f"# Contributors to {self.org_name}\n\n"

        # Convert to list and sort by number of repos, then by total commits
        sorted_contributors = sorted(
            [
                (
                    username,
                    data['profile_url'],
                    len(data['repos_contributed']),
                    data['total_commits'],
                    # Sort repos by last commit date
                    sorted(
                        data['repos_contributed'].items(),
                        key=lambda x: x[1],
                        reverse=True
                    )
                )
                for username, data in contributions.items()
            ],
            key=lambda x: (-x[2], -x[3])  # Sort by -repo_count, then -total_commits
        )
        contributors = [
            {
                "github": username,
                "name": contributions[username]['name'],
                "repos": [r[0] for r in repos[:5]],
                "more_repos": repo_count - 5 if repo_count > 5 else None,
            } for username, profile_url, repo_count, total_commits, repos in sorted_contributors
        
        ]

        # Setup Jinja2 environment
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('src/dynamic/contributors_template.md')

        # Render template with contributor data
        output = template.render(contributors=contributors)
       

        return output


def main():
    # Get GitHub token from environment variable (optional)
    token = os.getenv('GH_API_KEY')

    # Initialize analyzer
    org_name = "teamtomo"
    analyzer = GitHubContributionsAnalyzer(org_name, token)

    # Analyze contributions
    print("Analyzing contributions...")
    contributions = analyzer.analyze_contributions()

    # Generate markdown
    print("Generating markdown report...")
    markdown = analyzer.generate_markdown(contributions)

    # Save to file
    with open("src/site/team.md", "w") as f:
        f.write(markdown)

    print("Team page generated successfully!")

main()
 
