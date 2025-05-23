from smartphone import Smartphone

catalog = [
    Smartphone(
        brand="Apple",
        model="iPhone 14 Pro Max",
        phone_number="+79211234567"
    ),
    Smartphone(
        brand="Samsung",
        model="Galaxy S23 Ultra",
        phone_number="+79219876543"
    ),
    Smartphone(
        brand="Xiaomi",
        model="Redmi Note 11S",
        phone_number="+79214567890"
    ),
    Smartphone(
        brand="Huawei",
        model="P50 Pro",
        phone_number="+79217890123"
    ),
    Smartphone(
        brand="Google",
        model="Pixel 7 Pro",
        phone_number="+79213216549"
    )
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
