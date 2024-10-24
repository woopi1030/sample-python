from pymongo import MongoClient
from pprint import pprint
import faiss
import numpy as np
from collections import Counter

# app.py
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

# MongoDB 서버에 연결
client = MongoClient("mongodb+srv://wplee1087:y9eTIS0ioFugqrBG@library.hmzxr.mongodb.net/")  # 기본적으로 로컬 MongoDB 서버에 연결

# 'mydatabase'라는 데이터베이스 선택 (없으면 새로 생성됨)
db = client["library"]

# 'customers'라는 컬렉션 선택 (없으면 새로 생성됨)
collection = db["books"]

# 1. 데이터 삽입 (Create)
# data_samples = [
#     {'name': 'Alice', 'age': 30, 'score': 85},
#     {'name': 'Bob', 'age': 25, 'score': 90},
#     {'name': 'Charlie', 'age': 35, 'score': 70},
#     {'name': 'David', 'age': 30, 'score': 95},
# ]
# collection.insert_many(data_samples)

# 2. 데이터 조회
# result = collection.find_one()
# print("조회된 데이터:")
# pprint(result)

# # 3. 데이터 업데이트
# collection.update_one({'name': 'Alice'}, {'$set': {'age': 31}})

# 4. Aggregation 예제: 평균 점수 계산
# pipeline = [
#     {
#         '$group': {
#             '_id': '$year',
#             'totalPages': {'$sum': '$pages'}
#         }
#     },
#     {
#         '$sort': {
#             # -1 : 내림차순, 1: 오름차순
#             "totalPages": 1 
#         }
#     }
# ]
# aggregation_result = list(collection.aggregate(pipeline))
# print("Aggregation 결과:")
# pprint(aggregation_result)

# 5. full-text search (search index, search query)
# 서치 인덱스 생성
# collection.create_index([
#     ('title', 'text'), 
#     ('content', 'text')
# ])

# Full-Text Search 수행
search_query = 'home cooking'
# results = collection.find({'$text': {'$search': search_query}})
results = collection.aggregate([
    {
        '$search': {
            'index': 'fulltextsearch',  # 생성한 Search Index 이름
            'text': {
                'query': search_query,
                'path': ['title']  # 검색할 필드
            }
        }
    },
    # {
    #     '$project': {
    #         'title': 1,
    #         'content': 1,
    #         '_id': 0
    #     }
    # }
])
print("Aggregation 결과:")
pprint(results._data)

# 7. 모든 데이터 삭제
# collection.delete_many({}) 

# MongoDB 연결 종료
client.close()