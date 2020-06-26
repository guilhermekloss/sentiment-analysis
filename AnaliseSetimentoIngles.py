import pandas as pd
from sentistrength import PySentiStr
senti = PySentiStr()
senti.setSentiStrengthPath('SentiStrengthCom.jar') # Note: Provide absolute path instead of relative path
senti.setSentiStrengthLanguageFolderPath('SentStrength_Data_Sept2011') # Note: Provide absolute path instead of relative path

str_arr = ['What a lovely day', 'What a bad day']

result = senti.getSentiment(str_arr)
print (result)
result = senti.getSentiment(str_arr, score='scale')
print (result)

# OR, if you want dual scoring (a score each for positive rating and negative rating)
result = senti.getSentiment(str_arr, score='dual')
print(result)

# OR, if you want binary scoring (1 for positive sentence, -1 for negative sentence)
result = senti.getSentiment(str_arr, score='binary')
print(result)

# OR, if you want trinary scoring (a score each for positive rating, negative rating and neutral rating)
result = senti.getSentiment(str_arr, score='trinary')
print(result)