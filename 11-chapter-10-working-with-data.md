"Once you have your data, you should begin by exploring the data"

* Correlation Matrix

    - a matrix in which the ith row and jth column is the correlation between the
      ith dimension and the jth dimension of the data.

* Scatterplot Matrix

    - A collection of scatter plots organized into a grid/matrix. Each scatterplot
      shows the relationship between a pair of values.

* What to do when changing units of measurement affects the clustering of your 
  data? 

  - rescale data such that each dimension has mean 0 and std dev 1. "This   
    effectively gets rid of the units, converting each dimension to 'standard
    deviations from the mean'"

* Principal Component Analysis

    - used on  a multi-dimensional set to extract one or more dimensions that
      capture as much of the variation in the data as possible.

    - process: find scaled first principal component by maximizing variance of each
        data sample with another test vector.
        Then, find the projections of those vectors on first principal component
        subtract projections from data samples, and repeat process, until you have
        found all sufficiently meaningful data.
        Then transform into a lower dim space with those meaningful principal component vectors.

<!-- PAGE 199, DIMENSIONALITY REDUCTION -->