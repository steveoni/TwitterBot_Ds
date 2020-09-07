## Twitter Bot For Data Scientist

Implementation for a medium [post](https://towardsdatascience.com/twitter-bot-for-data-scientists-8f4242c4d876)

![bot](bot.jpg)

The repo shows how to implement some popular twitter bot and more especially, implement how data scientist can use the power of this bot in gathering dataset and deploying an intelligent bot using deep learning.

`bot/follow.py`  --- implementation of bot to monitor a particular set of people and also download all media content from such users tweet.

`bot/mention.py` ---- Obtain tweet in which you are mentioned, and then download the media content in such tweet.

`bot/monitor.py` ----  obtain tweet that have some particular keywords.

`bot/unrollthread.py` --- obtain a twitter thread and turn it into a text file.

For more details on how each of the bot work and how to deploy them to aws ec2, you can check out the medium [post](https://towardsdatascience.com/twitter-bot-for-data-scientists-8f4242c4d876)
