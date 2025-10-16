from typing import List, Opcional
from models import Book, Member

#Clase que gestiona toda la lógica de la biblioteca
class Libraly:
 def __init__(self): []
 self.books: List[Book] = []
 self.members: List [Member] = []
 self._loans: direct_[int,int] = []

 self._next_book_id = 1
        self._next_member_id = 1

    def add_book(self, title: str, author: str, year: int) -> Book:
        book = Book(book_id=self._next_book_id, title=title, author=author, year=year)
        self._next_book_id += 1
        self.books.append(book)
        return book
    
    def search_books(self, query:str) -> List[Book]:
        q = query.lower()
        return [b for b in self.books if q in b.title.lower() or q in b.author.lower()]
    

    def add_member(self, name: str, email: str) -> Member:
        member = Member(member_id=self._ne_member_id, name=name, email=email)
        self._ne_member_id += 1
        self.members.append(member)
        return member

    def search_members(self, query: str) -> List[Member]:
        q = query.lower()
        return [m for m in self.members if q in m.name.lower() or q in m.email.lower()]