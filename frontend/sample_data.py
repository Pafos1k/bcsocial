"""Fixed deck examples grouped by feature, ready to move into future apps.

These are display values, not models. Image names match the original PPTX media.
"""
PROFILE = {
    "name": "Gigi Jones", "email": "jeneen.jones@bc.edu", "year": "2027",
    "photo": "image12.png",
    "bio": "Senior studying CS + Econ. Always down for pickup soccer or a coffee chat about internships.",
    "majors": ["Computer Science", "Economics"],
    "interests": ["Intramurals", "Startups", "Music", "Volunteering"],
    "clubs": [("CS Club", "VP"), ("Boston College Club Cycling", "Member"), ("Investment Club", "Member")],
}
CONNECTIONS = [
    {"name": "Jack Mullen", "year": "27", "image": "image36.jpg"},
    {"name": "Anna Cortez", "year": "27", "image": "image67.jpg"},
    {"name": "Sam Tristan", "year": "28", "image": "image143.jpg"},
]
SUGGESTED_PEOPLE = [{"name": "Priya Nair", "year": "27", "image": "image30.jpg"}, CONNECTIONS[0]]
CLUBS = [
    {"name": "CS Club", "image": "image44.jpg"},
    {"name": "Boston College Club Cycling", "image": "image54.png"},
    {"name": "Investment Club", "image": "image59.jpg"},
    {"name": "Filmmakers Guild", "image": "image45.png"},
]
EBOARD = [("Anna Cortez", "President"), ("Marco Diaz", "Co-President"), ("Maria Dunphy", "Vice President")]
COMMUNITIES = [
    {"name": "A24 Film Fans", "image": "image60.png"},
    {"name": "Boston Runners", "image": "image69.jpg"},
    {"name": "Vinyl & Coffee", "image": "image187.jpg"},
]
CLUB_EVENTS = [
    {"title": "Stock Pitch Night", "meta": "Investment Club · Tue 7:00 PM · Fulton 511", "month": "SEP", "day": "30", "tone": "cream"},
    {"title": "Fall Hackathon Kickoff", "meta": "CS Club · Thu 6:00 PM · Stokes Hall S195", "month": "OCT", "day": "2", "image": "image114.jpg"},
    {"title": "Saturday Morning Group Ride", "meta": "BC Club Cycling · Sat 9:00 AM · Commonwealth Ave Gate", "month": "OCT", "day": "4", "tone": "cream"},
]
CAMPUS_EVENTS = [
    {"title": "UGBC Fall Concert", "meta": "UGBC · Fri 8:00 PM · Conte Forum", "month": "OCT", "day": "3", "image": "image46.png", "url": "events:detail"},
    {"title": "Student Short Film Showcase", "meta": "Filmmakers Guild · Sun 7:30 PM · Devlin 008", "month": "OCT", "day": "5"},
    {"title": "Fall Career Fair", "meta": "Career Center · Wed 11:00 AM · Corcoran Commons", "month": "OCT", "day": "8", "image": "image134.png"},
]
LISTINGS = [
    {"title": "Mini-Fridge", "price": "$40", "image": "image29.jpg", "url": "messaging:marketplace"},
    {"title": "Intro to Econ, 9th ed.", "price": "$25", "image": "image181.jpg"},
    {"title": "Desk Lamp", "price": "$10", "image": "image157.jpg"},
    {"title": "Twin XL Sheets (2 sets)", "price": "$15", "image": "image158.jpg"},
    {"title": "Bluetooth Speaker", "price": "$30", "image": "image155.jpg"},
    {"title": "Longboard", "price": "$60", "image": "image162.jpg"},
]
BC_NEWS = [
    {"title": "BC Eagles clinch bid for ACC tournament", "meta": "The Heights · 3h ago", "image": "image184.png"},
    {"title": "UGBC announces fall concert lineup", "meta": "BC Social News · 6h ago", "image": "image179.jpg"},
    {"title": "Dining hall hours extend for finals week", "meta": "BC Social News · 1d ago", "image": "image188.jpg"},
]
TODAY_NEWS = [
    {"title": "MBTA announces Green Line weekend closures", "meta": "Wire · 4h ago", "image": "image183.png"},
    {"title": "Fed holds rates steady, cites slowing inflation", "meta": "Wire · 8h ago", "image": "image180.png"},
    {"title": "Nor’easter expected to bring snow this weekend", "meta": "Wire · 10h ago", "image": "image186.png"},
]
CONVERSATIONS = {
    "individual": {
        "title": "Jack Mullen '27", "subtitle": "Connection since Sept 2026", "image": "image36.jpg", "placeholder": "Write a message…",
        "bubbles": [{"text": "hey are you going to the concert friday?"}, {"text": "yeah! already RSVPed, see you there", "outgoing": True, "receipt": "Read · 2:14 PM"}],
    },
    "club": {
        "title": "CS Club — Fall Hackathon", "subtitle": "18 members · Club group chat", "image": "image44.jpg", "placeholder": "Message the group…",
        "bubbles": [{"sender": "Anna Cortez (President)", "text": "team signups close Thursday at midnight!"}, {"sender": "Jack Mullen", "text": "can it be a team of 3, or does it have to be 4?"}, {"text": "3 is fine, 2-4 is the range", "outgoing": True}],
    },
    "marketplace": {
        "title": "Mini-Fridge, barely used", "subtitle": "Listed by You", "image": "image29.jpg", "price": "$40", "placeholder": "Write a message…",
        "bubbles": [{"text": "is the fridge still available?"}, {"text": "yep! can do pickup tonight after 6 near Vanderslice", "outgoing": True}],
    },
}
