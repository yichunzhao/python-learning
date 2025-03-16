# python-learning


 In the context of TensorFlow and most other frameworks, a tensor with **shape `[C]`** is a **1-dimensional** tensor with **C elements**. It is not a 0-dimensional tensor, but rather a 1D tensor.

Let’s clarify the different types of tensor shapes:

### 1. **0-Dimensional Tensor (Scalar):**
   - A **0D tensor** is a single value. 
   - Example: A single number like `3`, which has the shape `[]` (empty tuple).
   - **Shape**: `[]`
   - Example code:
     ```python
     scalar_tensor = tf.constant(3)  # Shape is [] (0D tensor)
     ```

### 2. **1-Dimensional Tensor (Vector):**
   - A **1D tensor** is a vector of elements. For example, a tensor with `C=4` elements.
   - **Shape**: `[C]`
   - Example: `[0., 1., 0., 0.]` with shape `(4,)`.
   - Example code:
     ```python
     vector_tensor = tf.constant([0., 1., 0., 0.])  # Shape is (4,) (1D tensor)
     ```

### 3. **2-Dimensional Tensor (Matrix):**
   - A **2D tensor** is a matrix (a grid of values).
   - **Shape**: `[rows, columns]`
   - Example: A matrix with 2 rows and 3 columns: `[[1, 2, 3], [4, 5, 6]]` with shape `(2, 3)`.
   - Example code:
     ```python
     matrix_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])  # Shape is (2, 3) (2D tensor)
     ```

### 4. **3-Dimensional Tensor (Tensor of Tensors):**
   - A **3D tensor** is essentially a 3D array.
   - **Shape**: `[depth, rows, columns]`
   - Example: A 3D tensor of shape `(2, 3, 3)` represents 2 matrices, each of size `(3, 3)`.

### 5. **4-Dimensional Tensor ** 
   - A **4D tensor** is essentially a 4D array.
   - **Shape**: `[batch, height, width, channels]`
   - Example: `np.ones((1, 4, 4, 3))` creates a 4D array with the following dimensions:
        - 1: This is often referred to as the batch size. It indicates that there's one "sample" in this array.
        - 4: This represents the height of the 2D spatial dimensions.
        - 4: This represents the width of the 2D spatial dimensions.
        - 3: This represents the number of channels (e.g., RGB for an image).
        - So, this creates a tensor where every entry is a 1.


---

