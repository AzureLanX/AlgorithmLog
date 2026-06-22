from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n+1)
        for i in range(len(bookings)):
            data = bookings[i]
            l = data[0]
            r = data[1]
            num = data[2]
            prefix[l-1] += num
            prefix[r] -= num
        
        for i in range(n):
            if i == 0:
                prefix[i] = prefix[i]
            else:
                prefix[i] = prefix[i] + prefix[i-1]
            
        
        return prefix[:-1]
