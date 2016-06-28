
# List of useful functions

There are four libraries imported for this analysis: `matplotlib`, `numpy`, `pandas`.

 - `numpy` is used for performing mathematical operations on arrays
 - `matplotlib` allows graphs to be plotted
 - `pandas` provides an interface for manipulating datasets

The list below gives some functions that you will find useful, although you can use other functions from the libraries given.
Clicking on the heading of each function will take you to the function's main documentation page.

## numpy

: [`numpy.sqrt(n)`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Return the square root of `n`                                         | `> a = numpy.array([1, 4, 9])`                                        |
|                                                                       |                                                                       |
|                                                                       | `> numpy.sqrt(a)`                                                     |
|                                                                       |                                                                       |
|                                                                       | `numpy.array([1, 2, 3])`                                              |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`numpy.mean(data)`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Return the mean of `data`                                             | `> a = numpy.array([1, 4, 9, 3])`                                     |
|                                                                       |                                                                       |
|                                                                       | `> numpy.mean(a)`                                                     |
|                                                                       |                                                                       |
|                                                                       | `4.25`                                                                |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`numpy.sum(data)`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Sum all elements in `data`                                            | `> a = numpy.array([1, 4, 9])`                                        |
|                                                                       |                                                                       |
|                                                                       | `> numpy.sum(a)`                                                      |
|                                                                       |                                                                       |
|                                                                       | `14`                                                                  |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`numpy.minimum(data1, data2)`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.minimum.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Compare two datasets and returns an array containing the element-wise | `> a = numpy.array([1, 4, 9])`                                        |
| minima                                                                |                                                                       |
|                                                                       | `> b = numpy.array([9, 4, 1])`                                        |
|                                                                       |                                                                       |
|                                                                       | `> numpy.minimum(a, b)`                                               |
|                                                                       |                                                                       |
|                                                                       | `numpy.array([1, 4, 1])`                                              |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`numpy.maximum(data1, data2)`](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.maximum.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Compare two datasets and returns an array containing the element-wise | `> a = numpy.array([1, 4, 9])`                                        |
| maxima                                                                |                                                                       |
|                                                                       | `> b = numpy.array([9, 4, 1])`                                        |
|                                                                       |                                                                       |
|                                                                       | `> numpy.maximum(a, b)`                                               |
|                                                                       |                                                                       |
|                                                                       | `numpy.array([9, 4, 9])`                                              |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


## matplotlib

Functions in `matplotlib` are accessed through `pyplot`.

: [`pyplot.hist(data, n, [x1, x2])`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Plots a histogram of given data in `n` equally spaced bins over the   | `> pyplot.hist(`                                                      |
| range `x1` to `x2`                                                    |                                                                       |
|                                                                       | `~~~~~~data.H1_PX, 10, [0, 10000]`                                    |
|                                                                       |                                                                       |
|                                                                       | `~~)`                                                                 |
|                                                                       |                                                                       |
|                                                                       | \includegraphics[width=\textwidth]{assets/01-hist.png}                |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`pyplot.hist2d(data1, data2, n, [[x1, x2], [y1, y2]])`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist2d)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Plot a 2D histogram from two datasets, with $n^2$ bins equally spaced | `> pyplot.hist2d(`                                                    |
| between `x1` and `x2` in `x` and `y1` and `y2` in `y`                 |                                                                       |
|                                                                       | `~~~~~~data.H1_PX, data.H2_PX,`                                       |
|                                                                       |                                                                       |
|                                                                       | `~~~~~~10, [[0, 2000], [0, 4000]]`                                    |
|                                                                       |                                                                       |
|                                                                       | `~~)`                                                                 |
|                                                                       |                                                                       |
|                                                                       | `> pyplot.colorbar()`                                                 |
|                                                                       |                                                                       |
|                                                                       | \includegraphics[width=\textwidth]{assets/02-hist2d.png}              |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`pyplot.scatter(x, y, size, color)`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Plot a scatter plot of `x` vs `y` where each point has area `size`    | `> pyplot.scatter(`                                                   |
| and colour `color`                                                    |                                                                       |
|                                                                       |                                                                       |
|                                                                       | `~~~~~~[1, 2, 5, 1, 3, 5],`                                           |
|                                                                       |                                                                       |
|                                                                       | `~~~~~~[2, 5, 1, 4, 3, 5],`                                           |
|                                                                       |                                                                       |
|                                                                       | `~~~~~~40, "red")`                                                    |
|                                                                       |                                                                       |
|                                                                       | `~~)`                                                                 |
|                                                                       |                                                                       |
|                                                                       | \includegraphics[width=\textwidth]{assets/03-scatter.png}             |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+

## pandas

The following pandas functions have to be applied to an exisiting `DataFrame` object, see the [example analysis](https://github.com/lhcb/opendata-project/blob/master/Example-Analysis.ipynb) for a demonstration.

: [`df.head(n)`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Produces a table of the first `n` rows of data in the structure       | `> df.head(3)`                                                        |
|                                                                       |                                                                       |
|                                                                       | \includegraphics[width=\textwidth]{assets/04-head.png}                |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`df.eval(expression)`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.eval.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Evaluate an expression in the context of the DataFrame                | `> df['H1_PT'] = data.eval(`               |
|                                                                       |                                                                       |
|                                                                       | `~~~~~~'H1_PT = sqrt(H1_PX**2 + H1_PY**2)'`                           |
|                                                                       |                                                                       |
|                                                                       | `~~)`                                                                 |
|                                                                       |                                                                       |
|                                                                       | `df.head(3)`                                                          |
|                                                                       |                                                                       |
|                                                                       | \includegraphics[width=\textwidth]{assets/05-eval.png}                |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+


: [`df.min()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.min.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Return the minimum value for each column in a dataframe               | `> df.min()`                                                          |
|                                                                       |                                                                       |
|                                                                       | `H1_PX              -122475.373002`                                   |
|                                                                       |                                                                       |
|                                                                       | `H1_PY              -613485.901808`                                   |
|                                                                       |                                                                       |
|                                                                       | `H1_PZ                 1420.725768`                                   |
|                                                                       |                                                                       |
|                                                                       | `dtype: float64`                                                      |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+



: [`df.max()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.max.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Return the maximum value for each column in a dataframe               | `> df.max()`                                                          |
|                                                                       |                                                                       |
|                                                                       | `H1_PX               2.411849e+05`                                    |
|                                                                       |                                                                       |
|                                                                       | `H1_PY               1.748288e+05`                                    |
|                                                                       |                                                                       |
|                                                                       | `H1_PZ               1.998913e+07`                                    |
|                                                                       |                                                                       |
|                                                                       | `dtype: float64`                                                      |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+



: [`df.query(expression)`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.query.html)

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Description                                                           | Example                                                               |
+=======================================================================+=======================================================================+
| Select part of a DataFrame provided `expression` evaluates to true    | `> df_2 = df.query("H1_PX > 0")   `                                   |
|                                                                       |                                                                       |
|                                                                       | `df_2.head(3)`                                                        |
|                                                                       |                                                                       |
|                                                                       | \includegraphics[width=\textwidth]{assets/06-query.png}               |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
