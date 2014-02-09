# README: Demobilizer Reddit Bot

This is a bot for reddit that will find mobile links in comments and "un-mobilize" them.

## Requirements:
- Python 2.7
	- Downloadable from [python.org](http://python.org)
- Praw (the Python Reddit API Wrapper): for Reddit API calls
	- To install Praw, use `sudo pip install praw`, or, if you don't have pip, install pip with `sudp easy_install pip`.

## To Run:

0. Download the script and processed.txt to a safe place.
1. In Terminal, go to the directory of the script and run `chmod +x {script_name}.py` to make it executable.
2. Put your account name and password in the script where the variables `username` and `password` are defined.
3. Be sure to change the comment reply message in `line 59` to what you want. Use Reddit markdown formatting and Python escape codes to format correctly.
4. Run the bot with cron:
	1. `cd ~`
	2. `crontab -e`
	3. Press `i` to edit
	4. On a new line, put a new cronjob. I use the timing `*/2 * * * *`, which runs every 2 minutes, 24/7. The job to be performed on this schedule should be: `cd ~/Path/to/script/folder/; python {script_name}.py`
	5. To exit editing and save changes, press `esc`, then `:`, then `w`, then `q`.
	6. Check that you crontab file was changed with `crontab -l`.
5. Be sure to manage the bot diligently by adding banned/ignored subreddits to the list.
