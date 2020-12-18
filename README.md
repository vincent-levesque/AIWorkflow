Are there unit tests for the API?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>python ApiTests.py
ssss
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK (skipped=4)


Are there unit tests for the model?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>python ModelTests.py
... test flag on
...... subsetting data
...... subsetting countries
... loading ts data from files
... saving test version of model: models\test-all-0_1.joblib
... saving test version of model: models\test-united_kingdom-0_1.joblib
.... loading ts data from files
.... loading ts data from files
.
----------------------------------------------------------------------
Ran 3 tests in 67.189s

OK


Are there unit tests for the logging?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>python LoggerTests.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.028s

OK


Can all of the unit tests be run with a single script and do all of the unit tests pass?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>python AllTests.py
....... test flag on
...... subsetting data
...... subsetting countries
... loading ts data from files
... saving test version of model: models\test-all-0_1.joblib
... saving test version of model: models\test-united_kingdom-0_1.joblib
.... loading ts data from files
.... loading ts data from files
.ssss
----------------------------------------------------------------------
Ran 11 tests in 64.084s

OK (skipped=4)


Is there a mechanism to monitor performance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
see performance.ipynb notebook 


Was there an attempt to isolate the read/write unit tests from production models and logs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
log_file = os.path.join("logs","predict-test.log")


Does the API work as expected? For example, can you get predictions for a specific country as well as for all countries combined?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>python predict.py
All:  {"y_pred":[228853.42045000003],"y_proba":null}

United Kingdom:  {"y_pred":[206256.72139999998],"y_proba":null}



Does the data ingestion exists as a function or script to facilitate automation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## load the model
print("LOADING MODELS")
all_data, all_models = model_load()
print("... models loaded: ",",".join(all_models.keys()))

Were multiple models compared?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
see notebook performance.ipynb (RandomForestRegressor, GradientBoostingRegressor, DecisionTreeRegressor)


Did the EDA investigation use visualizations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
see notebook part1.ipynb


Is everything containerized within a working Docker image?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Did they use a visualization to compare their model to the baseline model?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~