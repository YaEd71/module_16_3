from fastapi import FastAPI

app = FastAPI()

# Инициализация словаря пользователей
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    # Найти максимальный ключ и увеличить его на 1
    max_key = max(int(k) for k in users.keys())
    new_user_id = str(max_key + 1)
    users[new_user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"User {user_id} has been updated"
    return f"User {user_id} not found"

@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    return f"User {user_id} not found"

# Запуск приложения
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)