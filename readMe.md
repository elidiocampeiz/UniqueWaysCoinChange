The **coin change problem** deals with finding the total number of ways that an amount of money can be made using specific coins *only*.

For example, if 10 cents are needed, and you can only use coins of the amounts 2,5, and 8; then 10 cents can be created in exactly three ways: {2, 2, 2, 2, 2}, {5, 5} and {2, 8}.

Here the problem is solved using Dynamic Programing (DP), where the solutions to the sub-problems must be utilized to reach the original problem’s solution. Both the Bottom Up and Top Down aproaches are explored. The execution of each implemetation is timed using the timeit library. The results concluded that the bottom up algorithm yeilds much better results then the top down implementation.
