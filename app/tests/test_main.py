import json

class TestMain():
    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {'message': 'Hello, World!'}

    def test_mpesa_payment(self, client):
        response = client.post('/pay/mpesa', json={'phone': '254700000000', 'amount': 1000})
        assert response.status_code == 200
        # Add more assertions based on expected response

    def test_credit_card_payment(self, client):
        response = client.post('/pay/credit-card', json={'token': 'tok_visa', 'amount': 1000})
        assert response.status_code == 200
        # Add more assertions based on expected response
