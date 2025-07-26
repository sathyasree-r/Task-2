import pandas as pd
from fpdf import FPDF

# ----------- STEP 1: READ AND ANALYZE DATA -----------
df = pd.read_csv("data.csv")

# Basic analysis
total_sales = df['Sales'].sum()
avg_sales = df['Sales'].mean()
best_employee = df.loc[df['Sales'].idxmax()]['Name']
best_sales = df['Sales'].max()

# Group sales by department
sales_by_dept = df.groupby("Department")['Sales'].sum()

# ----------- STEP 2: GENERATE PDF REPORT -----------
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Sales Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

pdf = PDF()
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Summary", ln=True)

# Summary
pdf.set_font("Arial", "", 11)
pdf.multi_cell(0, 10, 
    f"Total Sales: {total_sales}\n"
    f"Average Sales: {avg_sales:.2f}\n"
    f"Best Employee: {best_employee} ({best_sales})"
)

# Sales by Department
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Sales by Department", ln=True)
pdf.set_font("Arial", "", 11)

for dept, sales in sales_by_dept.items():
    pdf.cell(0, 10, f"{dept}: {sales}", ln=True)

# ----------- STEP 3: SAVE PDF -----------
pdf.output("Sales_Report.pdf")
print("✅ Report Generated: Sales_Report.pdf")
