from flask import Blueprint, make_response, jsonify, request, current_app, send_from_directory
import os
from .controller import MainController

main_bp = Blueprint('main', __name__)
main_controller = MainController()

@main_bp.route('/', methods=['GET'])
def index():
    """ Example endpoint with simple greeting.
    ---
    tags:
      - Example API
    responses:
      200:
        description: A simple greeting
        schema:
          type: object
          properties:
            data:
              type: object
              properties:
                message:
                  type: string
                  example: "Hello World!"
    """
    result = main_controller.index()
    return make_response(jsonify(data=result))

@main_bp.route('/pay/mpesa', methods=['POST'])
def mpesa_payment():
    """Process Mpesa payment
    ---
    tags:
      - Payments
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            phone:
              type: string
              example: "254700000000"
            amount:
              type: number
              example: 1000
    responses:
      200:
        description: Payment processing result
    """
    data = request.get_json()
    result = main_controller.process_mpesa_payment(data)
    return make_response(jsonify(data=result))

@main_bp.route('/cart/add', methods=['POST'])
def add_to_cart():
    """Add product to cart
    ---
    tags:
      - Cart
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            product_name:
              type: string
              example: "Product A"
            product_price:
              type: number
              example: 1000
    responses:
      200:
        description: Product added to cart
    """
    data = request.get_json()
    result = main_controller.add_to_cart(data)
    return make_response(jsonify(data=result))

def admin_dashboard():
    """Admin dashboard endpoint.
    ---
    tags:
      - Admin
    responses:
      200:
        description: Admin dashboard page
    """
    return make_response(open('admin_dashboard.html').read())

@main_bp.route('/FRONTEND.HTML.HTML', methods=['GET'])
def serve_frontend():
    """Serve the frontend HTML file.
    ---
    tags:
      - Frontend
    responses:
      200:
        description: Frontend HTML page
      500:
        description: Error serving HTML file
    """
    try:
        return send_from_directory(current_app.static_folder, 'FRONTEND.HTML.HTML')
    except FileNotFoundError:
        return "HTML file not found", 404
    except Exception as e:
        return f"Error serving HTML file: {str(e)}", 500


@main_bp.route('/pay/credit-card', methods=['POST'])
def credit_card_payment():
    """Process credit card payment
    ---
    tags:
      - Payments
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            token:
              type: string
              example: "tok_visa"
            amount:
              type: number
              example: 1000
    responses:
      200:
        description: Payment processing result
      400:
        description: Invalid payment data
      500:
        description: Payment processing failed
    """
    data = request.get_json()
    result = main_controller.process_credit_card_payment(data)
    return make_response(jsonify(data=result))

    
@main_bp.route('/landingpage', methods=['GET'])
def serve_landing_page():
    """Serve the landing page HTML file.
    ---
    tags:
      - Frontend
    responses:
      200:
        description: Landing page HTML
      404:
        description: Landing page not found
    """
    try:
        return send_from_directory(current_app.static_folder, 'LANDINGPAGE.HTML')
    except FileNotFoundError:
        return "Landing page not found", 404
    except Exception as e:
        return f"Error serving landing page: {str(e)}", 500
