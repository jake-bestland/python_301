# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import praw
from pathlib import Path


reddit = praw.Reddit(
    client_id="*InsertCLIENT_ID*",
    client_secret="*InsertCLIENT_SECRET*",
    password="*InsertPASSWORD*",
    user_agent="ChangeMeClient/0.1 by YourUsername",
    username="*InsertUSERNAME*",
)

subreddit = reddit.subreddit("recipes")
BASE_URL = "https://www.reddit.com"
recipe_files = ""

for submission in subreddit.top(time_filter="all", limit=25):
    link = BASE_URL + submission.permalink
    recipe_files += (f"<li><a href='{link}'>{submission.title}</a></li>")

main_page = f"<h1>Recipe Colletction</h1><p>This page contains some recipes gathered from Reddit posts</p><ul>{recipe_files}</ul>"
mp = Path().home().joinpath("Desktop").joinpath("recipes").joinpath("main_recipe_page.html")
mp.write_text(main_page)

