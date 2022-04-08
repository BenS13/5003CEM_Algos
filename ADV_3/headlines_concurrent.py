import newspaper
from newspaper import Article
from concurrent.futures import ThreadPoolExecutor               #Import library for concurency

'''
input: url
output: list containing headlines
'''
def get_headline_one(url):
    result = newspaper.build(url, memoize_articles=False)       #Get info from url
    headline = []                                               #Array to store each headline
    headline.append('The headlines from %s are' % url)
    for i in range(1,6):                                        #Repeat 5 times
        art = result.articles[i]                                #Find the info we want
        art.download()                                          #Sanatise it
        art.parse()
        data = art.title
        headline.append(data)                                   #Append headline to array
    return headline
    
'''
input: none
output: the threads which run the functions
'''
def get_headline_all():
    urls = ['http://www.foxnews.com/',                          #URL list
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]

    with ThreadPoolExecutor(max_workers=2) as executor:         #Start a pool with x number of workers
        return executor.map(get_headline_one, urls, timeout=60) #function passed into map

def print_headlines():                                          #call the function which returns list
    headlines = get_headline_all()
    for unique in headlines:                                    #Print all the headlines out nicley
        print('\n')
        for sentence in unique:
            print('\n', sentence)

if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("print_headlines()", setup="from __main__ import print_headlines", number=1)
                                                                #Time how long the process takes
    print(elapsed_time)