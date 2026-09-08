import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

PACKAGE_DETAILS = {
    'domestic': {
        'hyderabad.webp': {
            'badge': 'Group Departure',
            'type': 'Domestic Group Tour',
            'name': 'Hyderabad Tour Package',
            'details': ['5 Nights / 6 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹9,500',
        },
        'udaipur.webp': {
            'badge': 'Diwali Offer',
            'type': 'Domestic Group Tour',
            'name': 'Udaipur Tour Package',
            'details': ['4 Nights / 5 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹8,700',
        },
        'kashmir.webp': {
            'badge': 'Group Departure',
            'type': 'Snow Tour',
            'name': 'Kashmir Tour Package',
            'details': ['10 Nights / 11 Days', 'Deluxe & Luxury Options'],
            'price': 'From ₹17,800',
        },
        'goa.webp': {
            'badge': 'Group Departure',
            'type': 'Beach Tour',
            'name': 'Goa Tour Package',
            'details': ['4 Nights / 5 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹7,000',
        },
        'manali.webp': {
            'badge': 'Group Departure',
            'type': 'Hill Station Tour',
            'name': 'Manali Dalhousie Amritsar Tour',
            'details': ['8 Nights / 9 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹16,000',
        },
        'kerala.webp': {
            'badge': 'Diwali Vacation',
            'type': 'Backwater Tour',
            'name': 'Kerala Tour Package',
            'details': ['7 Nights / 8 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹17,000',
        },
        'shimla.webp': {
            'badge': 'Group Departure',
            'type': 'Hill Station Tour',
            'name': 'Shimla Manali Tour Package',
            'details': ['7 Nights / 8 Days', 'Hotel · Food · Sightseeing · Train'],
            'price': '₹13,500',
        },
    },
    'international': {
        'russia.webp': {
            'badge': 'Group Departure',
            'type': 'International Group Tour',
            'name': 'Russia Tour Package',
            'details': ['Flights · Hotel · Sightseeing', 'Visa · Meals Included'],
            'price': '₹1,52,500',
        },
        'turkey.webp': {
            'badge': 'Group Departure',
            'type': 'International Group Tour',
            'name': 'Turkey Tour Package',
            'details': ['10 Nights / 11 Days', 'Flights · Visa · Food · Sightseeing'],
            'price': '₹1,90,000',
        },
        'bali.webp': {
            'badge': 'Island Escape',
            'type': 'Tropical Tour',
            'name': 'Bali Tour Package',
            'details': ['6 Nights / 7 Days', 'Hotel · Breakfast · Sightseeing'],
            'price': '₹66,500',
        },
        'dubai.webp': {
            'badge': 'City Escape',
            'type': 'International City Tour',
            'name': 'Dubai Tour Package',
            'details': ['4 Nights Accommodation', 'Tours · Transfers · Visa · Flights'],
            'price': '₹70,000',
        },
        'baku.webp': {
            'badge': 'City Escape',
            'type': 'International City Tour',
            'name': 'Baku Tour Package',
            'details': ['4 Nights Accommodation', 'Hotel · Breakfast · Visa · Flights'],
            'price': '₹68,000',
        },
        'uzbekistan.webp': {
            'badge': 'City Escape',
            'type': 'International City Tour',
            'name': 'Uzbekistan Tour Package',
            'details': ['4 Nights Accommodation', 'Hotel · Breakfast · Visa · Flights'],
            'price': '₹70,000',
        },
        'dubai-group-tour.webp': {
            'badge': 'Group Departure',
            'type': 'International City Tour',
            'name': 'Dubai Group Tour Package',
            'details': ['5 Nights / 6 Days', 'Hotel · Cruise · Desert Safari · Flights'],
            'price': '₹76,000',
        },
        'sri-lanka.webp': {
            'badge': 'Group Departure',
            'type': 'Island Tour',
            'name': 'Sri Lanka Tour Package',
            'details': ['6 Nights / 7 Days', 'Flights · Hotel · Sightseeing · Visa'],
            'price': '₹67,999',
        },
        'thailand.webp': {
            'badge': 'Group Departure',
            'type': 'International Tour',
            'name': 'Thailand Tour Package',
            'details': ['6 Nights / 7 Days', 'Flights · Hotel · Sightseeing · Visa'],
            'price': '₹64,999',
        },
    },
    'others': {
        'group-departures.webp': {
            'badge': 'Group Departures',
            'type': 'Domestic & International',
            'name': 'Group Departures Oct 2026 – Mar 2027',
            'details': ['8 Destinations', 'Dubai · Kashmir · Shimla · More'],
            'price': 'From ₹6,000',
        },
        'kashmir.webp': {
            'badge': 'Group Departure',
            'type': 'Snow Tour',
            'name': 'Kashmir Deluxe Package',
            'details': ['7 & 21 Nov | 5, 19 & 26 Dec', 'Hotel · Food · Sightseeing'],
            'price': '₹16,600',
        },
        'kashmir2.webp': {
            'badge': 'Group Departure',
            'type': 'Snow Tour',
            'name': 'Kashmir Luxury Package',
            'details': ['9 & 23 Jan', 'Hotel · Food · Sightseeing'],
            'price': '₹18,600',
        },
        'kerala.webp': {
            'badge': 'Group Departure',
            'type': 'Backwater Tour',
            'name': 'Kerala Package',
            'details': ['5 & 15 November', 'Hotel · Food · Sightseeing'],
            'price': '₹17,500',
        },
        'ooty.webp': {
            'badge': 'Group Departure',
            'type': 'Hill Station Tour',
            'name': 'Ooty Mysore Package',
            'details': ['14 November', 'Hotel · Food · Sightseeing'],
            'price': '₹15,000',
        },
        'hyderabad.webp': {
            'badge': 'Group Departure',
            'type': 'City Tour',
            'name': 'Hyderabad Package',
            'details': ['6 & 13 November | 22 Jan', 'Hotel · Food · Sightseeing'],
            'price': '₹8,700',
        },
        'shimla manali.webp': {
            'badge': 'Group Departure',
            'type': 'Hill Station Tour',
            'name': 'Shimla Manali Package',
            'details': ['Nov: 13 & 27 | Dec: 11 & 25', 'Jan: 1, 15 & 28 | March: 13'],
            'price': '₹12,500',
        },
        'goa.webp': {
            'badge': 'Group Departure',
            'type': 'Beach Tour',
            'name': 'Goa Package',
            'details': ['16 November', 'Hotel · Food · Sightseeing'],
            'price': '₹6,400',
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

def get_package_cards(folder, category, files=None):
    pkg_dir = os.path.join(app.static_folder, 'images', folder) if folder else app.static_folder
    packages = []
    package_details = PACKAGE_DETAILS.get(folder or category.lower(), {})
    if files is None and os.path.exists(pkg_dir):
        files = os.listdir(pkg_dir)
    if files is not None:
        for file in sorted(files):
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
                    'image': f'images/{folder}/{file}' if folder else f'images/{file}',
                    'contact_price': details['price'] == 'Contact for price',
                })
    return packages

@app.route('/packages')
def packages():
    active_category = request.args.get('category', 'domestic').lower()
    if active_category not in {'domestic', 'international', 'other'}:
        active_category = 'domestic'

    package_groups = {
        'domestic': get_package_cards('domestic', 'Domestic'),
        'international': get_package_cards('international', 'International'),
        'other': get_package_cards('others', 'Other'),
    }
    return render_template(
        'pages/packages.html',
        active_category=active_category,
        package_groups=package_groups,
    )

if __name__ == '__main__':
    app.run(debug=True, port=5050)
