# Wine-Quality-Estimation
An application that is built along with a machine learning model trained on the UCI  Portuguese "Vinho Verde"  white wine dataset.
This dataset is publicly available at [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv) for research purposes. 

__Dataset Reference:__ P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

## About Dataset
In the above reference, two datasets were created, using red and white wine samples. The inputs include objective tests (e.g. PH values) and the output is based on sensory data (median of at least 3 evaluations made by wine experts). Each expert graded the wine quality between 0 (very bad) and 10 (very excellent). Several data mining methods were applied to model these datasets under a regression approach. The support vector machine model achieved the best results. Several metrics were computed: MAD, confusion matrix for a fixed error tolerance (T), etc. Also, we plot the relative importances of the input variables (as measured by a sensitivity analysis procedure).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are munch more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.

__Number of Instances:__ red wine - 1599; white wine - 4898. 

__Number of Attributes:__ 11 + output attribute
  
__Note:__ several of the attributes may be correlated, thus it makes sense to apply some sort of feature selection.

__Attribute information:__ For more information, read [Cortez et al., 2009].

__Input variables (based on physicochemical tests):___
1. fixed acidity
2. volatile acidity
3. citric acid
4. residual sugar
5. chlorides
6. free sulfur dioxide
7. total sulfur dioxide
8. density
9. pH
10. sulphates
11. alcohol

Output variable (based on sensory data): 

12. quality (score between 0 and 10)

Missing Attribute Values: None


## Software Structure
The application is in two (2) parts:
### The Model/Algorithm/Estimator development and training
This is where the machine learning model or algorithm is trained to be able to tell poor and high grade wine with a quality of 0-10 (0 being very poor wine and 10 being a high grade wine).
The training language is python.
### The Application development
This is a software housing the model, with a user interface to enable easy interaction with the model.
The development language is python.
