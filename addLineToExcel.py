
#!!!!!!This will overwrite your excel file!!!!!!!!!!!!
# excel file must have an empty first column

import pandas as pd
import os
from openpyxl import load_workbook


file=input('File Path: ')

pth=os.path.dirname(file)

df=pd.read_excel(file)

file_cols = list(df)#Alternate to # file_cols = df.columns.values.tolist()

df_state = df
def addInstance(file_cols=file_cols, df=df, file=file):
    instance = {}
    writer = pd.ExcelWriter(file, engine='openpyxl')
    for i in file_cols:
        if i == file_cols[0]:
            continue
        else:
            param_entry = input(f'Add {i} Value: ')
            instance[i] = param_entry
    
    new_row = pd.DataFrame(instance, index=[0]) # index otherwise ValueError: If using all scalar values, you must pass an index
    
    newdf = pd.concat([new_row, df]).reset_index(drop=True)
    newdf.to_excel(writer, "Main", columns=file_cols, index=False, index_label=None)#index False AND index_label=None to get rid on Unnamed 0
    writer.save()
    global df_state
    df_state = newdf
    print(f'\nNew Instance Completed, {len(df)} ')
    print('Thanks for using this program.')
    
    return 


while True:
    x=input('Add an instance (Y/N): ').lower()
    if x == 'y':
        addInstance(df=df_state)
        y=input('Would you like to add another? (Y/N): ').lower()
        if y == 'n':
            print('\nThanks for using this program.')
            break
        elif y == 'y':
            continue
    elif x=='n':
        print('\nThanks for using this program.')
        break

    else: continue