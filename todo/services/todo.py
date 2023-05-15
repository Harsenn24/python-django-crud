from api_test.helper import DB


async def create(name, description) -> bool:
    data = {
        "name": name,
        "description": description
    }
    result = await DB(collection="todo").insertOne(data)
    print(result)
    return True


async def get_all() -> list:
    result = await DB(collection="todo").aggregate(
        [
            {
                "$project": {
                    "name": "$name",
                    "description": "$description",
                    "id": {"$toString": "$_id"},
                    "_id": 0
                }
            }
        ]
    )
    return result


async def getbyid(id) -> list:
    result = await DB(collection="todo").aggregate(
        [
            {
                "$match": {
                    "_id": id
                }
            },
            {
                "$project": {
                    "name": "$name",
                    "description": "$description",
                    "id": {"$toString": "$_id"},
                    "_id": 0
                }
            }
        ]
    )
    return result


async def update_partial(id, data) -> bool:
    data_partial = {}

    if data.get("name"):
        data_partial["name"] = data.get("name")

    if data.get("description"):
        data_partial["description"] = data.get("description")

    await DB(collection="todo").updateOne(
        {"_id": id},
        {"$set": data_partial}
    )

    return True


async def delete(id) -> bool:

    await DB(collection="todo").deleteOne({"_id": id})
    
    return True
