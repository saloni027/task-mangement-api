def test_get_task(client):
    
    response = client.get(
        "/tasks/1"
    )
    assert response.status_code == 200