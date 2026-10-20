import unittest

from app import app


class TestStudentTaskManager(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["application"],
            "Student Task Manager"
        )

    def test_tasks(self):
        response = self.client.get("/tasks")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["total"], 3)
        self.assertEqual(len(data["tasks"]), 3)

    def test_greet(self):
        response = self.client.get("/greet?name=Student")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Student!", response.get_json()["message"])


if __name__ == "__main__":
    unittest.main()
  
