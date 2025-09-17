from collections import defaultdict
import heapq  # Don't forget this import!

class FoodRatings(object):
    
    def __init__(self, foods, cuisines, ratings):
        """
        Initialize the Food Rating System with lazy deletion approach
        :type foods: List[str] - list of food names
        :type cuisines: List[str] - corresponding cuisine types  
        :type ratings: List[int] - initial ratings for each food
        """
        # \U0001f3d4️ Max heap per cuisine: stores (-rating, food_name) tuples
        # Using defaultdict(list) creates empty list for new cuisines automatically
        self.cuisine_to_heap = defaultdict(list)
        
        # \U0001f5fa️ Quick lookup: food name → cuisine type mapping
        self.food_to_cuisine = {}
        
        # \U0001f4ca Current rating tracker: food name → current rating (stored as negative)
        # Using negative values to match heap storage format for consistency
        self.food_to_rating = defaultdict(int)
        
        # \U0001f504 Initialize all data structures
        for i in range(len(foods)):
            food_name = foods[i]
            cuisine_type = cuisines[i] 
            rating = ratings[i]
            
            # Map food to its cuisine for quick lookup
            self.food_to_cuisine[food_name] = cuisine_type
            
            # \U0001f4e5 Push to max heap: negate rating since heapq is min-heap by default
            # Tuple (-rating, food_name) ensures lexicographic ordering for ties
            heapq.heappush(self.cuisine_to_heap[cuisine_type], (-rating, food_name))
            
            # Store current rating (negative for consistency with heap)
            self.food_to_rating[food_name] = -rating

    def changeRating(self, food, newRating):
        """
        Update a food's rating using lazy deletion technique
        :type food: str - name of food to update
        :type newRating: int - new rating value
        :rtype: None
        """
        # \U0001f50d Find which cuisine this food belongs to
        cuisine = self.food_to_cuisine[food]
        
        # \U0001f4e5 Push new rating to heap WITHOUT removing old entry (lazy approach!)
        # Old entries will be cleaned up later during highestRated() calls
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))
        
        # \U0001f504 Update the current rating tracker (our "source of truth")
        self.food_to_rating[food] = -newRating

    def highestRated(self, cuisine):
        """
        Find highest rated food for given cuisine with lazy deletion cleanup
        :type cuisine: str - cuisine type to search
        :rtype: str - name of highest rated food (lexicographically smallest if tied)
        """
        highest_food = None
        
        # \U0001f50d Keep checking heap top until we find a valid (non-stale) entry
        while len(self.cuisine_to_heap[cuisine]) > 0:
            # \U0001f440 Peek at the top element (highest priority)
            curr_entry = self.cuisine_to_heap[cuisine][0]  # (negative_rating, food_name)
            curr_rating = curr_entry[0]  # negative rating from heap
            curr_food = curr_entry[1]    # food name
            
            # \U0001f575️ Validate: does heap's rating match current rating for this food?
            if curr_rating != self.food_to_rating[curr_food]:
                # \U0001f5d1️ LAZY DELETION: This is stale data, remove it and continue
                heapq.heappop(self.cuisine_to_heap[cuisine])
                continue
            
            # ✅ Found valid entry! This is our highest rated food
            highest_food = curr_food
            break
            
        return highest_food


# \U0001f393 Professor's Notes:
# 1. The tuple (-rating, food_name) is brilliant! Python sorts tuples lexicographically,
#    so when ratings are tied, it automatically picks the lexicographically smaller name.
#
# 2. Lazy deletion avoids expensive heap removal operations. We only clean up stale 
#    entries when we encounter them during highestRated() calls.
#
# 3. The food_to_rating dict acts as our "source of truth" - if heap entry doesn't 
#    match this, we know it's outdated.
#
# 4. Time Complexity: O(log k) for both changeRating and highestRated (amortized)
#    where k is the number of foods per cuisine.
#
# 5. Space Complexity: O(n) where n is total number of foods.