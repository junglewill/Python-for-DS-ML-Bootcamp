# Python for DS ML Bootcamp
Exercises from taking Udemy online course - Python for Data Science and Machine Learning Bootcamp. The notes cover what I learnt from the online courses.

Including:
- numpy 
- pandas and pandas.plot
- matplotlib
- seaborn
- plotly and cufflinks
- Two data analytics projects (911 data, 6 banks stock price data)
- Machine Learning Algorithms:
  * Supervised
    1. Linear Regression (from linear_model family) and the threshold calculation
    2. Logistic Regression (from linear_model family) and the threshold calculation
    3. K-Nearest-Neighbor (from knn family), knn is a great way to deal with anonmous data columns, you can standardize before you approach the data, using StandardScaler.fit() , .transform (from preprocessing family)
    4. Decision Trees (from tree family)
    5. Random Forests (from emsemble family)
    6. Supported Vector Machine (svc) & GridSearchCV to .fit() and .predict(), it can help you to choose the best parameters (from sum and model selection family)
  * Unsupervised
    1. K-means and make_blobs (from cluster and datasets family), make_blobs can create data as the following illustration:
    data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8,random_state=101)
    2. Principal Component Analysis (from decomposition family), using in an unsupervised method, this is for you to find the first and second most influential principal component in your dataset, which is a collection of several variables
    3. Recommendation Systems using correlation: Content-based vs. Collaborative Filtering (Memory-Based Collaborative Filtering and Model-Based Collaborative filtering)
  * Natural Language Pocessing - import nltk (the library to process text mining problems)
    1. import string to remove punctuation; from nltk.corpus import stopwords to use stopwords.words('english') to eliminate the english stopwords.
    2. from sklearn.feature_extraction.text import CountVectorizer, this is to calculate the words of bag, simply use fit and transform to the data. .nnz is to find non zero values, and .shape is to know the words and how many sentences you have
    3. from sklearn.feature_extraction.text import TfidfVectorizer, this is to calculate the tf-idf value, also fit and transform the data. .volcabulary_ is to see a specific word's tf-idf value
    4. from sklearn.naive_bayes import MultinomialNB as the model. simply fit and predict. Noted that there're plenty other models you can choose from
    5. from sklearn.pipeline import Pipeline, this can collect all the previous steps into a list of tuples solution bags. A great way to summarize the methods you used. 
- Deep Learning Algorithms:
  1. Perceptron Model to neural networks: if a model is with 2 or more hidden layers, it's called deep neural networks
  2. Activation functions (Sigmoid, tanh, Rectified Linear Unit, ReLU)
- Big Data and Spark
  1. AWS account setup
  2. RDD transformation
