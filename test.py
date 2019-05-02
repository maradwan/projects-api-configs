from app import app
from flask import json

def test_add_config():        
    response = app.test_client().post(
        '/configs',
        data=json.dumps({ "name": "database", "data": { "ip": "192.168.1.1", "hostname": "eg001", "uptime": 7.3, "env": "prod" }}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data[0] == 'database'

def test_update_config():        
    response = app.test_client().put(
        '/configs/database',
        data=json.dumps({ "name": "database", "data": { "ip": "192.168.100.100", "hostname": "eg001", "uptime": 7.3, "env": "testing" }}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['data']['env'] == 'testing'

def test_delete_config():
    response = app.test_client().delete(   
        '/configs/database',
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == 'database'

def test_get_config():
    response = app.test_client().get(   
        '/configs',
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == []

def test_get_configs():
    request = app.test_client().post(
        '/configs',
        data=json.dumps({ "name": "database", "data": { "ip": "192.168.1.1", "hostname": "eg001", "uptime": 7.3, "env": "prod" }}),
        content_type='application/json',
    )

    load = json.loads(request.get_data(as_text=True))
    
    response = app.test_client().get(   
        '/configs/database',
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['data']['env'] == 'prod'

def test_search():
    request = app.test_client().post(
        '/configs',
        data=json.dumps({ "name": "database", "data": { "ip": "192.168.1.1", "hostname": "eg001", "uptime": 7.3, "env": "prod" }}),
        content_type='application/json',
    )

    load = json.loads(request.get_data(as_text=True))
    
    response = app.test_client().get(   
        '/search?name=database&data.env=prod',
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data[1]['data']['env'] 
