import pytest

@pytest.mark.run_last
def test_delete_task(client, auth_token):

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.delete("/tasks/1", headers=headers)

    
    assert response.status_code == 200