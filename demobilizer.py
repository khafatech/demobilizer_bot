#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

#===============
# Python Script for making mobile URLs non-mobile URLs
#  By /u/zd9
#
# Written in Python 2.7.5
#===============

import praw
import re
import sys
import pickle

# pull in onboard data and establish connection
username = "" #USERNAME GOES HERE
password = "" #PASSWORD GOES HERE
user_agent = ("simple praw script for "
              "making mobile URLs non-mobile URLs "
              "by /u/zd9")
reddit = praw.Reddit(user_agent = user_agent)
reddit.login(username = username, password = password)

# pull comments
subreddit_comments = reddit.get_comments('all')

pickle_file = open('processed.txt', 'r')
already_done = set(pickle.load(pickle_file))
pickle_file.close()

for comment in subreddit_comments:
    pattern1 = re.compile("(?P<mobile>://(?:.{1,12}\.)?m\.)")
    match = pattern1.search(comment.body)
    
    if not match:
        continue

    if match and comment.id not in already_done:

        url_pattern = re.compile("(?P<url>http.{1,}?(?:\s|\)|\Z))")

        url = url_pattern.search(comment.body)

        if not url:
            pickle_mod = open('processed.txt', 'w')
            already_done.add(comment.id)
            pickle.dump(already_done, pickle_mod)
            pickle_mod.close()
            continue
        if url:
            desk = url.group('url')
            desk_url = desk.replace('m.', '')
            desk_url = desk_url.rstrip(')')
        
            comment.reply(u"I've detected a mobile URL in your comment.\n\n**[Here's](%s) the equivalent non-mobile URL**.\n\n---\n\n*^[Bugs/Questions/Suggestions/Improvements?](http://www.reddit.com/message/compose/?to=zd9&subject=RE:+demobilizer+bot) ^| ^[Source\xa0Code](https://github.com/zd9/demobilizer_bot)*" % (desk_url))
        
        pickle_mod = open('processed.txt', 'w')
        already_done.add(comment.id)
        pickle.dump(already_done, pickle_mod)
        pickle_mod.close()


#===============
# Sample Comment reply:
#
#   I've detected a mobile URL in your comment.
#
#   **[Here's](desk_url) the equivalent non-mobile URL**.
#   ------------------------------
#   *^[Bugs/Questions/Suggestions/Improvements?](http://www.reddit.com/message/compose/?to=zd9&subject=RE:+demobilizer+bot) ^| ^[Source code](https://github.com/zd9/demobilizer_bot)*
#===============
