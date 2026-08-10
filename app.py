import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

PACKAGE_DETAILS = {
    'domestic Tour Packages': {
        'WhatsApp Image 2026-08-08 at 2.47.05 PM.jpeg': {
            'badge': 'Group Departure',
            'type': 'Domestic Group Tour',
            'name': 'Hyderabad Tour Package',
            'details': ['5 Nights / 6 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹8,500',
        },
        'WhatsApp Image 2026-08-08 at 2.47.06 PM.jpeg': {
            'badge': 'Diwali Offer',
            'type': 'Domestic Group Tour',
            'name': 'Udaipur Tour Package',
            'details': ['4 Nights / 5 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹7,700',
        },
        'WhatsApp Image 2026-08-08 at 2.47.07 PM (1).jpeg': {
            'badge': 'Group Departure',
            'type': 'Snow Tour',
            'name': 'Kashmir Tour Package',
            'details': ['10 Nights / 11 Days', 'Deluxe & Luxury Options'],
            'price': 'From ₹16,800',
        },
        'WhatsApp Image 2026-08-08 at 2.47.07 PM (2).jpeg': {
            'badge': 'Group Departure',
            'type': 'Beach Tour',
            'name': 'Goa Tour Package',
            'details': ['4 Nights / 5 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹6,000',
        },
        'WhatsApp Image 2026-08-08 at 2.47.07 PM.jpeg': {
            'badge': 'Group Departure',
            'type': 'Hill Station Tour',
            'name': 'Manali Dalhousie Amritsar Tour',
            'details': ['8 Nights / 9 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹15,000',
        },
        'WhatsApp Image 2026-08-08 at 2.47.08 PM (1).jpeg': {
            'badge': 'Diwali Vacation',
            'type': 'Backwater Tour',
            'name': 'Kerala Tour Package',
            'details': ['7 Nights / 8 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹16,000',
        },
        'WhatsApp Image 2026-08-08 at 2.47.08 PM.jpeg': {
            'badge': 'Group Departure',
            'type': 'Hill Station Tour',
            'name': 'Shimla Manali Tour Package',
            'details': ['7 Nights / 8 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹12,500',
        },
    },
    'international Tour Packages': {
        'WhatsApp Image 2026-08-08 at 2.47.11 PM (1).jpeg': {
            'badge': 'Group Departure',
            'type': 'International Group Tour',
            'name': 'Russia Tour Package',
            'details': ['Flights · Hotel · Sightseeing', 'Visa · Meals Included'],
            'price': '₹1,52,500',
        },
        'WhatsApp Image 2026-08-08 at 2.47.11 PM.jpeg': {
            'badge': 'Group Departure',
            'type': 'International Group Tour',
            'name': 'Turkey Tour Package',
            'details': ['10 Nights / 11 Days', 'Flights · Visa · Food · Sightseeing'],
            'price': '₹1,90,000',
        },
        'WhatsApp Image 2026-08-08 at 2.47.12 PM (1).jpeg': {
            'badge': 'Island Escape',
            'type': 'Tropical Tour',
            'name': 'Bali Tour Package',
            'details': ['6 Nights / 7 Days', 'Hotel · Breakfast · Sightseeing'],
            'price': '₹66,500',
        },
        'WhatsApp Image 2026-08-08 at 2.47.12 PM.jpeg': {
            'badge': 'City Escape',
            'type': 'International City Tour',
            'name': 'Dubai Tour Package',
            'details': ['4 Nights Accommodation', 'Tours · Transfers · Visa · Flights'],
            'price': '₹70,000',
        },
        'WhatsApp Image 2026-08-08 at 2.47.13 PM.jpeg': {
            'badge': 'City Escape',
            'type': 'International City Tour',
            'name': 'Baku Tour Package',
            'details': ['4 Nights Accommodation', 'Hotel · Breakfast · Visa · Flights'],
            'price': '₹68,000',
        },
        'WhatsApp Image 2026-08-08 at 2.47.14 PM (1).jpeg': {
            'badge': 'City Escape',
            'type': 'International City Tour',
            'name': 'Uzbekistan Tour Package',
            'details': ['4 Nights Accommodation', 'Hotel · Breakfast · Visa · Flights'],
            'price': '₹70,000',
        },
        'WhatsApp Image 2026-08-08 at 2.48.39 PM (1).jpeg': {
            'badge': 'Group Departure',
            'type': 'International City Tour',
            'name': 'Dubai Group Tour Package',
            'details': ['5 Nights / 6 Days', 'Hotel · Cruise · Desert Safari · Flights'],
            'price': '₹76,000',
        },
        'WhatsApp Image 2026-08-08 at 2.48.40 PM (1).jpeg': {
            'badge': 'Group Departure',
            'type': 'Island Tour',
            'name': 'Sri Lanka Tour Package',
            'details': ['6 Nights / 7 Days', 'Flights · Hotel · Sightseeing · Visa'],
            'price': '₹67,999',
        },
        'WhatsApp Image 2026-08-08 at 2.48.41 PM.jpeg': {
            'badge': 'Group Departure',
            'type': 'International Tour',
            'name': 'Thailand Tour Package',
            'details': ['6 Nights / 7 Days', 'Flights · Hotel · Sightseeing · Visa'],
            'price': '₹64,999',
        },
    },
    'other Tour Packages': {
        'group-departures-oct-2025-mar-2026.jpeg': {
            'badge': 'Group Departures',
            'type': 'Domestic & International',
            'name': 'Group Departures Oct 2025 – Mar 2026',
            'details': ['8 Destinations', 'Dubai · Kashmir · Shimla · More'],
            'price': 'From ₹6,000',
        },
    },
}

@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/events')
def events():
    return render_template('pages/events.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')
@app.route('/gallery')
def gallery():
    # Get all images dynamically
    gallery_dir = os.path.join(app.static_folder, 'images', 'gallery')
    images = []
    
    if os.path.exists(gallery_dir):
        for root, dirs, files in os.walk(gallery_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    # Create a relative path for the template: 'images/gallery/folder/file.jpg'
                    rel_dir = os.path.relpath(root, app.static_folder)
                    images.append(os.path.join(rel_dir, file).replace('\\', '/'))
                    
    print(f"Gallery Dir: {gallery_dir}, Total Images: {len(images)}")
    return render_template('pages/gallery.html', images=images)

def get_package_cards(folder, category):
    pkg_dir = os.path.join(app.static_folder, 'images', folder)
    packages = []
    package_details = PACKAGE_DETAILS.get(folder, {})
    if os.path.exists(pkg_dir):
        for file in sorted(os.listdir(pkg_dir)):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                details = package_details.get(file, {
                    'badge': 'Custom Package',
                    'type': f'{category} Tour',
                    'name': f'{category} Tour Package',
                    'details': ['Custom Itinerary', 'Contact Us for Details'],
                    'price': 'Contact for price',
                })
                packages.append({
                    **details,
                    'image': f'images/{folder}/{file}',
                    'contact_price': details['price'] == 'Contact for price',
                })
    return packages

@app.route('/packages')
def packages():
    active_category = request.args.get('category', 'domestic').lower()
    if active_category not in {'domestic', 'international', 'other'}:
        active_category = 'domestic'

    package_groups = {
        'domestic': get_package_cards('domestic Tour Packages', 'Domestic'),
        'international': get_package_cards('international Tour Packages', 'International'),
        'other': get_package_cards('other Tour Packages', 'Other'),
    }
    return render_template(
        'pages/packages.html',
        active_category=active_category,
        package_groups=package_groups,
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
