# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    # Sort the points by x-coordinate
    points.sort(key=lambda p: p[0])

    return divide_and_conquer(points)


def divide_and_conquer(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    n = len(points)
    if len(points) == 1:
        return points
    elif len(points) == 2:
        return points.sort(key=lambda p: p[1])
    elif len(points) == 3:
        return convex_hull_of_three(points)

    mid = n // 2
    left = divide_and_conquer(points[:mid])
    right = divide_and_conquer(points[mid:])

    return merge(left, right)


def merge(left: list[tuple[float, float]], right: list[tuple[float, float]]) -> list[tuple[float, float]]:
    # Find the lower and upper tangents
    upper_left, upper_right = find_upper_tangent(left, right)
    lower_left, lower_right = find_lower_tangent(left, right)

    # Merge the hulls
    merged_hull = []
    i = upper_left
    while i != lower_left:
        merged_hull.append(left[i])
        i = (i + 1) % len(left)

    j = lower_right
    while j != upper_right:
        merged_hull.append(right[j])
        j = (j + 1) % len(right)

    return merged_hull

def find_upper_tangent(left: list[tuple[float, float]], right: list[tuple[float, float]]) -> tuple[int, int]:
    # Find the upper tangent
    # i is the rightmost point in the left hull
    # j is the leftmost point in the right hull
    i = len(left) - 1
    j = 0

