from instabot import Bot
bot=Bot()
log_in=bot.login((username='myselfsomraj',password=''))
bot.unfollow('white_chilis')
bot.follow('white_chilis')
bot.send_massage(text='Hi i am somraj mondal',user_ids='white_chilis')
bot.upload_photo('20220216_144127.jpg',caption="This side Somraj")
followers=bot.get_user_followers('myselfsomraj')
for followerid in followers:
  print(bot.get_user_followers(followerid))
