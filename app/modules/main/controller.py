import requests
from flask import request
import json
import os

class MainController:
    def __init__(self):
        self.cart = []  # Initialize an empty cart

    def index(self):
        return {'message': 'Hello, World!'}  # Updated to match expected response structure

    def add_to_cart(self, data):
        """Add product to cart"""
        product_name = data.get('product_name')
        product_price = data.get('product_price')

        if product_name and product_price is not None:
            self.cart.append({'name': product_name, 'price': product_price})
            return {'cart': self.cart, 'message': 'Product added to cart'}
        else:
            return {'error': 'Invalid product data'}

    def process_mpesa_payment(self, data):
        """Process Mpesa payment"""
        # Mpesa API credentials and endpoint
        api_key = os.getenv('MPESA_API_KEY')
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'BusinessShortCode': '174379',
            'Password': os.getenv('MPESA_PASSWORD'),
            'Timestamp': '20240101000000',
            'TransactionType': 'CustomerPayBillOnline',
            'Amount': data['amount'],
            'PartyA': data['phone'],
            'PartyB': '174379',
            'PhoneNumber': data['phone'],
            'CallBackURL': os.getenv('MPESA_CALLBACK_URL'),
            'AccountReference': 'OsongoElectronics',
            'TransactionDesc': 'Payment for goods'
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': f"Payment failed with status code {response.status_code}"}
        except Exception as e:
            return {'error': str(e)}

    def process_credit_card_payment(self, data):
        """Process credit card payment"""
        # Stripe API credentials and endpoint
        stripe_api_key = os.getenv('STRIPE_API_KEY')
        stripe_url = 'https://api.stripe.com/v1/charges'
        
        headers = {
            'Authorization': f'Bearer {stripe_api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        payload = {
            'amount': int(float(data['amount']) * 100),  # Convert to cents
            'currency': 'kes',
            'source': data['token'],
            'description': 'Payment for Osongo Electronics'
        }
        
        try:
            response = requests.post(stripe_url, headers=headers, data=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': f"Payment failed with status code {response.status_code}"}
        except Exception as e:
            return {'error': str(e)}
