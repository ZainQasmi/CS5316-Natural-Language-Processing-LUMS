import csv

names=[]
ages=[]
with open('sentiment_labelled_sentences/imdb_labelled.txt','r') as f:
    # next(f) # skip headings
    reader=csv.reader(f,delimiter='\t')
    for nameage in reader:
        names.append(nameage)
        # names.append(name)
        # ages.append(age) 

print(names)[1][0]
# ('Mark', 'Matt', 'John', 'Jason', 'Matt', 'Frank', 'Frank', 'Frank', 'Frank')
# print(ages)
# ('32', '29', '67', '45', '12', '11', '34', '65', '78')