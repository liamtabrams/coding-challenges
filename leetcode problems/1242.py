"""
1242. Web Crawler Multithreaded
Solved
Medium

Topics

Companies
Given a URL startUrl and an interface HtmlParser, implement a Multi-threaded web crawler to crawl all links that are under the same hostname as startUrl.

Return all URLs obtained by your web crawler in any order.

Your crawler should:

Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all URLs from a webpage of a given URL.
Do not crawl the same link twice.
Explore only the links that are under the same hostname as startUrl.

As shown in the example URL above, the hostname is example.org. For simplicity's sake, you may assume all URLs use HTTP protocol without any port specified. For example, the URLs http://leetcode.com/problems and http://leetcode.com/contest are under the same hostname, while URLs http://example.org/test and http://example.com/abc are not under the same hostname.

The HtmlParser interface is defined as such:

interface HtmlParser {
  // Return a list of all urls from a webpage of given url.
  // This is a blocking call, that means it will do HTTP request and return when this request is finished.
  public List<String> getUrls(String url);
}
Note that getUrls(String url) simulates performing an HTTP request. You can treat it as a blocking function call that waits for an HTTP request to finish. It is guaranteed that getUrls(String url) will return the URLs within 15ms. Single-threaded solutions will exceed the time limit so, can your multi-threaded web crawler do better?

Below are two examples explaining the functionality of the problem. For custom testing purposes, you'll have three variables urls, edges and startUrl. Notice that you will only have access to startUrl in your code, while urls and edges are not directly accessible to you in code.

 

Example 1:



Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]
Example 2:



Input: 
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = "http://news.google.com"
Output: ["http://news.google.com"]
Explanation: The startUrl links to all other pages that do not share the same hostname.
 

Constraints:

1 <= urls.length <= 1000
1 <= urls[i].length <= 300
startUrl is one of the urls.
Hostname label must be from 1 to 63 characters long, including the dots, may contain only the ASCII letters from 'a' to 'z', digits from '0' to '9' and the hyphen-minus character ('-').
The hostname may not start or end with the hyphen-minus character ('-'). 
See:  https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames
You may assume there're no duplicates in the URL library.
 

Follow up:

Assume we have 10,000 nodes and 1 billion URLs to crawl. We will deploy the same software onto each node. The software can know about all the nodes. We have to minimize communication between machines and make sure each node does equal amount of work. How would your web crawler design change?
What if one node fails or does not work?
How do you know when the crawler is done?
"""

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from concurrent.futures import ThreadPoolExecutor, as_completed

class Solution:
    """
    Variant 1:
    The first solution I got to work for this problem copied from 
    https://www.youtube.com/watch?v=4jVu1E2SCE4. I believe the run time complexity is
    equal to the number of nodes divided by 10, or whatever max workers is set to. I
    believe the same would be true for the space complexity, but I am curious to see
    what leetcode says for this particular implementation. The number of nodes is not 
    predictable based on startUrl so the time and space complexity cannot be written as
    a function of a property (like length) of startUrl. LC's analysis tool reports O(N) 
    for both, so maybe my reasoning is correct. This solution beats ~74% of accepted
    answers in terms of RT and ~58% of answers in terms of memory efficiency
    respectively.
    """
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        get_base = lambda url: url.split('/')[2]
        curr_site = get_base(startUrl)
        visited = set([startUrl])

        with ThreadPoolExecutor(max_workers = 10) as ex:
            dq = deque([ex.submit(htmlParser.getUrls, startUrl)])
            while dq and as_completed(dq):
                curr_urls = dq.popleft().result()
                for url in curr_urls:
                    if url not in visited and get_base(url) == curr_site:
                        visited.add(url)
                        dq.append(ex.submit(htmlParser.getUrls, url))
        return list(visited)


import threading

class Solution:
  """
  Variant 2:
  The best implementation I have found using more rudimentary methods leveraging the 
  threading library rather than concurrent.futures. This ALMOST passes all test cases,
  but fails on test case 19 of 20 because it results in a TLE Error. I am trying to
  get a more rudimentary solution to work as an exercise for me to get a better 
  understanding of and practice the fundamentals of multithreading/concurrency in Python.
  Variant 1 is just too sophisticated for a newb to start with. So far I don't really 
  understand why Variant 1 is more efficienct than this, I just know that it is. I would
  bet that since Variant 1 has O(N) complexity in time and space, so does this solution,
  but clearly it is sub-optimal since it does not solve the problem quickly enough.   
  """
  def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def get_domain(url):
            return url.split('/')[2]

        start_domain = get_domain(startUrl)
        q = deque([startUrl])
        visited = set([startUrl])
        lock = threading.Lock()

        def worker():
            while True:
                lock.acquire()
                if not q:
                    lock.release()
                    return
                home = q.popleft()
                lock.release()
                
                urls = htmlParser.getUrls(home)
                for url in urls:
                    if get_domain(url) == start_domain:
                        lock.acquire()
                        if url not in visited:
                            visited.add(url)
                            q.append(url)
                        lock.release()

        threads = [threading.Thread(target=worker) for _ in range(10)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        return list(visited) 


import threading
from queue import Queue

class Solution:
  """
  Variant 3:
  This is Variant 2 with a few tweaks to make it run much more quickly and pass all of LC's
  test cases. Instead of using Python's deque data structure, it uses the queue data
  structure which is thread-safe and thus does not require locking for popping items. Instead
  of using the deque methods popleft() and append(), we use get() and put() for q. So for this
  more rudimentary approach where we use the threading library directly, we only require a lock
  around adding to the 'visited' set, substantially saving us time by having less blocking in
  the worker() function. It is important to note that calling q.task_done() is absolutely
  necessary to do at the very end of the worker function, since it is necessary to call q.join()
  in our main function crawl() and that would block indefinitely if q.task_done() is not called
  at the end of worker(), given the following facts about queue blocking from ChatGPT.

  '''The q.task_done() method in Python's Queue is used to indicate that a particular item from the 
  queue has been processed. It's necessary when you're using q.join(), which waits until all items 
  in the queue have been marked as "done" before continuing. Here's a breakdown of why it's needed:

  When to Use q.task_done()
  Signaling Completion of Tasks: When a worker thread finishes processing an item from the queue, 
  it calls q.task_done() to signal that the task associated with that item is complete.

  Working with q.join(): When you call q.join(), the main thread will wait until all items that were 
  put into the queue have been fully processed (i.e., each item has a matching task_done() call). 
  Without calling task_done() for each item, q.join() would block indefinitely, as it wouldn't know 
  that the queue has been fully processed.'''

  Anyway, besides those very important details, my original intuition and goal of using more
  rudimentary methods to solve this problem were valid, but my inexperience kept me from implementing
  them correctly at first. 

  Given Variants 1 and 2 have both time and space complexity of O(N), so must this solution. 

  Moreover, this solution beats ~75% and ~94% of accepted answers in terms of RT and memory efficiency
  respectively, suggesting it is superior to Variant 1 in terms of memory efficiency. 
  """
  def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_domain(url):
            return url.split('/')[2]

        start_domain = get_domain(startUrl)
        q = Queue()
        q.put(startUrl)
        visited = set([startUrl])
        visited_lock = threading.Lock()    # Lock for the visited set

        def worker():
            while True:
                home = q.get()
                if home is None:
                    return  
                
                urls = htmlParser.getUrls(home)
                new_urls = set()
                
                for url in urls:
                    if get_domain(url) == start_domain:
                        with visited_lock:
                            if url not in visited:
                                visited.add(url)
                                new_urls.add(url)
                
                for url in new_urls:
                    q.put(url)

                q.task_done()

        threads = [threading.Thread(target=worker) for _ in range(10)]

        for thread in threads:
            thread.start()

        q.join()

        for _ in range(10):
            q.put(None)

        for thread in threads:
            thread.join()

        return list(visited)