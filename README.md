How would we filter for all books with titles containing the word ‘Django’?
#YOU WOULD USE BOOK.OBJECTS.FILTER(BOOK__TITLE='DJANGO')
How would we filter for all books with tag ‘Fiction’?

# Book.objects.filter(Tag__name='Fiction')
How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!


book.objects.filter(Book__author='Django')

