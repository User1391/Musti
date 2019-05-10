from settings import *
def tuplengine(tuple1, tuple2, operation):
    """
    quick and dirty, element-wise, tuple arithmetic helper,
    created on Sun May 28 07:06:16 2017
    ...
    tuple1, tuple2: [named]tuples, both same length
    operation: '+', '-', '/', '*', 'd'
    operation 'd' returns distance between two points on a 2D coordinate plane (absolute value of the subtraction of pairs)
    """
    assert len(tuple1) == len(tuple2), "tuple sizes doesn't match, tuple1: {}, tuple2: {}".format(len(tuple1), len(tuple2))
    assert isinstance(tuple1, tuple) or tuple in type(tuple1).__bases__, "tuple1: not a [named]tuple"
    assert isinstance(tuple2, tuple) or tuple in type(tuple2).__bases__, "tuple2: not a [named]tuple"
    assert operation in list("+-/*d"), "operation has to be one of ['+','-','/','*','d']"
    return eval("tuple( a{}b for a, b in zip( tuple1, tuple2 ))".format(operation)) \
    if not operation == "d" \
      else eval("tuple( abs(a-b) for a, b in zip( tuple1, tuple2 ))")

def gravity(m1, m2, r):
    return ((m1*m2)/r**2)/100

def bodyGrav(body1, body2):
    m1 = body1.getMass()
    m2 = body2.getMass()
    rx = body1.xdist(body2)
    ry = body1.ydist(body2)
    invx = -1
    invy = -1
    if rx == 0:
        rx = 1
    if ry == 0:
        ry = 1
    if rx > 0:
        ax = 1 * invx
    elif rx < 0:
        ax = -1 * invx
    if ry > 0:
        ay = 1 * invy
    elif ry < 0:
        ay = -1 * invy
    return (ax*gravity(m1, m2, rx), ay*gravity(m1, m2, ry))

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

    # draw rectangle around the image
    pygame.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)
