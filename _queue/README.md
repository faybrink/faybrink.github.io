# Scheduled posts

Nothing in this folder is on the website. GitHub Pages skips folders whose
names start with an underscore.

Every morning at about 6:15 AM Central, the "Publish scheduled posts" action
(.github/workflows/scheduled-publish.yml) checks this folder. For each dated
folder (YYYY-MM-DD) whose date has arrived, it merges those files into the
site, records the date in published.txt, commits, and submits the new pages
to IndexNow.

- Each dated folder holds only the files that change that day.
- _base/ holds the live versions the queue was built from. The action uses
  them to keep any edits you make to the live site in the meantime.
- If one of your edits collides with a queued change, the action publishes
  nothing that day and the run shows as failed in the Actions tab. GitHub
  emails you when that happens.
- Don't add a file named .nojekyll to the site. It would make this folder
  public on your website.
