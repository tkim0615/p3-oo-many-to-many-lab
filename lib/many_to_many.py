class Author:
    all = []

    def __init__(self, name):
        self.name = name  
        Author.all.append(self)  
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        royalty_list = [contract.royalties for contract in self.contracts()]
        x = sum(royalty_list)
        return x
class Book:
    all = []

    def __init__(self, title):
        self.title = title  
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]  
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property ##getter author
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        else:
            self._author = author
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception
        else:
            self._book = book
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception
        else:
            self._date = date
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception
        else:
            self._royalties =royalties

    @classmethod       
    def contracts_by_date(cls, date):
        # # return [contract for contract in cls.all if contract.date == date]
        # sorted_by_date = sorted(cls.all, key=lambda contract: contract.date, reverse = True)
        # for contract in sorted_by_date:
        #     print(contract.date)
        return [contract for contract in cls.all if contract.date == date]
        
        
author1 = Author("Name 1")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
author2 = Author("Name 2")
book4 = Book("Title 4")
contract1 = Contract(author1, book1, "02/01/2001", 10)
contract2 = Contract(author1, book2, "01/01/2001", 20)
contract3 = Contract(author1, book3, "03/01/2001", 30)
contract4 = Contract(author2, book4, "01/01/2001", 40)
mizaki = Author('Mizaki')
mizaki.sign_contract(Book('mybook'), '11/01/2001', 3000)
mizaki_contract = mizaki.contracts()
for contract in mizaki_contract:
    print(contract, contract.author, contract.book.title, contract.date, contract.royalties)
# print(contract2.contracts_by_date())
## contract.author still is a instance of Author class. Digg 1 more to its attribute and get the attribute

