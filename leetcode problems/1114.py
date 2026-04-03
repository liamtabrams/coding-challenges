"""
1114. Print in Order
Solved
Easy

Topics

Companies
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 

Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 

Constraints:

nums is a permutation of [1, 2, 3].
"""

import threading

class Foo:
    """
    Variant 1:
    My next-day reproduction of the official solution given by LC to solve this problem,
    'Approach 1: Pair Synchronization'. The only difference between this implementation
    and the one LC provides is that I call self.secondJobDone.release() outside of the
    firstJobDone lock context manager rather than inside. I don't THINK it matters, but
    maybe it does. Since this code really just instructs the class methods on an order
    of operations and doesn't actually process any input, it doesn't make a lot of sense
    to discuss complexity for this particular problem, but technically both the time and 
    space complexity of this solution is O(1). This solution beats ~60% and ~38% of
    accepted answers in terms of RT and memory efficiency respectively.   
    """
    def __init__(self):
        self.firstJobDone = threading.Lock()
        self.secondJobDone = threading.Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobDone.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstJobDone:
            printSecond()
        self.secondJobDone.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondJobDone:
            printThird()


from threading import Lock

class Foo:
    """
    Variant 2:
    The official solution for 'Approach 1: Pair Synchronization' given by LC for solving
    this problem. As mentioned previously, my reproduction was spot-on except the second
    job lock is released outside the context manager for the first job lock rather than
    inside as it is in this implementation. Again I am not sure if this makes any real
    difference as the real efficiency report suggests that this solution beats about the
    same percentage of accepted answers in both RT and memory efficiency (~60% and 45% 
    respectively).
    """
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()