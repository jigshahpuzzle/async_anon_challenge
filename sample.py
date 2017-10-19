import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Load in the data
training_data = pd.read_csv("training_data.csv", index_col="ListingKey")
testing_data = pd.read_csv("testing_data.csv", index_col="ListingKey")
print(training_data)
print(testing_data)

# Validate accuracy for a Random Forest Model
training_data = training_data.apply(LabelEncoder().fit_transform)
clf = RandomForestClassifier(n_estimators=50)
features_X = training_data.drop(["LoanStatus"], axis=1).as_matrix()
target_y = training_data["LoanStatus"].values
print(cross_val_score(clf, features_X, target_y))

# Generate Predictions
test_X = testing_data.apply(LabelEncoder().fit_transform) # Note different LE not recommended!
clf.fit(features_X, target_y)
predictions = clf.predict(test_X)
predictions = pd.DataFrame(data=predictions, index=testing_data.index)
predictions.to_csv("firstname_lastname.csv", header=False)
