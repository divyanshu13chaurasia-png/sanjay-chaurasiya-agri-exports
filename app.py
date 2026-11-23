from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'change-this-before-deployment'

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',  # Set your MySQL password here if you have one
    'database': 'sanjay_agri_exports'
}


FALLBACK_PRODUCTS = [
    {
        'product_name': 'Potato',
        'category': 'Root Vegetables',
        'description': 'Fresh potatoes for wholesale and export enquiries.',
        'image_path': 'images/potatoes.jpeg'
    },
    {
        'product_name': 'Elephant Foot Yam',
        'category': 'Root Vegetables',
        'description': 'Fresh Elephant Foot Yam, also known as Suran or Jimikand.',
        'image_path': 'images/elephant-foot-yam.jpeg'
    },
    {
        'product_name': 'Capsicum',
        'category': 'Vegetables',
        'description': 'Fresh capsicum for wholesale enquiries.',
        'image_path': 'images/capsicum.jpeg'
    },
    {
        'product_name': 'Green Chilli',
        'category': 'Vegetables',
        'description': 'Fresh green chilli for wholesale enquiries.',
        'image_path': 'images/green-chilli.jpeg'
    },
    {
        'product_name': 'Cabbage',
        'category': 'Vegetables',
        'description': 'Fresh cabbage for wholesale enquiries.',
        'image_path': 'images/cabbage.jpeg'
    },
    {
        'product_name': 'Fresh Raw Turmeric',
        'category': 'Root Vegetables',
        'description': 'Fresh raw turmeric rhizomes for wholesale enquiries.',
        'image_path': 'images/fresh-turmeric.jpeg'
    }
] 


def get_products():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT product_name, category, description, image_path FROM products WHERE is_active = TRUE ORDER BY product_id")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products or FALLBACK_PRODUCTS
    except Error:
        return FALLBACK_PRODUCTS



@app.route('/')
def home():
    return render_template('index.html', products=get_products())



@app.route('/enquiry', methods=['POST'])
def enquiry():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    company = request.form.get('company', '').strip()
    country = request.form.get('country', '').strip()
    product = request.form.get('product', '').strip()
    quantity = request.form.get('quantity', '').strip()
    message = request.form.get('message', '').strip()

    if not name or not email or not message:
        flash('Please fill in your name, email, and message.', 'error')
        return redirect(url_for('home') + '#contact')

    # Current schema stores the message in contact_messages. Buyer enquiries will be
    # linked to buyers/products in a later step once we validate the full form flow.
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        subject = f"Buyer enquiry | {product or 'Product not specified'} | {country or 'Country not specified'} | {quantity or 'Quantity not specified'}"
        cursor.execute(
            "INSERT INTO contact_messages (name, email, subject, message) VALUES (%s, %s, %s, %s)",
            (name, email, subject, f"Company: {company}\nCountry: {country}\nProduct: {product}\nQuantity: {quantity}\n\n{message}")
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash('Thank you. Your enquiry has been received.', 'success')
    except Error as e:
        print("MYSQL ENQUIRY ERROR:", e)
        flash('The enquiry could not be saved. Please contact us directly for now.', 'error')
    return redirect(url_for('home') + '#contact')



if __name__ == '__main__':
    app.run(debug=True)
