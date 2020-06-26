import pandas as pd
from sentistrength import PySentiStr
senti = PySentiStr()
senti.setSentiStrengthPath('SentiStrengthCom.jar') # Note: Provide absolute path instead of relative path
senti.setSentiStrengthLanguageFolderPath('portuguese') # Note: Provide absolute path instead of relative path


#-1 (not negative) to -5 (extremely negative)
#1 (not positive) to 5 (extremely positive)

str_arr = [
    'Que dia maravilhoso', 
'Que dia ruim',
'Vcs são incriveis, vcs conseguem tirar Pessoas da depressão, obrigada por me fazer sorrir todos os dias , espero de vdd poder encontrar vcs e dar um abraço mto apertado!!!!!😪❤❤',
'No vídeo de hoje, os integrantes da LOUD tiraram um tempo pra conversar com os inscritos do Discord por chamada de vídeo. Eles entraram de surpresa na call do Discord e surpreenderam.']

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