import os
from random import randint
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Initialize commit counter
total_commits = 0

# Loop through the number of days in the last week
for i in range(365, 371):  # Last 7 days
    num_commits_today = randint(1, 4)
    total_commits += num_commits_today  # Count commits for the day
    for j in range(num_commits_today):  # Random number of commits per day
        commit_date = current_date - timedelta(days=i)
        date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        with open('file.txt', 'a') as file:
            file.write(f'Commit on {date_str}\n')
        os.system(f'git add .')
        os.system(f'git commit --date="{date_str}" -m "commit on {date_str}"')

# Push the commits to the main branch
os.system('git push -u origin main')
