import unittest
from run import app

class TestApi(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True

    def testName(self):
        name = input("Enter the name you want to check\n")
        response = self.app.get("http://127.0.0.1:5000/employee/%s" %name)
        #emp = json.loads(response.get_data())
        self.assertEqual(response.status_code,200)

    def testNumber(self):
        strng = input("Enter the number or emailid you want to check\n")
        response = self.app.get("http://127.0.0.1:5000/employee/search/%s" %strng)
        #emp = json.loads(response.get_data())
        self.assertEqual(response.status_code,200)
        reg = r'[\w.-]+@[\w.-]+\.[\w+]|(\d{9}$)'
        self.assertRegex(self, strng, reg)

    def testCity(self):
        city = input("Enter the city you want to check\n")
        response = self.app.get("http://127.0.0.1:5000/employee/searchadd/%s" %city)
        #emp = json.loads(response.get_data())
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()