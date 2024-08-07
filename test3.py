#q1 
# def file_reader(filename):
#     with open(filename,'r') as in_data:
#         for line in in_data:
#             yield line
#             #in_data.readline()

# data = (file_reader('essay.txt'))
# for text in data:
#     print("\n",text)

# for text in data:
#     print(text)

#q3
# class Book:
#     def __init__(self,name,author,year):
#             self.name = name
#             self.author = author
#             self.year = year
#     def display_book(self):
#         print(f"Name: {self.name}, Author: {self.author}, Year: {self.year}")

# class Library:
#     def __init__(self):
#         self.catalogue = []

#     def add_to_catalogue(self,book):
#          self.catalogue.append(book)
#          print(f"{book.name} is added to library catalogue.")
    
#     def display_catalogue(self):
#          print(f'{self.catalogue}')
    
# class Customer:
#     def __init__(self,name,id):
#           self.name = name
#           self.id = id
#           self.borrowed = []
    
#     def borrow_book(self,book):
#         self.borrowed.append(book)
#         print(f"{book.name} has been borrowed from library.")
    
#     def return_book(self,book):
#          self.borrowed.remove(book)
#          print(f"{book.name} has been returned to the library.")

# lib = Library()

# lib.add_to_catalogue(Book('Python Prog','Zed Shaw',2022))
# lib.add_to_catalogue(Book('Intro to Java','ABCD',2023))
# #lib.display_catalogue()

# c1 = Customer('Harmehar',100)
# c1.borrow_book(Book('Python Prog','Zed Shaw',2022))
# c1.return_book(Book('Python Prog','Zed Shaw',2022))

#q3
import concurrent.futures
import time
st = time.perf_counter()

def chunker(itr):
    with open('data.txt','r') as in_file:
        for row in in_file:   
                in_data = in_file.readlines()
                for i in range(1,itr):
                    for  i in range(0,len(in_data), 20):
                        chunk = in_data[i:i+20]
                        #chunk_sum=0
                        for j in chunk:
                            j=j.split(",")
                            #print(j)
                            # l = sum([int(e.replace("\n", "")) for e in j])
                            for e in j:
                                w  = e.replace("\n", "")
                                w = int(w)
                print(w)
                                
# list_sum=0
# list_sum +=w
# chunk_sum +=(list_sum)
# return f'{chunk_sum}'
print(chunker(3))



# with concurrent.futures.ThreadPoolExecutor() as exe:
#     iterations = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     chunks = [exe.map(chunker,iterations)]
#     #print((chunks))
    
#     for r in concurrent.futures.as_completed(chunks):
#         list_sum , chunk_sum = 0,0
#         a = list()
#         a = r.result()
#         list_sum += int(a[20])
#         chunk_sum +=(list_sum)
#         print(f"Sum of each line using batches in 'data.txt' is: {chunk_sum}")
#         print(r.result())

ft = time.perf_counter()
print(f"Time taken for computation: {round(ft-st,5)} seconds.")