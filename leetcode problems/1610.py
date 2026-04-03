"""
1610. Maximum Number of Visible Points
Solved
Hard

Topics

Companies

Hint
You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].



You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.

 

Example 1:


Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
Example 2:

Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.
Example 3:


Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
Output: 1
Explanation: You can only see one of the two points, as shown above.
 

Constraints:

1 <= points.length <= 105
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100
"""

import math

def number_of_points(angle, d, points):
    #angle_upper_bound = d + angle/2
    if d - angle/2 < 0:
        angle_upper_bound = d + angle/2
        # see which points have angles between 360 and (360 + d - angle/2)
        # AND see which points have angles between 0 and angle_upper_bound
        angle_lower_bound = (360 + d - angle/2)
        points_in_fov_left = [point for point in points if 0 <= point <= angle_upper_bound]
        points_in_fov_right = [point for point in points if angle_lower_bound <= point < 360]
        points_in_fov = points_in_fov_left + points_in_fov_right
    elif d + angle/2 >= 360:
        angle_upper_bound = (d + angle/2)%360
        angle_lower_bound = d - angle/2
        points_in_fov_left = [point for point in points if 0 <= point <= angle_upper_bound]
        points_in_fov_right = [point for point in points if angle_lower_bound <= point < 360]
        points_in_fov = points_in_fov_left + points_in_fov_right
    else:
        angle_lower_bound = d - angle/2
        angle_upper_bound = d + angle/2
        points_in_fov = [point for point in points if angle_lower_bound <= point <= angle_upper_bound]
    
    return len(points_in_fov)

class Solution:
    """
    The following is the best solution I could come come up with on my own for this problem.
    It passed 83/119 test cases.
    It is incorrect, ugly, and extremely inefficient. 
    """
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        near_points = 0
        points_your_rf = []
        for point in points:
            point_cartesian = []
            point_cartesian.append(point[0] - location[0])
            point_cartesian.append(point[1] - location[1])
            if point_cartesian[0] == point_cartesian[1] == 0:
                near_points += 1
            else:
                points_your_rf.append(point_cartesian)
        angles_your_rf = []
        for point in points_your_rf:
            hypotenuse = math.sqrt(point[0]**2 + point[1]**2)
            arcsin = round(math.asin(point[1]/hypotenuse)*180/math.pi, 1)
            arccos = round(math.acos(point[0]/hypotenuse)*180/math.pi, 1)
            if arcsin < 0 and arccos > 0:
                arcsin = 360 + arcsin
            if arcsin > 0 and arccos < 0:
                arcsin = 180 - arcsin
            if arcsin < 0 and arccos < 0:
                arcsin = 180 - arcsin
            angles_your_rf.append(arcsin)
            
        max_points = 0
        for d in range(0, 3600, 1):
            num_points = number_of_points(angle, d/10, angles_your_rf)
            if num_points > max_points:
                max_points = num_points
        
        return max_points + near_points


class Solution:
    """
    The following is the official, optimal solution that passes all test cases. It
    essentially uses a sliding window approach and a very helpful atan2 utility
    function in Python to get angle values. It would be more of a pain to get 
    the correct angle values using the atan function instead. This solution has a 
    run time complexity of O(NlogN) (the NlogN comes from the sorting which is the 
    dominant term) and a space complexity of O(N). It makes sense that it is so 
    efficient since the implementation is so elegant.
    """
    def visiblePoints(
        self, points: List[List[int]], angle: int, location: List[int]
    ) -> int:
        v = []
        x, y = location
        same = 0
        for xi, yi in points:
            if xi == x and yi == y:
                same += 1
            else:
                v.append(atan2(yi - y, xi - x))
        v.sort()
        n = len(v)
        v += [deg + 2 * pi for deg in v]
        t = angle * pi / 180
        mx = max((bisect_right(v, v[i] + t) - i for i in range(n)), default=0)
        return mx + same



