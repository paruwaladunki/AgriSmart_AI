from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

crop_prediction = pd.read_csv(r'C:\Users\Sangu\Desktop\AgriSmart_AI\data\crop_data.csv')

state_encoder = LabelEncoder()
crop_prediction['STATE'] = state_encoder.fit_transform(crop_prediction['STATE'])

crop_encoder = LabelEncoder()
crop_prediction['CROP'] = crop_encoder.fit_transform(crop_prediction['CROP'])

# One-hot encode nominal categorical features
crop_prediction = pd.get_dummies(crop_prediction, columns=['SOIL_TYPE'], drop_first=True)

print(crop_prediction.head())

#features
features = ['STATE', 'N_SOIL', 'P_SOIL', 'K_SOIL', 'TEMPERATURE', 'HUMIDITY', 'ph', 'RAINFALL'] + [col for col in crop_prediction.columns if col.startswith('SOIL_TYPE_')]
X = crop_prediction[features]

#target variable
y=crop_prediction['CROP']

#splitting data into train_data and test_data
train_X, test_X,train_y, test_y = train_test_split(X, y, test_size=0.25, random_state=1)

print("train_X shape:", train_X.shape)
print("train_y shape:", train_y.shape)
print("test_X shape:", test_X.shape)
print("test_y shape:", test_y.shape)

#define model
predict_model = RandomForestClassifier(random_state=1)

#fitting model -> training model
predict_model.fit(train_X, train_y)

#predicting model
predictions = predict_model.predict(test_X)

accuracy = accuracy_score(test_y, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Print detailed classification report
print("\nClassification Report:")
print(classification_report(test_y, predictions, target_names=crop_encoder.classes_))