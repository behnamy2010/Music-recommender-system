👌 حتما — یک **README.md مینیمال** برات آماده کردم که توضیح کوتاه بده، طریقه نصب و اجرا (محلی و Docker) و اجرای تست‌ها رو نشون بده.

---

📄 `README.md`

````markdown
# RadioJavan CLI (Minimal)

A minimal command-line tool that takes a song title and returns 10 recommendations.  
Data is loaded from a CSV file and a pre-trained similarity model (pickle).

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git https://github.com/parvvaresh/Music-recommender-system
cd Music-recommender-system
pip install -r requirements.txt
````

---

## ▶️ Usage

Run locally:

```bash
python RJ_Recommendation_System.py "Gentleman"
```

Example output:

```
 rank          musicName     artistName
    1       Nakoni Bavar        Zedbazi
    2          Mr. Lodeh   Amir Tataloo
    3 To Ke Nisti Pisham          Masih
    4             Moohat Mohsen Yeganeh
    5             Doctor           Sasy
    6      Harjaye Shahr     Ali Yasini
    7        Tekoon Bede          Arash
    8     Ashegham Kardi   Hoorosh Band
    9             Ey Vay          Sahar
   10          Ey Joonam     Sami Beigi
```

---

## 🐳 Run with Docker

Build the image:

```bash
docker build -t radiojavan-cli .
```

Run:

```bash
docker run --rm radiojavan-cli "Gentleman"
```

---

## ✅ Tests

Run tests with **pytest**:

```bash
pytest -v
```

---

## 🧹 Lint

Run linter (**flake8**):

```bash
flake8 .
```
