import unittest
from app import app
from flask import session

class ForexExchangeTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment for the test case.
        """
        self.client = app.test_client()
        app.config['TESTING'] = True
        
    def test_convert_valid_currencies(self):
        """
        Test case to verify the conversion of valid currencies.

        This test case sets the session with valid currencies and sends a POST request to the '/convert' endpoint
        with the 'from' currency as 'USD', 'to' currency as 'EUR', and 'amount' as '100'. It then asserts that the
        response status code is 200 and checks if the 'USD', 'EUR', and '100' are present in the response data.

        """
        with self.client.session_transaction() as sess:
            sess['currencies'] = {'USD': 'Dollar', 'EUR': 'Euro'}
        response = self.client.post('/convert', data={'from': 'USD', 'to': 'EUR', 'amount': '100'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'USD', response.data)
        self.assertIn(b'EUR', response.data)
        self.assertIn(b'100', response.data)
        
    def test_convert_invalid_currencies(self):
        """
        Test case to check the behavior when invalid currencies are entered for conversion.

        This test sets up a session with valid currencies and then sends a POST request to the '/convert' endpoint
        with an invalid currency as the 'to' parameter. The test asserts that the response contains the message
        'Please enter valid currencies'.

        """
        with self.client.session_transaction() as sess:
            sess['currencies'] = {'USD': 'Dollar', 'EUR': 'Euro'}
        response = self.client.post('/convert', data={'from': 'USD', 'to': 'XYZ', 'amount': '100'}, follow_redirects=True)
        self.assertIn(b'Please enter valid currencies', response.data)
    
    def test_convert_missing_fields(self):
        """
        Test case to check if an error message is displayed when there are missing fields in the conversion form.
        """
        with self.client.session_transaction() as sess:
            sess['currencies'] = {'USD': 'Dollar', 'EUR': 'Euro'}
        response = self.client.post('/convert', data={'from': '', 'to': 'EUR', 'amount': '100'}, follow_redirects=True)
        self.assertIn(b'Please fill all the fields', response.data)
    
    def test_same_currency(self):
        """
        Test case to check if the conversion of the same currency returns the correct result.

        This test sets up a session with currencies and sends a POST request to the '/convert' endpoint
        with the same currency for both 'from' and 'to' parameters and an amount of 100. It then checks
        if the response status code is 200 and if the response data contains the expected amount.

        Returns:
            None
        """
        with self.client.session_transaction() as sess:
            sess['currencies'] = {'USD': 'Dollar', 'EUR': 'Euro'}
        response = self.client.post('/convert', data={
            'from': 'USD',
            'to': 'USD',
            'amount': '100'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'100', response.data)

    
if __name__ == '__main__':
    unittest.main()