import pickle

class TBook:
    author=''
    title=''
    age=''
book= TBook()
book.author= 'Босова Л.Л'
book.title='Практикум по информатике. 7 класс'
book.age=2015

library=[]
count=5
for i in range(count):
    library.append(TBook())
    library[i].author="Автор "+str(i+1)
    library[i].title='Название '+str(i+1)
    library[i].age=123*(i+1)

for i in range(len(library)):
    print(library[i].author, library[i].title, library[i].age, sep=' | ')

f=open('library.dat','wb')
pickle.dump(library, f)
f.close()

f=open('library.dat','rb')
library_2= pickle.load(f)
f.close()
print()
for i in range(len(library_2)):
    print(library_2[i].author, library_2[i].title, library_2[i].age, sep=' | ')