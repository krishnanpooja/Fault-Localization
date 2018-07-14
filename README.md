#Exploring the Relationship between Design Metrics and Software Diagnostics using Machine Learning 
This repository contains python scripts for required to extract metrics for DEFECTS4J Project. 
Two '.csv' files containing the training data. The model was built using Weka v3.8.

## Requirement:
1. Eclipse Plugin CodePro, SourceMonitor
2. Weka version 3.8

#Python Scripts:
Each python script contains relevant comments on its usage in the beginning of the file.
In general, most of the Python scripts need to be provided with the path of the folders as argument.
example:-`python DDU.py filepath`

##Datasets:
Two .csv files :
1. `TrainingData_2.csv` contains overall data. Used for testing Static, Dynamic,Test and Bug metrics seperately. Contains labels - Good, Bad and Unknown
2.  `Training_2_GoodBad.csv` contains only relevant metrics. Can be used to test the final best model. Labels- Good and Bad.

## How to run the Model:
1. Load the training set  `Training_2_GoodBad.csv` on Weka. 
2. Parameter list check the File attribute and press 'Remove'. Its not a relevant attribute for modeling.
3. Classify tab. Load the 'BestModel' in the model folder. Right click on the model and choose the option 'Reapply this models configuration'. 
4. Choose K fold. Set the number of folds to 12( for a good result)
5. Press Start.

## List of Important Metrics
1.Lines
2.Max Complexity
3.Max Depth
4.num_of_tests
5.num_of_passed_tests
6.num_of_failed_tests
7.CBO
8.IFC(Information Flow complexity)
9.Density
10.Diversity
11.Uniqueness
12.DDU
13.No of Modified 
14.No of Chunks
15.No of Failing tests
16.No of Repair Actions
17.Exception Type

## TODO
1. Collect more metrics esp. Dynamic.
2. Try normalizing or using PCA visualization to choose the label thresholds.
