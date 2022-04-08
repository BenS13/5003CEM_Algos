import newspaper
from newspaper import Article
import time

def get_headlines():

    URLs = ['http://www.foxnews.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]
            #'https://www.nytimes.com/',
           # 'https://www.lemonde.fr',
         #   'https://lefigaro.fr',
          #  'https://www.dailystar.co.uk/',
           # 'https://www.thesun.co.uk']

    for url in URLs:
        start = time.time()
        result = newspaper.build(url, memoize_articles=False)
        #print('\n''The headlines from %s are' % url, '\n')
        for i in range(1,6):
            art = result.articles[i]
            art.download()
            art.parse()
            print(art.title)
            #print("a")
        end = time.time()
        #print("Time taken:", (end-start), '\n')

if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=1)             
    print(elapsed_time) 
