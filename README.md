# Data Kitchen
Some nice cooking recipes to help you run your Data Science project like a professional kitchen! We run our data kitchen using the CRISP-DM methodology:

## Understand Business
* important questions to ask...

## Understand Data
* Look for metadata of the data
* Talk to business about meaning of data
* Important questions to ask...
* Look at data distribution:
* Histogram
  * Barchart
  * Boxplot
  * Violinplot
  * Kernel Density
  * Scatterplot matrix

## Prepare and Clean Data
* Deal with missing values
* check and remove repeated values
* check and potentially remove outliers (real outliers or measurement errors?)
* It may make sense to group categorical values in order to create less categories
* Convert String features to categorical features
* Perform statistical data transformations
* are labels imbalanced?
  * correct for imbalance with C parameter?
  * correct for imbalance by manipulating data and adding extra labels?
* Scale numeric values (normalize or standardize)
  * min-max scaling
  * z-score scaling
* Create indicator values (beware of columns with too many categorical values)
* Check curse of dimensionality (data should grow exponentially with number of features)
* Create feature vectors
* Split training and test data set



Data Quality
* Check coverage (e.g., whether all possible values are represented)
* Check keys
* Verify that the meanings of attributes and contained values fit together
* Identify missing attributes and blank fields
* Establish the meaning of missing data
* Check for attributes with different values that have similar meanings (e.g., low fat, diet)
* Check spelling and format of values (e.g., same value but sometimes beginning with a lower-case
letter, sometimes with an upper-case letter)
* Check for deviations, and decide whether a deviation is “noise” or may indicate an interesting phenomenon
* Check for plausibility of values, (e.g., all fields having the same or nearly the same values)


Data Selection
* Collect appropriate additional data (from different sources—in-house as well as externally) Perform significance and correlation tests to decide if fields should be included
* Reconsider Data Selection Criteria (See Task 2.1) in light of experiences of data quality and data exploration (i.e., may wish include/exclude other sets of data)
* Reconsider Data Selection Criteria (See Task 2.1) in light of experience of modeling (i.e., model assessment may show that other datasets are needed)
* Select different data subsets (e.g., different attributes, only data which meet certain conditions)

* Consider the use of sampling techniques (e.g., A quick solution may involve splitting test and training datasets or reducing the size of the test dataset, if the tool cannot handle the full dataset. It may also be useful to have weighted samples to give different importance to different attributes or different values of the same attribute.)
* Document the rationale for inclusion/exclusion
* Check available techniques for sampling data


## Model

* Describe any characteristics of the current model that may be useful for the future
* Record parameter settings used to produce the model
* Give a detailed description of the model and any special features
* For rule-based models, list the rules produced, plus any assessment of per-rule or overall model
accuracy and coverage
* For opaque models, list any technical information about the model (such as neural network topology)
and any behavioral descriptions produced by the modeling process (such as accuracy or sensitivity)
* Describe the model’s behavior and interpretation
* State conclusions regarding patterns in the data (if any); sometimes the model reveals important facts
about the data without a separate assessment process (e.g., that the output or conclusion is duplicated in one of the inputs)


## Evaluate
* Cross validation


* Train. Score. Evaluate
* Confusion matrix (TPR. TNR. etc)
* Misclassification Error or Accuracy
* Precision, Recall, F1-score
* AUROC

## Deploy
