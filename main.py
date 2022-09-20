from instabot import *
bot=Bot()
log_in=bot.login((username='myselfsomraj',password=''))
bot.unfollow('white_chilis')
bot.follow('white_chilis')
bot.send_massage(text='Hi i am somraj mondal',user_ids='white_chilis')
bot.upload_photo()
