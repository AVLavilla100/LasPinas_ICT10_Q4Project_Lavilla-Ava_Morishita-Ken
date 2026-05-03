from pyscript import document

class Photo:
    def __init__(self, name, caption, src):
        self.name = name        
        self.caption = caption  
        self.src = src          

    def render_card(self):
        card = document.createElement("div")
        card.className = "photo-card"

        # Image element
        img = document.createElement("img")
        img.src = self.src
        img.alt = self.caption

        # Card body
        body = document.createElement("div")
        body.className = "card-body"

        title = document.createElement("p")
        title.className = "card-title"
        title.textContent = self.name

        desc = document.createElement("p")
        desc.className = "card-text"
        desc.textContent = self.caption

        body.appendChild(title)
        body.appendChild(desc)
        card.appendChild(img)
        card.appendChild(body)

        return card


class Gallery:
    def __init__(self):
        self.photos = []   
   
    def add_photo(self, photo):
        self.photos.append(photo)

    def render(self, container_id):
        container = document.querySelector(f"#{container_id}")
        container.innerHTML = ""

        for photo in self.photos:
            card = photo.render_card()    # call each photo's method
            container.appendChild(card)



gallery = Gallery()

photos_data = [
    ("Intramurals",   "A day devoted to sports. This 2026, Yellow Tigers won as overall champion in the Las Pinas campus. ",       "intramurals2.png"),
    ("Joint Campout",     "Held at Preziosa farms, both grade 6 and 10 learned essential skills for development and growth. ",    "jointcampout.png"),
    ("CAT Graduation", "An important milestone for the grade 10 as they graduate from citizenship training to be a devoted peacebuilder and leader.",      "catgraduation.png"),
    ("Sabayang Bigkas",   "An in-house event where grade 10 students performed a Filipino literature piece and captured the eyes of many.",    "sabayangbigkas.png")
]

for name, caption, src in photos_data:
    photo = Photo(name, caption, src)  
    gallery.add_photo(photo)

gallery.render("gallery-grid")

status = document.querySelector("#py-status")
status.textContent = f"Showing {len(gallery.photos)} highlights."
status.style.color = "#555"