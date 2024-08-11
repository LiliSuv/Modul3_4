root_word='округ'
other_words='окраина','труд','весна', 'круг','окрошка','субокруг', 'листва', 'округлость'
def single_root_words(root_word,*other_words):
    same_words=[]
    for k in range (8):
        y=other_words[k]
        if any (i in other_words[k] for i in  [root_word])  > 0:
            same_words.append(other_words[k])
        elif any (i in root_word for i in [ other_words[k]])>0:
            same_words.append (other_words[k])
    print( same_words)
single_root_words(root_word,*other_words)