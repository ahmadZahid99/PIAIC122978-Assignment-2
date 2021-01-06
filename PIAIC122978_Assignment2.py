# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Numpy_Assignment_2::
# %% [markdown]
# ## Question:1
# %% [markdown]
# ### Convert a 1D array to a 2D array with 2 rows?
# %% [markdown]
# #### Desired output::
# %% [markdown]
# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# %%
import numpy as np
a=np.arange(10)
a.reshape(2,5)

# %% [markdown]
# ## Question:2
# %% [markdown]
# ###  How to stack two arrays vertically?
# %% [markdown]
# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# %%
a=np.arange(10).reshape(2,-1)
b=np.repeat(1,10).reshape(2,-1)
np.vstack([a,b])

# %% [markdown]
# ## Question:3
# %% [markdown]
# ### How to stack two arrays horizontally?
# %% [markdown]
# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# %%
np.hstack([a,b])

# %% [markdown]
# ## Question:4
# %% [markdown]
# ### How to convert an array of arrays into a flat 1d array?
# %% [markdown]
# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# %%
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)
array_of_arrays = np.array([arr1, arr2, arr3])
array_of_arrays=np.concatenate(array_of_arrays)
array_of_arrays

# %% [markdown]
# ## Question:5
# %% [markdown]
# ### How to Convert higher dimension into one dimension?
# %% [markdown]
# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# %%
a=np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
a.reshape(-1)

# %% [markdown]
# ## Question:6
# %% [markdown]
# ### Convert one dimension to higher dimension?
# %% [markdown]
# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# %%
b=np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
b.reshape(5,3)

# %% [markdown]
# ## Question:7
# %% [markdown]
# ### Create 5x5 an array and find the square of an array?

# %%
c=np.array([[55, 25, 15, 41,22], 
            [30, 44, 2, 54,44], 
            [11, 45, 77, 11,55], 
            [11, 212, 4, 20,66],
            [55, 25, 15, 30, 44]]) 
np.square(c)

# %% [markdown]
# ## Question:8
# %% [markdown]
# ### Create 5x6 an array and find the mean?

# %%
c=np.array([[55, 25, 15, 41,22,23], 
            [30, 44, 2, 54,44,34], 
            [11, 45, 77, 11,55,45], 
            [11, 212, 4, 20,66,56],
            [55, 25, 15, 30, 44,67]]) 
np.mean(c)

# %% [markdown]
# ## Question:9
# %% [markdown]
# ### Find the standard deviation of the previous array in Q8?

# %%
np.std(c)

# %% [markdown]
# ## Question:10
# %% [markdown]
# ### Find the median of the previous array in Q8?

# %%
np.median(c)

# %% [markdown]
# ## Question:11
# %% [markdown]
# ### Find the transpose of the previous array in Q8?

# %%
c.T

# %% [markdown]
# ## Question:12
# %% [markdown]
# ### Create a 4x4 an array and find the sum of diagonal elements?

# %%
d=np.array([[55, 25, 15, 41], 
                    [30, 44, 2, 54], 
                    [11, 45, 77, 11], 
                    [11, 212, 4, 20]]) 
np.trace(d)

# %% [markdown]
# ## Question:13
# %% [markdown]
# ### Find the determinant of the previous array in Q12?

# %%
np.linalg.det(d)

# %% [markdown]
# ## Question:14
# %% [markdown]
# ### Find the 5th and 95th percentile of an array?

# %%
a=np.array([20, 2, 7, 1, 34])
print("5th percentile of a : ", 
       np.percentile(a, 5))
print("95th percentile of a : ", 
       np.percentile(a, 95))

# %% [markdown]
# ## Question:15
# %% [markdown]
# ### How to find if a given array has any null values?

# %%
a=np.array([[ 1 , 2],[ 3 , np.nan]])
np.isnan(a)


# %%



