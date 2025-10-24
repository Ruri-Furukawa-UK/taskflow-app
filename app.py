import streamlit as st
from tasks import task_manager
from datetime import date

st.title("タスク管理アプリ（CRUD対応）")

# --- タスク追加フォーム ---
with st.expander("タスクを追加"):
    task_name = st.text_input("タスク名")
    tags = st.multiselect("タグ", ["仕事", "勉強", "運動", "趣味"])
    deadline = st.date_input("期限", value=date.today())

    if st.button("タスク追加"):
        if task_name:
            task_manager.add_task(task_name, tags, deadline)
            st.success(f"{task_name} を追加しました")
        else:
            st.warning("タスク名は必須です")

# --- 現在のタスク一覧 ---
tasks_df = task_manager.load_tasks()

if tasks_df.empty:
    st.info("タスクはまだありません")
else:
    st.subheader("現在のタスク一覧")

    # DataFrameにインデックスを追加して管理
    tasks_df_display = tasks_df.copy()
    tasks_df_display.index.name = "ID"
    st.dataframe(tasks_df_display)

    # --- タスク操作 ---
    st.subheader("タスク操作")

    task_ids = tasks_df.index.tolist()
    selected_id = st.selectbox("操作するタスクを選択", task_ids,
                               format_func=lambda x: f"{x}: {tasks_df.at[x, 'タスク名']}")

    action = st.radio("操作", ["完了/未完了切替", "編集", "削除"])

    if action == "完了/未完了切替":
        if st.button("ステータス更新"):
            current = tasks_df.at[selected_id, "ステータス"]
            new_status = "完了" if current != "完了" else "未着手"
            task_manager.update_task(selected_id, ステータス=new_status)
            st.success(f"ステータスを {new_status} に更新しました")

    elif action == "編集":
        edit_name = st.text_input("タスク名", value=tasks_df.at[selected_id, "タスク名"])
        edit_tags = st.multiselect("タグ", ["仕事", "勉強", "運動", "趣味"],
                                   default=tasks_df.at[selected_id, "タグ"])
        edit_deadline = st.date_input("期限", value=tasks_df.at[selected_id, "期限"])

        if st.button("更新"):
            task_manager.update_task(selected_id, タスク名=edit_name, タグ=edit_tags, 期限=edit_deadline)
            st.success("タスクを更新しました")

    elif action == "削除":
        if st.button("削除"):
            task_manager.delete_task(selected_id)
            st.success("タスクを削除しました")
