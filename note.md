# The Corner Loaf — Lab Notes

## Brief to priorities

### Three things a customer must learn within five seconds on a phone

#### 1. Whether there is bread today, and what is on the shelf

**Supporting words from the brief:**

> “Regulars have mentioned they cannot quickly tell what is actually available that day”

> “It makes you work to find out something simple, like whether there is bread today.”

> “People come in, they see what is on the shelf that morning, they buy it.”

#### 2. That it is a small, warm, real neighbourhood bakery, not a chain

**Supporting words from the brief:**

> “new visitors say it does not feel like the same warm, unfussy place they experience in person”

> “it should not feel corporate or overly polished”

> “it feels like a small, real place, not a chain”

#### 3. Where it is, so they can decide to stop in on the walk

**Supporting words from the brief:**

> “a small neighbourhood bakery on Boundary Road in East Legon, Accra”

> “A lot of his regulars are commuters who walk past every morning”

> “people increasingly check the website on their phones, mid-walk, to decide whether it is worth stopping in today”

## Sketch and short note

I drew two mobile layouts and chose Sketch A because it puts the customer's immediate questions before the supporting content.

### Sketch A — selected

[View Sketch A](sketches/corner-loaf-a.png)

I brought the three vital answers into the first part of the page so a customer checking their phone mid-walk can quickly decide whether to stop:

- **What is available today:** I placed the product rows near the top, with images, descriptions and prices together so customers can quickly see what they might buy.
- **What kind of bakery it is:** I placed the bakery name and space for a short introduction first, to communicate the small neighbourhood bakery's identity without a long introduction.
- **Where it is:** I included the Boundary Road location panel directly after the products so customers can find the shop after seeing what is on the shelf.

I also placed the opening status above the products to help customers judge whether they can visit. I kept FAQs, the preorder form, About Marcus and messaging below these essentials so they do not delay the quick stop-in decision. The preorder form gives customers a way to request items ahead of a visit, while About Marcus adds the personal story behind the shop.

### Sketch B — alternative considered

[View Sketch B](sketches/corner-loaf-b.png)

I explored a layout with a large image and Preorder button first, followed by opening hours, location and today's products. I did not choose it because the image and preorder action push availability further down, making commuters work harder to answer their main question.

## Food image optimization

I made all three food photographs used on the page WebP and replaced the "Available today" placeholders with the supplied sourdough, whole wheat and chin chin photos. I used my locally installed FFmpeg to convert the two JPEGs and optimize the existing Chin Chin WebP, with quality 80, compression level 6 and a maximum width of 640px without enlarging smaller images.

The served photographs total 118,478 bytes, down from 356,944 bytes (about 67% smaller). I kept the source originals, added descriptive alt text and image dimensions, and used simple CSS to fit the photos into the mobile rows and desktop cards. No JavaScript is needed.
