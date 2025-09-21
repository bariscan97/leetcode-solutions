class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        
        self.store = defaultdict(int)
        self.films = defaultdict(SortedList)
        self.rental = set()

        for shop, movie, price in entries:
            self.store[(shop, movie)] = price
            self.films[movie].add((price, shop))
            

    def search(self, movie: int) -> List[int]:
        a = self.films[movie][:5]
        return [x[1] for x in a]


    def rent(self, shop: int, movie: int) -> None:

        price = self.store[(shop, movie)]
        self.films[movie].discard((price, shop))
        self.rental.add((price, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
 
        price = self.store[(shop, movie)]
        self.films[movie].add((price, shop))
        self.rental.discard((price, shop, movie))
    

    def report(self) -> List[List[int]]:

        report_stores = sorted(self.rental)[:5]
        return [[s, m] for p, s, m in report_stores]