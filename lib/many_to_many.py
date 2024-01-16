class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return[contract.book for contract in self.contracts()]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        royalties_list = [contract.royalties for contract in self.contracts()]
        return sum(royalties_list)
        print(royalties_list)


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return[contract.author for contract in self.contracts() if contract.book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author 
    @author.setter
    def author(self,author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]

author1 = Author('JKR')
author2 = Author('Tolstoy')
book1 = Book('Harry Potter')
book2= Book('Animal farm')
contract2 = Contract(author2, book1, '12/11/24', 4000)
book3 = Book('fun book')
contract3 = Contract(author2, book2, '4/21/24', 4000)
contract1 = Contract(author1, book1, '1/29/23', 2000)
contract4 = Contract(author1, book1, '3/2/23', 2000)
print(contract3.contracts_by_date('4/21/24'))
print(author1.total_royalties())