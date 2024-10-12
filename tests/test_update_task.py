def test_update_task(client, auth_token):
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.put(
        "/tasks/1",
        json={"title": "New Test Task Updated", "status":"completed"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New Test Task Updated"
    assert response.json()["status"] == "completed"