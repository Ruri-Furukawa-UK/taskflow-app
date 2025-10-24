import pandas as pd
from datetime import date

DATA_FILE = "tasks/task_data.csv"

# CSVから読み込み
def load_tasks():
    try:
        df = pd.read_csv(DATA_FILE)
        df['タグ'] = df['タグ'].apply(eval)  # CSVでリストを扱う場合
        df['期限'] = pd.to_datetime(df['期限']).dt.date
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['タスク名', 'タグ', 'ステータス', '期限'])

# CSVに保存
def save_tasks(df):
    df.to_csv(DATA_FILE, index=False)

# タスク追加
def add_task(name, tags, deadline):
    df = load_tasks()
    new_task = pd.DataFrame([[name, tags, "未着手", deadline]],
                            columns=['タスク名', 'タグ', 'ステータス', '期限'])
    df = pd.concat([df, new_task], ignore_index=True)
    save_tasks(df)

# タスク更新
def update_task(index, **kwargs):
    df = load_tasks()
    for key, value in kwargs.items():
        df.at[index, key] = value
    save_tasks(df)

# タスク削除
def delete_task(index):
    df = load_tasks()
    df = df.drop(index).reset_index(drop=True)
    save_tasks(df)
