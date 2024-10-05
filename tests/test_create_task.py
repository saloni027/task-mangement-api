
def test_create_task(client):
    
    response = client.post(
        "/tasks/",
        json={"title": "New Test Task", "description": "Test description", "due_date": "2024-10-04T10:12:04.186Z", "status":"pending"}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "New Test Task"
 