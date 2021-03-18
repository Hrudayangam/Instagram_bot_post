# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:18:53 2021

@author: hrudayangam
"""

from instabot import Bot 


bot = Bot()
 
bot.login(username = "bun.ty_", 
		password = "redacted", '''use_cookie=False,generate_all_uuids=(False)''') 

bot.upload_photo(r"C:/Users/hruda/.spyder-py3/myqr.png", 
				caption ="panda") 


#if you are getting the error "KeyError: 'ds_user'"
#use use_cookie=False,generate_all_uuids=(False) in the bot.login 
