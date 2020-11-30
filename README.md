__WEBSITE RISK PREDICTION__


Team members:-
1)	Navaneetha Murali
2)	Krishnapriya A
3) 	Midhul M
4)	Naveen B Jacob

__Description of the project__

The project is based on Rule based unsupervised Learning. 

__Reference sites and papers :__

1) Datasets and feature extraction : https://github.com/OneRepublicMarchingOn/FI-XSS-SVM

2) Naive Bayes from scratch : https://github.com/python-engineer/MLfromscratch/blob/master/mlfromscratch/naivebayes.py 

3) A Framework for Detecting Anomalies in HTTP Traffic Using Instance-Based Learning and K-Nearest Neighbor Classification:-Michael Kirchner,Upper Austria University of Applied Sciences, Campus Hagenberg, Department Secure Information Systems
C. Kruegel, G. Vigna and W. Robertson, “A multi-model approach to the detection of web-based attacks”. The International Journal of Computer and Telecommunications Networking, Volume 48, Elsevier, 2005.
W. Robertson, F. Maggi, C. Kruegel and G. Vigna, “Effective Anomaly
Detection with Scarce Training Data”. Proceedings of the Network and Distributed System Security Symposium (NDSS), San Diego, CA USA, February 2010.

4) SVM codes : https://github.com/OneRepublicMarchingOn/FI-XSS-SVM/blob/master/xss-linear-svm-original.py 

__Modifications Done__

The features extracted from the above codes were used to fit each of the classifier models for training and testing. 
__To execute the project__
Use the index.html to run with a UI.
Run the testing.py file.
to run the whole file you will need the treelib library installed. To install it run "pip install treelib".
__To Run the gui__
    Required components:-
        *pipenv
        *flask\\insinde the virtual env
        steps for running:
            * pip3 install pipenv
            * pipenv shell
            * pipenv install flask
            * flask run
            After doing this you can use __ctrl+c__ to terminate the flask and then type __exit__ to exit the virtual env
            for running next time:- 
                In the home dir :-
                    * pipenv shell
                    * flask run