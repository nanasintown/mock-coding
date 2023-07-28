"""
Build a library with:
  - store all books
  - remember active books
  - remember last page in all books
  - show last reading page in active books

Classes:
  - Book class
      - title -> str
      - id (title may not unique)
      - pages -> list
      - last reading page
  - Library class
      - active book -> str
      - collection of books => {id: Book()}

Assume:
  - Given books will have titles, content, last reading pages are not provided
"""

class Book:
  def __init__(self, id, title, content):
    self.id = id # from counting how many books in the library
    self.title = title
    self.content = content # list of string correspond to the pages
    self.last_page = 0

  def display_page(self):
    return self.content[self.last_page]

  def turn_page(self):
    self.last_page += 1
    return self.display_page()

class Library():
  def __init__(self):
    self.collection = dict()
    self.active_book = None
    self.id_counter = 0

  def add_book(self, title, content):
    new_book = Book(self.id_counter, title=title, content=content)
    self.collection[new_book.id] = new_book
    self.id_counter += 1

  def remove_from_collection(self, id):
    del self.collection[id]

  def set_active_book(self, id):
    self.active_book = id

  def display_page(self):
    return self.collection[self.active_book].display_page()

  def turn_page(self):
    return self.collection[self.active_book].turn_page()

"""
Given a scenario if reader needs to increase the font size
=> Calculate how many character per page based on the font size
  Get start index = chars_per_page * last_page
  get end index = chars_per_page + start index
  ===> return self.content[start_index : end_index]
"""
