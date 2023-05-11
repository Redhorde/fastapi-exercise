from uuid import UUID

import pydantic
from fastapi import FastAPI, HTTPException
import json

import models

app = FastAPI()

#   Manual data loading is inferior to automatic parsing using pydantic
# with open('data/data_block.json') as file:
#     data = json.load(file)

#   Pydantic data parsing, less prone to errors
data = pydantic.parse_file_as(path='data/data_block.json', type_=models.List)

#   Part of manual data parsing, obsolete
# for starting_entry in data:
#     starting_entry['id'] = UUID(starting_entry['id'])


@app.get('/')
async def root():
    return {None}


@app.get('/data', tags=['data'])
async def get_data():
    return {"data": data}


@app.post('/data', tags=['data'])
async def send_entry(entry: models.Entry):
    print(data.__root__)
    for i, ent in enumerate(data.__root__):
        if entry.id == ent.id:
            data.__root__[i] = entry
            break
    else:
        data.__root__.append(entry)
    return {'id': entry.id}


@app.delete('/data/{entry_id}', tags=['data'])
async def delete_entry(entry_id: UUID):
    for i, ent in enumerate(data.__root__):
        if ent.id == entry_id:
            data.__root__.pop(i)
            return {'detail': f'Entry with ID {entry_id} removed'}
    else:
        raise HTTPException(status_code=404, detail=f'ID {entry_id} does not exist')


@app.put('/data/{entry_id}', tags=['data'])
async def update_entry(entry: models.Entry):
    for i, ent in enumerate(data.__root__):
        if entry.id == ent.id:
            data.__root__[i] = entry
            return {'detail': f'Entry with ID {entry.id} updated'}
    else:
        raise HTTPException(status_code=404, detail=f'ID {entry.id} does not exist')


