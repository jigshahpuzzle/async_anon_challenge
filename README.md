# Async Anon Machine Learning Challenge 

## Overview 

The following repository contains a sample training dataset from Prosper's Lending Platform on approximately 100k issued loans. It includes features such as the borrower's credit rating, debt to income ratio, as well as Prosper's estimate of the creditworthiness of the borrower. Your job is to use these features to predict whether the borrower will default on each of the loans. The loan default is encoded in the "LoanStatus" variable where 1 indicates a default and a 0 indicates a completed loan. 

## Making a Submission 

Your model will be tested using the provided test dataset. Notice the "LoanStatus" column is missing- your job is to generate these predictions! They will be compared to the actual values, which are currently hidden. Generate your predictions in a csv file, in the following format: 

ListingKey1,Prediction1
ListingKey2,Prediction2
ListingKey3,Prediction3
...

Make sure to preserve the order of the ListingKeys as listed in the test dataset when making your predictions. Your answers will simply be diffed with the correct answer set to determine your score. Note that there is no space between the comma and the prediction. 

Once you have generated your predictions, fork the repository, and commit your predictions file as firstname-lastname.csv. Make a pull request into the original repository before the time is up.

## Sample Code

It is recommended that you use Python3 for this challenge; sample code is provided in the repository to help you get started with reading the data. However, feel free to use any programming environment you like if there is a specific stack that you prefer and you are comfortable parsing the data yourself. 
