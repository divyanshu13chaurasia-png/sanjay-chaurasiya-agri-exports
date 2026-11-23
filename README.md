# Sanjay Chaurasiya Agri Exports Website

Flask + MySQL starter website with product catalogue and buyer enquiry form.

## Setup
1. Start MySQL in XAMPP.
2. Confirm database `sanjay_agri_exports` and tables are created.
3. Edit DB credentials in `app.py` if needed.
4. In VS Code terminal run:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```
5. Visit http://127.0.0.1:5000


## Images
Place product photos in `static/images/` matching these names:
- potatoes.jpg
- elephant-foot-yam.jpg
- capsicum.jpg
- green-chilli.jpg
- cabbage.jpg
- fresh-turmeric.jpg

## Important before public deployment
- Replace Flask `secret_key` with a secure random secret from environment variables.
- Do not deploy with `debug=True`.
- Configure a strong MySQL account/password and least-privilege permissions.
- Add HTTPS, CSRF protection, spam/rate limiting, validation and deployment environment configuration.
- Verify business details, supply claims, and product availability before publishing.
