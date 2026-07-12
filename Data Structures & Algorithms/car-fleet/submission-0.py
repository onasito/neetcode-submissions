class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        stack = []
        
        for pos, spd in pairs:
            time = (target - pos) / spd
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)