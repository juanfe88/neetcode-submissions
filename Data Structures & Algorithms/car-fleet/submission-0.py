class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos,spe) for pos,spe in zip(position,speed)])
        fleets = len(cars)
        max_time = -float('inf')
        for car in cars[::-1]:
            eta = (target - car[0])/car[1]
            if eta>max_time:
                max_time = eta
            else: 
                fleets -=1
        return fleets
            
