import requests, json
import os
# Custom imports
from src.utils import *
import argparse

token = os.environ["NOTION_TOKEN"]
tasks_databaseId = os.environ["NOTION_TASK_DATABASE_ID"]
update_DB_URL = f'https://api.notion.com/v1/databases/{tasks_databaseId}'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"}

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--get", type=str, default="")
    parser.add_argument("--check_task", type=int, default=None)
    parser.add_argument("--uncheck_task", type=int, default=None)
    parser.add_argument("--add_task", type=str, default=None, 
                        help="Create a task in your task db.")
    args = parser.parse_args()
    
    if args.get=="todos":
        db_data = readDatabase(tasks_databaseId, headers)
        print(get_tasks_from_db(db_data))
    
    if args.check_task!=None:
        task_num=args.check_task
        task_status = True
        page_data = get_page_in_database(tasks_databaseId, headers, task_num)
        page_id = page_data["id"]
        check_task(page_data, page_id, headers, check_status=task_status)
    
    if args.uncheck_task!=None:
        task_num=args.uncheck_task
        task_status = False
        page_data = get_page_in_database(tasks_databaseId, headers, task_num)
        page_id = page_data["id"]
        check_task(page_data, page_id, headers, check_status=task_status)
    
    if args.add_task!=None:
        task_title = args.add_task
        create_task(task_title, tasks_databaseId, headers)
        
