import pandas as pd
from sentistrength import PySentiStr
senti = PySentiStr()
senti.setSentiStrengthPath('SentiStrengthCom.jar') # Note: Provide absolute path instead of relative path
senti.setSentiStrengthLanguageFolderPath('SentStrength_Data_Sept2011') # Note: Provide absolute path instead of relative path
result = senti.getSentiment('i love my grilfriend')
print (result)