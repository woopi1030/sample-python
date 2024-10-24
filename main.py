from pymongo import MongoClient

# app.py
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

# MongoDB 서버에 연결
client = MongoClient("mongodb+srv://wplee1087:y9eTIS0ioFugqrBG@library.hmzxr.mongodb.net/")  # 기본적으로 로컬 MongoDB 서버에 연결

# 'mydatabase'라는 데이터베이스 선택 (없으면 새로 생성됨)
db = client["mydatabase"]

# 'customers'라는 컬렉션 선택 (없으면 새로 생성됨)
collection = db["customers"]

# 1. 데이터 삽입 (Create)
# 1. 데이터 삽입
data_samples = [
    {'name': 'Alice', 'age': 30, 'score': 85},
    {'name': 'Bob', 'age': 25, 'score': 90},
    {'name': 'Charlie', 'age': 35, 'score': 70},
    {'name': 'David', 'age': 30, 'score': 95},
]
collection.insert_many(data_samples)

# 2. 데이터 조회
result = collection.find_one({'name': 'Alice'})
print("조회된 데이터:", result)

# # 3. 데이터 업데이트
# collection.update_one({'name': 'Alice'}, {'$set': {'age': 31}})

# 4. Aggregation 예제: 평균 점수 계산
pipeline = [
    {
        '$group': {
            '_id': None,
            'average_score': {'$avg': '$score'}
        }
    }
]
aggregation_result = list(collection.aggregate(pipeline))
print("Aggregation 결과:", aggregation_result)

# collection.delete_many({})  # 모든 데이터 삭제

# MongoDB 연결 종료
client.close()