import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # mydict = {}
    # for i in range(len(courses)):
    #     student = courses['student'][i]
    #     clas = courses['class'][i]
    #     if clas not in mydict:
    #         mydict[clas] = 0
    #     mydict[clas] += 1
    # result = []
    # for key,value in mydict.items():
    #     if value >= 5:
    #         result.append([key])
    # return pd.DataFrame(result,columns=['class'])
    group = courses.groupby(['class']).nunique().reset_index()
    df = group[group['student']>= 5]
    return df[['class']]

    

    

    