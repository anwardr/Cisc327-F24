from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates')

# Dummy data for demonstration with image URLs and prices
medicines = [
    {
        "name": "Aspirin",
        "description": "Aspirin is a widely used over-the-counter medication known for its ability to reduce pain, fever, and inflammation. It works by inhibiting the production of certain natural substances in the body that cause swelling and discomfort. In addition to treating conditions such as headaches, muscle pain, and arthritis, aspirin is often recommended in low doses for its blood-thinning properties to help prevent heart attacks, strokes, and blood clot-related issues. However, it may not be suitable for individuals with certain medical conditions, such as bleeding disorders or stomach ulcers",
        "image": "https://thumbs.dreamstime.com/b/aspirin-18931443.jpg",
        "price": "$4.99"
    },
    {
        "name": "Ibuprofen",
        "description": "Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) that is commonly used to alleviate pain, reduce fever, and diminish inflammation. It is effective in treating a variety of conditions, including headaches, toothaches, back pain, arthritis, menstrual cramps, and minor injuries. By blocking the body's production of inflammatory substances, ibuprofen provides relief from swelling and discomfort. It is generally safe for short-term use, but long-term or excessive use may lead to side effects, such as stomach upset or kidney issues",
        "image": "https://images.squarespace-cdn.com/content/v1/64fa119384cfa04842cde737/1720711558094-KVI1UJF6305WUISRWUML/69367-394-01_05.JPG?format=1000w",
        "price": "$5.99"
    },
    {
        "name": "Paracetamol",
        "description": "Paracetamol, also known as acetaminophen, is a popular pain reliever and fever reducer. It is frequently used for conditions like headaches, muscle aches, arthritis, backaches, toothaches, colds, and fevers. Unlike NSAIDs, paracetamol does not have significant anti-inflammatory effects, making it a suitable choice for those who cannot tolerate NSAIDs. It works by altering the way the body senses pain and regulates temperature. While generally safe when used as directed, overuse or high doses can lead to liver damage, so it's important to adhere to the recommended dosage",
        "image": "https://c8.alamy.com/comp/DTANR9/box-of-32-paracetamol-tablets-caplets-on-a-white-background-DTANR9.jpg",
        "price": "$3.99"
    },
]

@app.route("/", methods=["GET", "POST"])
def home():
    selected_medicine = None
    if request.method == "POST":
        medicine_name = request.form.get("medicine_name", "").lower()
        for medicine in medicines:
            if medicine_name in medicine["name"].lower():
                selected_medicine = medicine
                break
    return render_template("index.html", medicine=selected_medicine)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
