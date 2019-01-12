from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
 
import requests
 
# getting text document from Internet
text = requests.get('https://en.wikipedia.org/wiki/Shah_Jahan').text
 
#print ('Summary:')
#print (summarize(text, ratio=0.01))
 
print ('\nKeywords:')
print (keywords(text, ratio=0.01))