class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        fleet_stack = []

        for p, s in sorted(pair)[::-1]:
            fleet_stack.append((target - p) / s)

            if len(fleet_stack) >= 2 and fleet_stack[-1] <= fleet_stack[-2]:
                fleet_stack.pop() 
        
        return len(fleet_stack)