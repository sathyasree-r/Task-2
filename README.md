# Task-2
📝 Automated Sales Report Generation
This project reads sales data from a CSV file, analyzes it, and automatically generates a formatted PDF report using Python and FPDF.

📌 Features
✅ Reads data from a CSV file (data.csv)
✅ Calculates Total Sales, Average Sales, and Best Employee
✅ Groups and summarizes Sales by Department
✅ Generates a clean PDF report (Sales_Report.pdf) with headers, footers, and formatted sections

🛠️ Tech Stack
Python 3.x

Libraries Used:

pandas → Data reading & analysis

fpdf → PDF generation

🚀 Installation & Setup
1️⃣ Clone this repository
git clone https://github.com/your-username/sales-report-generation.git
cd sales-report-generation

2️⃣ Install dependencies
pip install pandas fpdf

3️⃣ Prepare your data file
Your CSV file (data.csv) should be in this format:
| Name  | Department | Sales |
| ----- | ---------- | ----- |
| John  | IT         | 1000  |
| Alice | Marketing  | 2500  |
| Mary  | Sales      | 1800  |
| Bob   | Sales      | 1500  |

▶️ Running the Script
Run the Python script:
python Sales-report-generation.py
✅ Output: A PDF file named Sales_Report.pdf will be generated in the same directory.

📂 Project Structure
sales-report-generation/
│
├── data.csv                    # Input data
├── Sales-report-generation.py   # Python script
├── Sales_Report.pdf             # Auto-generated report
└── README.md                    # Project documentation

📷 Sample Report
The generated PDF looks like this:
Sales Report

Summary
Total Sales: 6800
Average Sales: 1360.00
Best Employee: Mary (1800)

Sales by Department
IT: 1000
Marketing: 2500
Sales: 3300

👨‍💻 Author
Sathyasree 
🌐 GitHub: github.com/sathyasre-r
🤝 Contributing
Pull requests are welcome!

📜 License
This project is licensed under the MIT License.
