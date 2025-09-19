class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dic = {}
        self.rate = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if not cuisine in self.rate:
                self.rate[cuisine] = SortedList(key=lambda x: (x[0], ''.join(chr(255 - ord(c)) for c in x[1])))
            self.rate[cuisine].add([rating, food])
            self.dic[food] = [rating, cuisine]

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.dic[food]
        self.rate[cuisine].discard([rating, food])
        self.rate[cuisine].add([newRating, food])
        self.dic[food][0] = newRating
    
    def highestRated(self, cuisine: str) -> str:
        return self.rate[cuisine][-1][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)