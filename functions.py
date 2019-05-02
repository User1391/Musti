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
