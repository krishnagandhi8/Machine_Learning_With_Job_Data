import pandas as pd
from warnings import filterwarnings
from ml.preprocessing.cleansing import preprocessing_description, preprocessing_title, preprocessing_company
from ml.preprocessing.cleansing import preprocessing_location, preprocessing_salary, salary_remove_unit, get_skills
from ml.preprocessing.cleansing import get_salary_average, get_experience_senior, get_experience_junior

def apply_preprocessing_on_fields(df):
    filterwarnings('ignore')
    '''
        NOTE: df should be a pandas DataFrame
    '''
    df['Title'] = df['Title'].apply(lambda x: preprocessing_title(x))
    df['Location'] = df['Location'].apply(lambda x: preprocessing_location(x))
    df['Company'] = df['Company'].apply(lambda x: preprocessing_company(x))
    df['Description'] = df['Description'].apply(lambda x: preprocessing_description(x))
    df['Salary'] = df['Salary'].apply(lambda x: preprocessing_salary(x))

    df['Salary_Unit_Month'] = 0
    df['Salary_Unit_Year'] = 0
    df['Salary_Unit_Week'] = 0
    df['Salary_Unit_Day'] = 0
    df['Salary_Unit_Hour'] = 0
    for i in range(df.shape[0]):
        if df['Salary'][i].endswith('month'):
            df['Salary_Unit_Month'][i] = 1
        elif df['Salary'][i].endswith('year'):
            df['Salary_Unit_Year'][i] = 1
        elif df['Salary'][i].endswith('week'):
            df['Salary_Unit_Week'][i] = 1
        elif df['Salary'][i].endswith('day'):
            df['Salary_Unit_Day'][i] = 1
        elif df['Salary'][i].endswith('hour'):
            df['Salary_Unit_Hour'][i] = 1
    
    df['Salary_New'] = df['Salary'].apply(lambda x: salary_remove_unit(x))
    df['Salary_Average'] = df['Salary_New'].apply(lambda x: get_salary_average(x))

    df['Job_Type_Part_Time'] = 0
    df['Job_Type_Full_Time'] = 0
    for i in range(df.shape[0]):
        if df['Description'][i].find('part time') != -1:
            df['Job_Type_Part_Time'][i] = 1
        if df['Description'][i].find('full time') != -1:
            df['Job_Type_Full_Time'][i] = 1

    df['XP_Experience'] = 0
    df['XP_Fresher'] = 0
    df['Gender_Male'] = 0
    df['Gender_Female'] = 0
    for i in range(df.shape[0]):
        if df['Description'][i].find('male') != -1:
            df['Gender_Male'][i] = 1
        if df['Description'][i].find('female') != -1:
            df['Gender_Female'][i] = 1
    
    df['Education_Tenth'] = 0
    df['Education_Twelvth'] = 0
    df['Education_Bachelors'] = 0
    df['Education_Masters'] = 0
    df['Education_Doctorate'] = 0
    for i in range(df.shape[0]):
        if df['Description'][i].find(' 10 ') != -1 or df['Description'][i].find('10th') != -1:
            df['Education_Tenth'][i] = 1
        if df['Description'][i].find(' 12 ') != -1 or df['Description'][i].find('12th') != -1 or df['Description'][i].find('higher secondary'):
            df['Education_Twelvth'][i] = 1
        if df['Description'][i].find('bachelor degree') != -1:
            df['Education_Bachelors'][i] = 1
        if df['Description'][i].find('masters degree') != -1:
            df['Education_Masters'][i] = 1
        if df['Description'][i].find('doctoral') != -1 or df['Description'][i].find('doctorate'):
            df['Education_Doctorate'][i] = 1
        
    df['Skills_Description'] = df['Description'].apply(lambda x: get_skills(x))
    df['Skills_Title'] = df['Title'].apply(lambda x: get_skills(x))
    df['Skills'] = df['Skills_Description'] + df['Skills_Title']
    df['Skills'] = df['Skills'].apply(lambda x: x[1:])

    df['Position_Junior'] = df['Title'].apply(lambda x: get_experience_junior(x))
    df['Position_Senior'] = df['Title'].apply(lambda x: get_experience_senior(x))

    df = df[df['Location'] != 'India'].reset_index().drop(['index'], axis=1)

    return df