#!/usr/bin/env python
# coding: utf-8

# In[1]:


questions = {
    "strong":"Do ye like yer drinks strong?",
    "salty": "Do ye like it with salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}


# In[2]:


ingredients = {
    "strong": ["glug of rum","slug of whisky","splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twitst of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


# In[18]:


import random
def bartender():
    #guideline for users
    print('Insert "Y" for yes and "N" for no.')
    for taste in questions:
        answer = ''
        #force customers to give the approriate answers:
        while answer.lower() != "y" and answer.lower() != "n":
            answer = input(questions[taste]+' ')
        #conditions:
        if answer.lower() == "y":
            result = 'I might give you a/an ' + random.choice(ingredients[taste]) +'.'
            break
    return result    

        


# In[19]:


bartender()


# In[ ]:





# In[ ]:





# In[ ]:




