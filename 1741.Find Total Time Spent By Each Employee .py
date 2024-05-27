import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # dictionary = {}
    # for i in range(len(employees)):
    #     emp_id = employees['emp_id'][i]
    #     day = employees['event_day'][i]
    #     in_time = employees['in_time'][i]
    #     out_time = employees['out_time'][i]
    #     if (day,emp_id) in dictionary:
    #         dictionary[(day,emp_id)] += out_time-in_time
    #     else:
    #         dictionary[(day,emp_id)] = out_time-in_time
    # result = []
    # for key,value in dictionary.items():
    #     result.append([key[0],key[1],value])
    # return pd.DataFrame(result,columns=['day','emp_id','total_time'])

    employees['total_time'] = employees['out_time']- employees['in_time']
    group = employees.groupby(['event_day','emp_id'])['total_time'].sum().reset_index()
    employees.rename({'event_day':'day'},axis=1,inplace = True)
    return employees
    
    

    