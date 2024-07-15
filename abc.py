import csv

# Read CSV data
products = []
with open('pear_shaped.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row)

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }
        .product {
            display: flex;
            flex-direction: column;
            align-items: center;
            border: 1px solid #ddd;
            margin: 10px;
            padding: 10px;
            border-radius: 5px;
            transition: box-shadow 0.3s;
        }
        .product img {
            max-width: 100%;
            height: auto;
            border-bottom: 1px solid #ddd;
            margin-bottom: 10px;
        }
        .product h2 {
            font-size: 20px;
            margin: 10px 0;
        }
        .product p {
            font-size: 16px;
            margin: 10px 0;
        }
        .product a {
            text-decoration: none;
            color: #007BFF;
        }
        .product a:hover {
            text-decoration: underline;
        }
        .product:hover {
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Product Selection</h1>
        <div class="grid">
"""

for product in products:
    html_content += f"""
            <div class="product">
                <img src="{product['selection1_image']}" alt="{product['selection1_dress_name']}">
                <h2>{product['selection1_dress_name']}</h2>
                <p>Price: ${product['selection1_cost']}</p>
                <a href="{product['selection1_cost_url']}">Buy Now</a>
            </div>
"""

html_content += """
        </div>
    </div>
</body>
</html>
"""

# Write to HTML file
with open('products.html', 'w') as file:
    file.write(html_content)
