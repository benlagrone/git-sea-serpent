import json
import os
import subprocess
from datetime import datetime, timedelta

# Load pixel art from JSON
with open('pixel_art.json', 'r') as file:
    pixel_art = json.load(file)['art']

# Calculate the start date for the pixel art on the GitHub contributions graph
# Assuming today is March 17, 2025, and we want to start the art exactly one year ago
today = datetime(2025, 3, 17)
start_date = today - timedelta(weeks=52)

def create_commits_for_day(date, commit_count):
    for _ in range(commit_count):
        # Set GIT_AUTHOR_DATE and GIT_COMMITTER_DATE
        env = {
            'GIT_AUTHOR_DATE': date.strftime('%Y-%m-%d 12:00') + ' +0000',
            'GIT_COMMITTER_DATE': date.strftime('%Y-%m-%d 12:00') + ' +0000',
            **os.environ,
        }
        # Create an empty commit with the specified date
        subprocess.run(['git', 'commit', '--allow-empty', '-m', 'Pixel Art Commit'], env=env)

def generate_pixel_art_commits():
    # Iterate through each day of the week (Sunday=0, ..., Saturday=6)
    for day_index, daily_commits in enumerate(pixel_art):
        # Iterate through each week
        for week_offset, commit_count in enumerate(daily_commits):
            if commit_count > 0:  # Only generate commits for days with a non-zero value
                # Calculate the date for the commit
                commit_date = start_date + timedelta(weeks=week_offset, days=day_index)
                create_commits_for_day(commit_date, commit_count)

if __name__ == '__main__':
    generate_pixel_art_commits()
    # Push the commits to GitHub
    subprocess.run(['git', 'push'])