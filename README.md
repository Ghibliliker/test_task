# test_task

ФИО - Масло П.В.

Иструкция развертывания:

```
cd task_2/test_parser
```
```
pip install pipenv
```
```
pipenv shell
```
```
pipenv install --system --deploy --ignore-pipfile
```
```
uvicorn test_parser.asgi:application
```

Пример тела запроса:
```
{
    "id": "73512949"
}
```