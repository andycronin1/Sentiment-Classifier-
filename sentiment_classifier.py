#----------------------------------------------------------------------------------------------------------       
#Python Sentiment Classifier 

#The aim of this project was to write some code that could open several tweets, Analyse the tweet and find 
#the Number of Retweets, Number of Replies, Number of Positive words in the tweet, Number of Negative words
#in the tweet and the net score. It would then output these results to a csv file. 

#To do this, the punctuation had to be removed from the tweet and all words were converted to lower case. 
#Functions were written to carry this out. 
##----------------------------------------------------------------------------------------------------------
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(x): 
    for i in x: 
            if i in punctuation_chars: 
                x = x.replace(i, '')
    return x

def get_pos(x):
    count = 0
    x = x.split(' ')
    for i in x: 
        i = i.lower()
        i = strip_punctuation(i)
        if i in positive_words:
            count = count + 1 
    return count 


def get_neg(x):
    count = 0
    x = x.split(' ')
    for i in x: 
        i = i.lower()
        i = strip_punctuation(i)
        if i in negative_words:
            count = count + 1 
    return count 

initial_file = open("project_twitter_data.csv", 'r')
x = []
lines = initial_file.readlines()
header = lines[0]
field_names = header.strip().split(',')
#print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    no_retweets = vals[-2]
    no_replies = vals[-1]
    #print(vals)
    #print(vals[0])
    pos_score = get_pos(vals[0])
    neg_score = get_neg(vals[0])
    net_score = pos_score - neg_score 
    x.append((no_retweets,no_replies,pos_score,neg_score,net_score))
    #print(x)
print(x)   

outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for i in x:
    row_string = '{},{},{},{},{}'.format(i[0],i[1],i[2],i[2],i[4])
    outfile.write(row_string)
    outfile.write('\n')

outfile.close
