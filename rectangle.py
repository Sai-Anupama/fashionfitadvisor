import csv

# Function to read CSV data
def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to generate HTML from CSV data
def generate_html(data):
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
            background-color: #f0f0f0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }
        .grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .product {
            flex: 1 1 calc(25% - 20px);
            box-sizing: border-box;
            margin: 10px;
            padding: 10px;
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 5px;
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: box-shadow 0.3s;
        }
        .product img {
            max-width: 100%;
            height: auto;
            border-bottom: 1px solid #ddd;
            margin-bottom: 10px;
        }
        .product h2 {
            font-size: 16px;
            margin: 10px 0;
            text-align: center;
        }
        .product p {
            font-size: 14px;
            margin: 5px 0;
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
        @media (max-width: 1200px) {
            .product {
                flex: 1 1 calc(33.33% - 20px);
            }
        }
        @media (max-width: 768px) {
            .product {
                flex: 1 1 calc(50% - 20px);
            }
        }
        @media (max-width: 480px) {
            .product {
                flex: 1 1 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 align="center">Happy Shopping!!!</h1>
        <div class="grid">
    """
    
    for item in data:
        html_content += f"""
            <div class="product">
                <img src="{item['selection1_image']}" alt="{item['selection1_name']}">
                <h2><a href="{item['selection1_name_url']}">{item['selection1_name']}</a></h2>
                <p>Price: {item['selection1_cost']}</p>
            </div>
        """
    
    html_content += """
        </div>
    </div>
</body>
</html>
    """
    
    return html_content

# Path to your CSV file
csv_file = 'rectangle.csv'

# Read CSV data
csv_data = read_csv(csv_file)

# Generate HTML content
html_content = generate_html(csv_data)

# Save HTML to file
html_file = 'rectangle.html'
with open(html_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f'HTML file "{html_file}" has been created successfully.')
