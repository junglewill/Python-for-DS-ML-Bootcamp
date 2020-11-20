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
    1. Linear Regression (from linear_model family)
    2. Logistic Regression (from linear_model family)
    3. K-Nearest-Neighbor (from knn family), knn is a great way to deal with anonmous data columns, you can standardize before you approach the data, using StandardScaler.fit() , .transform (from preprocessing family)
    4. Decision Trees (from tree family)
    5. Random Forests (from emsemble family)
    6. Supported Vector Machine (svc) & GridSearchCV to .fit() and .predict(), it can help you to choose the best parameters (from sum and model selection family)
  * Unsupervised
    1. K-means and make_blobs (from cluster and datasets family), make_blobs can create data as the following illustration:
    data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8,random_state=101)
    2.
  * Natural Language Pocessing
- Deep Learning Algorithms:
  1. neural net and deep learning
