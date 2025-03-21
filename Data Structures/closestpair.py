import math

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y


def dist(p1, p2):
   return math.sqrt( (p1.x-p2.x)**2 + (p1.y-p2.y)**2 )


def strip_closest(strip, d):
   min_dist = d
   closest_points = (None, None)
   strip.sort(key=lambda p: p.y)

   for i in range(len(strip)):
      for j in range(i+1, len(strip)):
         if abs(strip[i].y - strip[j].y) >= d:
            break
         current_dist = dist(strip[i], strip[j])
         if current_dist<min_dist:
            min_dist = current_dist
            closest_points = (strip[i], strip[j])
   
   return min_dist, closest_points


def brute_force(points, left, right):
   min_dist = float('inf')
   closest_points = (None, None)

   for i in range(left, right):
      for j in range(i + 1, right + 1):
         current_dist = dist(points[i], points[j])
         if current_dist < min_dist:
               min_dist = current_dist
               closest_points = (points[i], points[j])
               
   return min_dist, closest_points


def closest_pair_recursive(points, left, right):
   if right - left <= 2:
      return brute_force(points, left, right)
   
   mid = left+(right-left)//2
   mid_point = points[mid]

   dl, closest_pair_left = closest_pair_recursive(points, left, mid)
   dr, closest_pair_right = closest_pair_recursive(points, mid+1, right)
   d = min(dl, dr)

   if dl<dr:
      closest_points = closest_pair_left
   else:
      closest_points = closest_pair_right
   
   strip = []
   for i in range(left, right+1):
      if abs(points[i].x - mid_point.x) < d:
         strip.append(points[i])
   
   d_strip, closest_pair_strip = strip_closest(strip, d)
   if d_strip<d:
      return d_strip, closest_pair_strip
   else:
      return d, closest_points



def closest_pair(points):
   points.sort(key=lambda p: p.x)
   return closest_pair_recursive(points, 0, len(points)-1)

def main():
   points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
   distance, closest_points = closest_pair(points)
   print(f"Closest distance: {distance}")
   print(f"Closest points: ({closest_points[0].x}, {closest_points[0].y}) and ({closest_points[1].x}, {closest_points[1].y})")

main()