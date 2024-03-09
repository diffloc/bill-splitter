import operator


sorted_books = dict(sorted(books.items(), key=operator.itemgetter(1)))

shortest_book = min(books.items(), key=operator.itemgetter(1))[0]
longest_book = max(books.items(), key=operator.itemgetter(1))[0]

print(shortest_book)
print(longest_book)
