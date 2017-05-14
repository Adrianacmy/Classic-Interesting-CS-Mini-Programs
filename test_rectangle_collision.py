from rectangle_collision import Point, Rectangle


def test_is_collided():
    p1 = Point(0, 0)
    p2 = Point(2, 2)
    r1 = Rectangle(p1, 2, 2)
    r2 = Rectangle(p2, 3, 3)
    
    assert r1.is_collided(r2) == False