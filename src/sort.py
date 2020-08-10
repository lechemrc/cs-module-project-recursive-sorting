from book import Book
import time
import csv

def insertion_sort(books):
    # loop through len-1 elements
    for i in range(1, len(books)):
        temp = books[i]
        j = i
        while j > 0 and temp.genre < books[j - 1].genre:
            # shift left until correct genre found
            books[j] = books[j - 1]
            j -= 1
        # insert at correct position
        books[j] = temp

    return books

# Version A: Conventional, recursive Quick Sort
def quick_sort_A(books):
    # BASE - we are trying to sort a single element
    if len(books) == 1:
        return books

    # Recursive ---- 
    # Choose a pivot
    pivot = books[0]
    LHS = []
    RHS = []
    for i in range(1, len(books)):
        if books[i] < pivot:
            # Move to LHS
            LHS.append(books[i])
        elif books[i] >= pivot:
            # Move to RHS
            RHS.append(books[i])

    return quick_sort_A(LHS) + [pivot] + quick_sort_A(RHS)


# Version B:
# NOT done in place because for large inputs, we
# exceed Python's maximum recursion depth with 
# in-place Quick Sort
def quick_sort_B( books ):
    # STRETCH: implement Quick Sort for larger datasets

    return books


def book_sort(books):
    # STRETCH: combine Insertion & Quick Sort for
    # an improved sorting algorithm
    
    return books

# Read in book data from CSV file
# provided by https://github.com/uchidalab/book-dataset
with open('src/book_data.csv') as csvfile:
    my_books_long = []
    data = csv.DictReader(csvfile)
    for book in data:
        #print(book['title'], book['author'], book['genre'])
        my_books_long.append(Book(book['title'], book['author'], book['genre']))
    my_books_medium = my_books_long[0:997]
    my_books_short = my_books_long[0:10]

print("***********~Test with 10 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_short)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

start = time.time()
sorted_books = quick_sort_A(my_books_short)
end = time.time()
print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n***********~Test with ~1,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_medium)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

start = time.time()
sorted_books = quick_sort_A(my_books_medium)
end = time.time()
print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n**********~Test with +2,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_long)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_B(my_books_long)
# end = time.time()
# print("Quick Sort (B) took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = book_sort(my_books_long)
# end = time.time()
# print("Book Sort took:       " + str((end - start)*1000) + " milliseconds\n")