import math_op as op
import numpy as np

def test_2d_with_value():
    data = np.empty((2, 2), dtype=np.int32)
    print(f"data was {data} with shape of {np.shape(data)}")
    data = op.assign_special(data)#, 1, nr, nc, 2)
    print(f"data is {data} with shape of {np.shape(data)}")


def test_2d_with_reference():
    data = np.random.random((2, 2)).astype(float)

    print(f"data was {data} with shape of {np.shape(data)}")
    op.assign_special_ref(data)#, 1, nr, nc, 2)
    print(f"data is {data} with shape of {np.shape(data)}")



print(op.add(3, 2))
print("\n" + 6 * "=" + " With Value " + 6 *"=")
test_2d_with_value()
print("\n" + 6 * "=" + " With Reference " + 6 *"=")
test_2d_with_reference()



