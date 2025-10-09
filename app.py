from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def index():
    """Homepage route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/services')
def services():
    """Services page route"""
    return render_template('services.html')

@app.route('/testimonials')
def testimonials():
    """Testimonials page route"""
    return render_template('testimonials.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone', '')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('contact'))
        
        try:
            # Create email message
            msg = Message(
                subject=f'New Contact Form Submission from {name}',
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=['amateurhourcoaching@gmail.com'],
                body=f"""
New contact form submission from AmateurHour Coaching website:

Name: {name}
Email: {email}
Phone: {phone}
Message:
{message}
                """
            )
            
            # Send email
            mail.send(msg)
            flash('Thank you for your message! We\'ll get back to you soon.', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            flash('There was an error sending your message. Please try again or email us directly at amateurhourcoaching@gmail.com', 'error')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """500 error handler"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run on port 5004
    app.run(debug=True, host='0.0.0.0', port=5004)

