"""
So ways of climbing to n stair will be ways of n-1 stairs + ways of n-2 stair, and here's the explaination:
In this problem, we can either climb 1 step at a time or 2 steps at a time. 
So we can find the ways of climbing to nth stair by checking the ways of climbing to (n-1)th stairs.
For example, if climbing to 5th stairs has 8 different ways, then we can find the ways of climbing to 6th stairs by:
1. climb 1 step after all 5th stairs ways so which means there is F(5) ways.
ex: 11111 -> 111111 or 11112 -> 111121. see? 
2. But hey! we can also climb 2 steps at a time, so we can step down 1 step and step up 2 step
But by doing this, we can only apply that to the ways that has with 1 step at the end like : 11111 or 1211
So how many ways of climbing to 5th stairs ends with 1 step?
remember 1.?, since only ways of (n-1) th stair will add 1 to the end, others will be 1 step down and 2 steps up,
so we know that in all 5th ways, there will be 4th ways that ends with 1, which the amount is f(4)
so the ways that climb to 6th stairs is the sums of ways climbing to 5th stairs and 4th stairs
f(6) = f(5)[the cases that ends with 1] + f(4) [the cases that ends with 2 by 1 step down]
conclusion : f(n) =  f(n-1) + f(n-2), it's a Fibonacci sequence but with f(0) = 1 instead of 0

"""


class Solution:
    def climbStairs(self, n):
        a = 1
        b = 1
        while(n):
            temp = a 
            a = b
            b = temp + b
            n = n - 1
        return a
