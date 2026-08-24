Libry =  []
wish_list = []
book_one = str(input("Pleas enter a book name:"))
Libry.append(book_one)
book_too = str(input("do you add the new book? to add libry(prees enter to skip):"))
if book_too:
    Libry.append(book_too)
    print(f'the Libry now{Libry}')
else:
    print(Libry)
book_wash = str(input("Enter the name book you wish to have:"))
wish_list.append(book_wash)
Book_wishtoo = str(input("Enter the too(enter to skip):"))
if Book_wishtoo:
    wish_list.append(Book_wishtoo)
    print(f'the {wish_list}')
else:
    print(f'this {wish_list}')
Book_new = str(input("Enter the book you have in the whitlist(Enter to skip):"))
if Book_new:
    Libry.append(Book_new)
elif Book_new in Libry:
    wish_list.remove(Book_new)
    print(Libry)
    print(wish_list)
else:
    print(Libry)
    print(wish_list)
donate_book = str(input("enter the donaiten book enter to skip:"))
if donate_book in Libry:
    Libry.remove(Book_new)
    print(Libry)
else:
    print(f'the final Libry{Libry}')

print("Thank you for use program")
print("Copyright (c) 2026 [Mohammad alhawri]. All rights reserved.")
print("Licensed under the BSD 3-Clause License.")
