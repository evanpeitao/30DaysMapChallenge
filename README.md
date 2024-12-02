## **2024 30Days Map Challenge** ##

Day 01 - Points : [POI in Shanghai Commercial District](https://xupeitao.github.io/30DaysMapChallenge/Day01_ShanghaiPOIMap)


# Forget Gate
f_t = sigmoid(np.dot(W_f, np.concatenate([h_t_minus_1, x_t])) + b_f) 
# Input Gate
i_t = sigmoid(np.dot(W_i, np.concatenate([h_t_minus_1, x_t])) + b_i)  
# Update Cell State
c_tilde_t = np.tanh(np.dot(W_c, np.concatenate([h_t_minus_1, x_t])) + b_c) 
c_t = f_t * c_t_minus_1 + i_t * c_tilde_t 
# Output Gate
o_t = sigmoid(np.dot(W_o, np.concatenate([h_t_minus_1, x_t])) + b_o) h_t = o_t * * np.tanh(c_t)



# Import RandomForestClassifier from sklearn.ensemble
from sklearn.ensemble import RandomForestClassifier
# Create a random forest classifier
classifier = RandomForestClassifier(n_estimators=100)
# Train the classifier on the training data
classifier.fit(X_train, y_train)
# Use the classifier to make predictions on the test data
predictions = classifier.predict(X_test)
# Evaluate the performance of the classifier
accuracy = classifier.score(X_test, y_test)



# Import xgb library
import xgboost as xgb
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the XGBoost classifier
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
# Train the model
model.fit(X_train, y_train)
# Make predictions on the test set
y_pred = model.predict(X_test)


# Import SHAP library
import shap
# Create SHAP TreeExplainer
explainer1 = shap.TreeExplainer(model)
shap_values1 = explainer1.shap_values(X_test)
# Plot SHAP values
shap.summary_plot(shap_values1, X_test, feature_names=df.feature_names)

# Create SHAP GradientExplainer
explainer2 = shap.GradientExplainer(model, X_train)
shap_values2 = explainer2.shap_values(X_test)
# Plot SHAP values
shap.summary_plot(shap_values1, X_test, feature_names=df.feature_names)
