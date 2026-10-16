from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    activities[activity_name]["participants"] = [
        participant for participant in activities[activity_name]["participants"] if participant != email
    ]

    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200
    assert email in activities[activity_name]["participants"]

    unregister_response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )

    assert unregister_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
