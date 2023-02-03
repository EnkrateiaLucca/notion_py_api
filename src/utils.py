import json
import requests


def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    
    return data


def readPage(pageId, headers):
    readUrl = f"https://api.notion.com/v1/pages/{pageId}"

    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()
    print(res.status_code) 
    
    return data


def add_content_to_block(block_content):    
    readUrl = f"https://api.notion.com/v1/blocks/{pageId}/children"

    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()
    print(res.status_code) 
    
    return data
    


def get_idea_from_content_board(db_data, content_board_tag = "Idea"):
    """
    Gets an idea (as a multi select property) from a gallery board.
    """
    length_of_table = len(db_data["results"])
    content_list = []
    for i in range(length_of_table):
        try:
            if db_data["results"][i]["properties"]["Status"]["select"]["name"] == content_board_tag:
                content_list.append(db_data["results"][i]["properties"]["Name"]["title"][0]["plain_text"])
        except:
            continue
    
    return content_list


def get_content_title_idx(db_data, content_title):
    length_db = len(db_data["results"])
    for i in range(length_db):
        if db_data["results"][i]["properties"]["Name"]["title"][0]["plain_text"]==content_title:
            content_idx = i
            break
    
    return content_idx


def get_page_in_database(databaseId, headers, page_content_idx):
    db_data = readDatabase(databaseId, headers)
    return db_data["results"][page_content_idx]

def remove_page_metadata(page_data, keys_to_remove):
    for key in keys_to_remove:
        page_data.pop(key)
    
    return page_data

def remove_property_metadata(page_data, property_name, property_type,
                             keys_to_remove):
    """
    Removes unwated property metadata to be able to update
    a page.
    """
    print("Removing property specific meta keys (color and id for select)")
    for key in keys_to_remove:
        page_data["properties"][property_name][property_type].pop(key)
    
    return page_data

def change_page_property_option(page_data,pageId,headers,property_name, property_type, property_dest_name):
    page_data["properties"][property_name][property_type]["name"]=property_dest_name
    return page_data
    
        
def update_page_property(page_data,pageId,headers,property_name, property_type, property_dest_name):
    updateURL = f'https://api.notion.com/v1/pages/{pageId}'
    page_data = change_page_property_option(page_data,pageId,headers,property_name, property_type, property_dest_name)
    updated_page = json.dumps(page_data)
    res = requests.request("PATCH", updateURL, headers=headers, data=updated_page)
    print(res.text)
    print("Content Board updated!")


# def createPage(databaseId, headers):

#     createUrl = 'https://api.notion.com/v1/pages'
    
#     newPageData = {}

#     data = json.dumps(newPageData)
#     # print(str(uploadData))

#     res = requests.request("POST", createUrl, headers=headers, data=data)

#     print(res.status_code)
#     print(res.text)