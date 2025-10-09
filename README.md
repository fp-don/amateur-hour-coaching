# AmateurHour Coaching Website

A professional, modern Flask-based website for AmateurHour Coaching - personalized fitness and triathlon training services.

## Features

- **Responsive Design**: Fully responsive layout that works on all devices
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Contact Form**: Integrated contact form with email functionality
- **Service Pages**: Detailed information about coaching services
- **Testimonials**: Client success stories and reviews
- **SEO Optimized**: Meta tags and semantic HTML for better search visibility

## Pages

- **Home**: Hero section with services overview and testimonials
- **About**: Alyssa's background, credentials, and coaching philosophy
- **Services**: Detailed information on all 4 coaching services
- **Testimonials**: Client success stories and reviews
- **Contact**: Contact form and information

## Technologies Used

- Python 3.10+
- Flask 3.0.0
- Flask-Mail for email functionality
- HTML5/CSS3
- JavaScript (ES6+)
- Font Awesome icons
- Google Fonts (Poppins & Montserrat)

## Installation

### 1. Clone or Navigate to the Project Directory

```bash
cd "/Users/dontestevens/Desktop/CyNet Security & Design LLC/Sites/AmateurHour_Flask_Site"
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=True

# Email Configuration (Optional - for contact form)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=noreply@amateurhourcoaching.com
```

**Note:** For Gmail, you'll need to:
1. Enable 2-factor authentication
2. Generate an "App Password" for mail access
3. Use the App Password (not your regular password)

### 6. Run the Application

```bash
python app.py
```

The website will be available at: `http://localhost:5001`

## Project Structure

```
AmateurHour_Flask_Site/
│
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # This file
│
├── static/
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   ├── js/
│   │   └── main.js      # JavaScript functionality
│   └── images/          # Image assets (to be added)
│
└── templates/
    ├── base.html        # Base template with navigation/footer
    ├── index.html       # Homepage
    ├── about.html       # About page
    ├── services.html    # Services page
    ├── testimonials.html # Testimonials page
    ├── contact.html     # Contact page
    ├── 404.html         # 404 error page
    └── 500.html         # 500 error page
```

## Configuration

### Email Setup

The contact form requires email configuration. If you don't set up email:
- The form will still work
- You'll see an error message
- Users can still email directly at: amateurhourcoaching@gmail.com

### Debug Mode

For production, make sure to:
1. Set `FLASK_DEBUG=False` in `.env`
2. Use a strong `SECRET_KEY`
3. Configure proper email credentials
4. Use a production WSGI server (not Flask's built-in server)

## Adding Images

Place images in the `static/images/` directory:

- `hero-background.jpg` - Hero section background
- `alyssa-coach.jpg` - About page main image
- `coach-placeholder.jpg` - Homepage welcome section
- `training-philosophy.jpg` - About page philosophy section
- `triathlon-training.jpg` - Services page
- `nutrition-guidance.jpg` - Services page
- `road-race-training.jpg` - Services page
- `custom-training.jpg` - Services page

**Recommended image sizes:**
- Hero background: 1920x1080px
- Profile photos: 800x800px
- Service images: 800x600px

## Customization

### Colors

Edit the CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #FF6B35;    /* Orange */
    --secondary-color: #004E89;  /* Blue */
    --accent-color: #1A659E;     /* Light Blue */
}
```

### Content

Update content in the respective HTML templates in the `templates/` directory.

### Contact Email

Update the contact email in:
- `templates/base.html` (footer)
- `templates/contact.html` (contact info)
- `app.py` (form recipient)

## Deployment

### Using Gunicorn (Production)

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Run with Gunicorn:
```bash
gunicorn --bind 0.0.0.0:5001 app:app
```

### Using WSGI File

A `wsgi.py` file is included for deployment with Apache/Nginx.

## Maintenance

### Updating Content

1. **Services**: Edit `templates/services.html`
2. **Testimonials**: Edit `templates/testimonials.html`
3. **About Info**: Edit `templates/about.html`
4. **Contact Info**: Edit `templates/contact.html` and `templates/base.html`

### Adding New Pages

1. Create a new HTML template in `templates/`
2. Add a route in `app.py`
3. Add navigation link in `templates/base.html`

## Support

For questions or issues:
- Email: amateurhourcoaching@gmail.com
- Website Development: FrostPalm Technologies LLC

## License

Copyright © 2024 AmateurHour Coaching. All rights reserved.

---

**Built with ❤️ by FrostPalm Technologies LLC**

