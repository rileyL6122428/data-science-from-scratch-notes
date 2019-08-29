* machine learning definition (from this book)

    - creating and using models that are *learned from data*

**Fundamentals of Machine Learning**

    * Overfitting
        - producing a model that performs well to the data provided for training,
          but then generalizes poorly to new data. Typically produced by models 
          that are too complex.
    
    * Underfitting
        - producing a model that doesn't perform well even on training data (typically will discard this model right off the bat).

    * How to bypass overfitting?
        - use different data to train the model and to test the model.

    * Confusion matrix
        - a table used to measure the performance of a classification model.
        has rows and columns for True positive, true negative, false positive (type 1), false negative (type 2)
    
    * Accurate models are not necessarliy good models (think Luke is for Luekemia).
        - you should also measure precision & recall
    
    * precision in a confusion matrix is
        - how accurate our positive predictions were
    
    * recall in a confusion matrix is
        - measures what fraction of the positives our model identified

    * Usually the choice of a model involves a trade off between
        - precision & recall. A model that predicts "yes" when it's even a
        little bit confident will probably have a high recall and low precision.
        A model that predicts "yes" only when it is extremely confident is likely to have low recall and a high precision.

        Put another way, it's a trade off between false positives and false negatives.
    
    * Bias variance trade off:
        - another way to think about over vs under fitting problem
        variance = how much a model changes based on provided training data
        bias = how many mistakes a model makes relative to any sample of data,      including a training set
        high variance & low bias -> overfitting
        low variance & high bias -> underfitting

    * First steps solutions when encountering high bias

        - try adding more features (i.e. go from degree 0 polinomial to degree 1)
            or get more data
    
    * First steps solutions when encountering high variance

        - remove features (i.e. go from degree 9 to degree 8 polinomial) or get
            more data
    
    * One way to decrease chances of overfitting (related to model complexity)

        - hold model complexity constant and add more data to train on (doesn't work though if you start out with high bias)
    
    * Features are

        - whatever inputs we provide to our model. Becomes interesting when our data becomes complicated (like detecting spam based on an email)
    
    * Types of features we extract...

        - limits the types of models we can use