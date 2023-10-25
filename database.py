from bson.objectid import ObjectId
import motor.motor_asyncio
import asyncio
# from decouple import config

# MONGO_URI = config("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
database = client["students"]
student_collection = database["students_collection"]

def student_helper(student):
    return {
        "id" : str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }

async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

async def add_student(student_data : dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id" : student.inserted_id})
    print(new_student)
    return student_helper(new_student)

async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)
    
async def update_student(id : str, data : dict):
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id" : ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id" : ObjectId(id)},
            {"$set" : data}
        )
        if updated_student:
            return True
        return False

async def delete_student(id : str):
    student = await student_collection.find_one({"_id" : ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id" : ObjectId(id)})
        return True    
    
# data = {
#     "fullname": "Luis Rosas",
#     "email": "superMark2058@gmail.com",
#     "course_of_Study": "Computer Science",
#     "year": 3,
#     "gpa": "4.8"
# }


# loop = asyncio.get_event_loop()
# loop.run_until_complete(add_student(data))
# loop.close()