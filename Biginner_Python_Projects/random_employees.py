'''Using random, we create a list of employees with fake names, emails, adresses, 
phonenumbers'''

import random

first_names = ["John", "Jane", "Chris", "Joseph", "James", "Davis", "Alex", "Ann", "Tom", "CHristine"]

last_names = ["Thabuks", "Wafula", "Smith", "Muthoni", "Kiptoo", "Namwamba","Shikoko","Naliaka","Wambui", "Wesley"]

street_names = ["Main","High", "Lumumba", "Park", "Moi", "Oak","Pine", "Cedar", "Earl", "Maternity"]

fake_cities = ["Nairobi", "Thika", "Kiambu", "Kisumu", "Homabay", "Mombasa", "Maasai Mara", "Kilifi", "Bondo", "Malindi"]

counties = ["Nairobi", "Machakos", "Mombasa", "Kilifi", "Kwale","Kisumu", "Meru", "Kajiado", "Mandera", "Garisa"]

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f"+254-7{random.randint(10,99)}-{random.randint(100,999)}-{random.randint(100,999)}"

    street_num = random.randint(100,999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    county = random.choice(counties)
    postal_address = random.randint(100, 999)
    address = f"street number & name: {street_num} {street}, county: {county}, Postal Address: {postal_address} {city}"

    email = f"{first.lower()}.{last.lower()}@chilcot.co.ke"

    print(f"{first} {last}\nPhone number: {phone}\n{address}\nEmail: {email}\n")