import math   # likely useful

def rotate_point_ccw(p: tuple[float, float],
                     pivot: tuple[float, float],
                     rotation_angle: float) -> tuple[float, float]:
    """
    Rotate point p about pivot by 'rotation_angle' degrees counter-clockwise.

    Parameters:
        p (tuple[float, float]): The point (x, y).
        pivot (tuple[float, float]): The pivot (cx, cy).
        rotation_angle (float): Rotation angle in degrees (CCW positive).

    Returns:
        tuple[float, float]: Rotated point (x', y').
    """
    # TODO: implement here!

    theta = math.radians(rotation_angle)
    x = p[0]
    y = p[1]
    cx = pivot[0]
    cy = pivot[1]
    px = (x - cx) * math.cos(theta) - (y - cy) * math.sin(theta) + cx
    py = (x - cx) * math.sin(theta) + (y - cy) * math.cos(theta) + cy

    return (px, py)
