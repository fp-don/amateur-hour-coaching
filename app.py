from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
from markupsafe import escape
import os
import re

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize Flask-Mail
mail = Mail(app)

def contains_malicious_patterns(text):
    """Check for obvious malicious patterns in user input"""
    if not text:
        return False
    
    # Common XSS attack patterns (case-insensitive)
    malicious_patterns = [
        r'<script[^>]*>',
        r'javascript:',
        r'onerror\s*=',
        r'onload\s*=',
        r'onclick\s*=',
        r'onfocus\s*=',
        r'onmouseover\s*=',
        r'<iframe[^>]*>',
        r'<object[^>]*>',
        r'<embed[^>]*>',
        r'eval\s*\(',
        r'expression\s*\(',
    ]
    
    text_lower = text.lower()
    for pattern in malicious_patterns:
        if re.search(pattern, text_lower):
            return True
    
    return False

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
        # Get and sanitize form data
        name = escape(request.form.get('name', '').strip())
        email = request.form.get('email', '').strip().lower()
        phone = escape(request.form.get('phone', '').strip())
        message = escape(request.form.get('message', '').strip())
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('contact'))
        
        # Check for malicious patterns (blocks obvious attacks)
        if contains_malicious_patterns(name) or contains_malicious_patterns(phone) or contains_malicious_patterns(message):
            flash('Your submission contains invalid characters. Please remove any HTML or script tags and try again.', 'error')
            return redirect(url_for('contact'))
        
        # Email format validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('contact'))
        
        # Length validation (prevent abuse)
        if len(name) > 100 or len(email) > 100 or len(phone) > 20 or len(message) > 2000:
            flash('Form data exceeds maximum length. Please shorten your message.', 'error')
            return redirect(url_for('contact'))
        
        try:
            # Create professional HTML email
            html_body = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, #004E89, #1A659E); color: white; padding: 30px; text-align: center; border-radius: 8px 8px 0 0; }}
                    .header h1 {{ margin: 0; font-size: 24px; }}
                    .content {{ background: #ffffff; padding: 30px; border: 1px solid #e0e0e0; }}
                    .field {{ margin-bottom: 20px; }}
                    .field-label {{ font-weight: bold; color: #004E89; margin-bottom: 5px; }}
                    .field-value {{ padding: 10px; background: #f7f9fc; border-radius: 4px; }}
                    .message-box {{ padding: 15px; background: #f7f9fc; border-left: 4px solid #1A659E; border-radius: 4px; margin-top: 10px; }}
                    .footer {{ background: #f7f9fc; padding: 20px; text-align: center; font-size: 12px; color: #666; border-radius: 0 0 8px 8px; }}
                    .reply-button {{ display: inline-block; background: white; color: #1A659E; padding: 12px 30px; text-decoration: none; border-radius: 25px; margin-top: 15px; border: 2px solid #1A659E; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🏃‍♂️ New Contact Form Submission</h1>
                        <p style="margin: 5px 0 0 0; font-size: 14px;">AmateurHour Coaching Website</p>
                    </div>
                    
                    <div class="content">
                        <p>You've received a new inquiry from your website contact form:</p>
                        
                        <div class="field">
                            <div class="field-label">👤 Name:</div>
                            <div class="field-value">{name}</div>
                        </div>
                        
                        <div class="field">
                            <div class="field-label">📧 Email:</div>
                            <div class="field-value">{email}</div>
                        </div>
                        
                        <div class="field">
                            <div class="field-label">📱 Phone:</div>
                            <div class="field-value">{phone if phone else 'Not provided'}</div>
                        </div>
                        
                        <div class="field">
                            <div class="field-label">💬 Message:</div>
                            <div class="message-box">{message}</div>
                        </div>
                        
                        <div style="text-align: center; margin-top: 30px;">
                            <a href="mailto:{email}?subject=Re: Your AmateurHour Coaching Inquiry" class="reply-button">
                                Reply to {name}
                            </a>
                        </div>
                    </div>
                    
                    <div class="footer">
                        <p>This email was sent from the contact form on amateurhourcoaching.com</p>
                        <p style="margin: 5px 0 0 0;">AmateurHour Coaching | Dayton, OH</p>
                    </div>
                </div>
            </body>
            </html>
            """
            
            # Plain text fallback
            text_body = f"""
New Contact Form Submission - AmateurHour Coaching

Name: {name}
Email: {email}
Phone: {phone if phone else 'Not provided'}

Message:
{message}

---
Reply directly to: {email}
Sent from: amateurhourcoaching.com contact form
            """
            
            # Create email message with improved headers
            msg = Message(
                subject=f'🏃 New Inquiry from {name} - AmateurHour Coaching',
                sender=('AmateurHour Coaching Website', app.config['MAIL_DEFAULT_SENDER']),
                recipients=['amateurhourcoaching@gmail.com'],
                body=text_body,
                html=html_body,
                reply_to=email
            )
            
            # Add custom headers to reduce spam score
            msg.extra_headers = {
                'X-Mailer': 'AmateurHour Coaching Contact Form',
                'X-Priority': '1',
                'Importance': 'high'
            }
            
            # Send email
            mail.send(msg)
            flash('Thank you for your message! We\'ll get back to you within 72 hours.', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            flash('There was an error sending your message. Please try again or email us directly at amateurhourcoaching@gmail.com', 'error')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap for SEO"""
    return render_template('sitemap.xml'), 200, {'Content-Type': 'application/xml'}

@app.route('/robots.txt')
def robots():
    """Serve robots.txt for SEO"""
    return app.send_static_file('robots.txt')

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

