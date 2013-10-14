# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 06:16:37 2013

@author: localadmin
"""

from utils import case_collection
#from datatime import data

class Message:
    """message = self.message
    user = self.user
    tags = self.tags
    """
    
    def get_message_from_db(self):
        wrap_db = case_collection("workshop", "messages").find_one()
        self.message = wrap_db["message"]
        self.user = wrap_db["user"]
        self.tags = wrap_db["tags"]
        
    def add_new_message(self, **kwargs):
        case_collection("workshop", "messages").insert(kwargs)
            
    def get_message_by_key(self, **kwargs):
        
        wrap_db = case_collection("workshop", "messages").find(kwargs)        
        massage_list = []        
        
        for key in wrap_db:
            del(key["_id"])
            massage_list.append(key)
            #self.__dict__[key] = wrap_db[key]
        
        return massage_list
            
            
class User:
    """
    """
    def get_user_by_atribute(self, **kwargs):
        coursor = case_collection("workshop", "users").find_one(kwargs)
        for key in coursor:
            self.__dict__[key] = coursor[key]
            
    def get_list_all_users(self):
        coursor = case_collection("workshop", "users").find({})
        list_users = []
        for key in coursor:
            del(key["_id"])
            list_users.append(key)
        return list_users
        
    def get_description(self):
        coursor = case_collection("workshop", "users").find_one({})
        del(coursor["_id"])
        return coursor
        
    def is_user(self, username="admin", passwd="pasword"):
        coursor = case_collection("workshop", "users").find_one({
                                                "username":username, 
                                                "password":passwd})
                                                
        try:
            if (coursor["username"] == username) and (coursor["password"] == passwd):
                print True
                return True
        except:
            return False
        
        
        
        
        
if __name__ == '__main__':
    new_mess = Message()
    #print new_mess.get_message_by_key(tags="python")
    #new_mess.get_message_from_db()
    #print new_mess.get_message_by_tag("python")
    #print new_mess["message"]    
    #for key in new_mess:
    #    print key, "\n"
    usr = User()
    #print usr.get_list_all_users()
    #print usr.get_description()
    print usr.is_user("momel", "momelpass")
