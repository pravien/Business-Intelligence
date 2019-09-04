import os
import pandas as pd

def create_data_frame():
    li = []
    for filename in os.listdir('./boliga_stats'):
        #filename = os.path.join(os.getcwd(),filename)
        df = pd.read_csv(os.path.join('./boliga_stats',filename), index_col=None, header=0)
        li.append(df)

    return pd.concat(li, axis=0, ignore_index=True)

if __name__ == '__main__':
    print(create_data_frame().head())