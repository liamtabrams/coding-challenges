"""
coding question with 2 arrays of integers. For any integer in array1, we'll call the
closest int from array2 it's 'sensor' and the difference between the 2 integers can be 
called a 'sensor distance'. Return the largest sensor distance.
"""
import numpy as np
import time

def return_largest_sensor_distance_trivial(list1, list2):
    """
    Return maximum sensor distance from list1.
    I believe the run time complexity of this solution is O(n*m) where n and m are the
    lengths of list1 and list2 respectively and the space complexity is O(m), but I am
    not certain. ChatGPT agrees with me though.
    """ 
    start_time = time.time()
    max_sensor_distance = 0
    list2_array = np.array(list2)
    for i in list1:
        sensor_distance = np.min(np.abs(list2_array - i))
        if sensor_distance > max_sensor_distance:
            max_sensor_distance = sensor_distance

    print(max_sensor_distance)

    end_time = time.time()

    print(f"Execution time of trivial version: {end_time - start_time} seconds")


from bisect import bisect_left

def return_largest_sensor_distance_binary_search(list1, list2):
    """
    Return maximum sensor distance from list1.
    This is a more efficient solution that leverages binary search of list2 rather than
    iterating over the entire array to find the minimum (which is what np.min function 
    does). Since the sort of list2 has time complexity of mlogm and the binary search
    (which is the mechanism behind bisect_left or _right) for each element of list1 is
    nlogm, the total time complexity of this solution is O((n+m)logm). The space
    complexity of this solution is O(m) since the sorted list 'list2' itself is O(m),
    which is the dominant term.

    We in fact see that this solution gives ~ >1 order of magnitude faster speed. If we
    chose even bigger input lists to test our solution we would see an even bigger
    disparity between this solution and the trivial solution, in terms of run time. 
    """ 
    start_time = time.time()
    
    # Sort list2
    list2.sort()
    max_sensor_distance = 0

    # Function to find the closest element in sorted_list using binary search
    def find_closest(sorted_list, target):
        pos = bisect_left(sorted_list, target)
        if pos == 0:
            return sorted_list[0]
        if pos == len(sorted_list):
            return sorted_list[-1]
        before = sorted_list[pos - 1]
        after = sorted_list[pos]
        if after - target < target - before:
            return after
        else:
            return before
    
    # Iterate over each element in list1
    for i in list1:
        closest_value = find_closest(list2, i)
        sensor_distance = abs(closest_value - i)
        if sensor_distance > max_sensor_distance:
            max_sensor_distance = sensor_distance

    print(max_sensor_distance)

    end_time = time.time()

    print(f"Execution time of binary search version: {end_time - start_time} seconds")


list1 = [
    23, 45, 12, 67, 89, 34, 56, 78, 90, 123, 145, 167, 189, 210, 231, 250, 
    273, 289, 300, 315, 333, 347, 365, 378, 390, 405, 423, 437, 456, 470,
    489, 501, 523, 537, 556, 570, 589, 601, 623, 637, 656, 670, 689, 701, 
    723, 737, 756, 770, 789, 801, 823, 837, 856, 870, 889, 901, 923, 937, 
    956, 970, 989, 1001, 1023, 1037, 1056, 1070, 1089, 1101, 1123, 1137, 
    1156, 1170, 1189, 1201, 1223, 1237, 1256, 1270, 1289, 1301, 1323, 1337, 
    1356, 1370, 1389, 1401, 1423, 1437, 1456, 1470, 1489, 1501, 1523, 1537, 
    1556, 1570, 1589, 1601, 1623, 1637, 1656, 1670, 1689, 1701, 1723, 1737, 
    1756, 1770, 1789, 1801, 1823, 1837, 1856, 1870, 1889, 1901, 1923, 1937, 
    1956, 1970, 1989, 2001
]

list2 = [
    5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 
    140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 
    280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 
    420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 
    560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 
    700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 
    840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 
    980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 
    1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 
    1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 
    1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 
    1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 
    1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 
    1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 
    1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 
    1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 
    2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 
    2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 
    2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 
    2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500
]

# Answer should be 5 (as far as I'm aware)

return_largest_sensor_distance_trivial(list1, list2)

return_largest_sensor_distance_binary_search(list1, list2)