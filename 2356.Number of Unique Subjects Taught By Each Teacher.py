import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # mydict = {}
    # for i in range(len(teacher)):
    #     t_id = teacher['teacher_id'][i]
    #     sub_id = teacher['subject_id'][i]
    #     if t_id not in mydict:
    #         mydict[t_id] = set()
    #     mydict[t_id].add(sub_id)
    # result = []
    # for key,value in mydict.items():
    #     result.append([key,len(value)])
    # return pd.DataFrame(result,columns=['teacher_id','cnt'])
    group = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    result = group.rename(columns = {"subject_id":"cnt"})
    return result
    
    