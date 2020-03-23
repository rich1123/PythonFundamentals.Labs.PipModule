import pandas as pd
import json
import os.path
from glob import glob

def json_helper(path):

    def read_json(path):
        with open(path, 'r') as f:
            data = json.load(f)
            return data

    for dirpath, dirnames, filenames in os.walk(path):
            result = []
            for f in filenames:
                if f.endswith('.json'):
                    json_content_2 = read_json(os.path.join(path, f))
                    for i in json_content_2:
                        i["source"] = f
                        result.append(i)
            df_loc = pd.DataFrame(result)
            return df_loc


if __name__ == "__main__":
    print(json_helper('/Users/rmaiale/dev/DataEngineering.Labs.NOAADailySummaries/'))

