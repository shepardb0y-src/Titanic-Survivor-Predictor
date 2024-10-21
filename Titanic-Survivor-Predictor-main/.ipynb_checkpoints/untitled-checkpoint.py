import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from sklearn.ensemble import RandomForestClassifier  # Corrected import
from sklearn.metrics import accuracy_score


df =pd.read_csv('train.csv')
df.sample(5)



def get_title(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return 'Uknown'

df['Title'] = df['Name'].map(lambda x: get_title(x))

def replace_titles(x):
    title = x['Title']
    if title in ['Capt', 'Col', 'Major']:
        return 'Officer'
    elif title in ['Jonkheer', "Don", "The Countess", 'Dona', "Lady", "Sir"]:
        return 'Royalty'
    elif title in ['Mme', 'Lady', 'the Countess']:
        return "Mrs"
    elif title in ['Mlle', 'Ms']:
        return "Miss"
    else:
        return title


def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.sav', 'rb'))
    predictions = randomforest.predict(x)
    print(predictions)
    



df['Title'] = df.apply(replace_titles, axis=1)


df['Age'].fillna(df['Age'].median() )
df['Fare'].fillna(df['Fare'].median())
df['Embarked'].fillna(df['Embarked'].mode()[0])  # Fill with mode (most frequent value)
df = df.drop(['Cabin', 'Ticket', 'Name'], axis=1)
sex_mapping = {'male': 0, 'female': 1}
df['Sex'] = df['Sex'].replace(sex_mapping)
embarked_mapping = {'S': 0, 'C': 1, 'Q': 2}
df['Embarked'] = df['Embarked'].replace(embarked_mapping)
title_mapping = {'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Dr': 4, 'Rev': 5, 'Officer': 6, 'Royalty': 7}
df['Title'] = df['Title'].replace(title_mapping)

x = df.drop(['Survived', 'PassengerId'], axis =1)
y = df['Survived']
x_train, x_val, y_train, y_val = train_test_split(x,y, test_size =0.1)

randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
y_pred = randomforest.predict(x_val)
acc_randomforest = round(accuracy_score(y_pred, y_val) * 100, 2)  # Corrected typo in accuracy_score
print('Accuracy :',acc_randomforest)

# Saving the model to a file
pickle.dump(randomforest, open('titanic_model.sav', 'wb'))  # Corrected the mode in the open function

prediction_model(1,1,11,1,1,19,1,1)






