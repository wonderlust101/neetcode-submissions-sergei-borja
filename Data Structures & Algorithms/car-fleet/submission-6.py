class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [[p, s] for p, s in zip(position, speed)]

        fleet_stack = []
        fleet.sort(reverse=True)

        for p, s in fleet:
            fleet_stack.append((target - p) / s)
            
            while len(fleet_stack) >= 2 and fleet_stack[-1] <= fleet_stack[-2]:
                fleet_stack.pop()


        return len(fleet_stack)