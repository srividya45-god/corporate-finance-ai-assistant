Corporate Finance AI Assistant

📌 Project Overview

The Corporate Finance AI Assistant is a web-based financial analysis application developed as part of the Learning Block 1 project for the MBA Finance program.

The application combines Python-based financial calculations with Generative AI to help users understand important corporate finance concepts and financial results in simple language.

The project focuses on financial analysis, cost of capital, capital budgeting, and AI-assisted interpretation.

---

👩‍🎓 Student Details

Student Name: Srividya Gundagani
Program: MBA in Finance
Department: MBA in Finance
College: Pallavi Engineering College
Academic Year: 2025–2027
Project: Corporate Finance AI Assistant
Mentor: Mr. Raghavendra Rao

---

🎯 Objectives

The main objectives of this project are:

- To perform important corporate finance calculations using Python.
- To analyse financial performance through financial ratios.
- To calculate Weighted Average Cost of Capital (WACC).
- To evaluate investment projects using NPV, IRR and Payback Period.
- To provide simple explanations of financial results using Generative AI.
- To develop an interactive and user-friendly financial analysis dashboard.
- To demonstrate how Artificial Intelligence can support corporate finance decision-making.

---

🚀 Main Features

1. Ratio Analysis

The application provides financial ratio analysis to understand a company's financial performance.

Examples include:

- Current Ratio
- Debt-to-Equity Ratio
- Net Profit Margin
- Return on Equity (ROE)

---

2. WACC Analysis

The application calculates Weighted Average Cost of Capital (WACC) to estimate the company's overall cost of financing.

WACC can help in evaluating investment decisions and determining an appropriate required rate of return.

---

3. Capital Budgeting

The application evaluates investment projects using:

- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Payback Period

These techniques help assess whether a proposed investment project should be accepted or rejected.

---

4. AI Assistant

The application includes an AI Assistant that can answer corporate finance questions and provide financial explanations in plain English.

The AI integration uses the Anthropic Claude API.

The API key is stored securely using Streamlit Secrets and is not included in the GitHub source code.

---

🧮 Methodology

The project follows a hybrid approach:

1. Financial data is entered by the user.
2. Python and Pandas process the financial data.
3. Financial ratios and other calculations are performed programmatically.
4. WACC and capital budgeting calculations are performed using Python.
5. Generative AI is used to interpret financial information and provide explanations.
6. The results are displayed through an interactive Streamlit dashboard.

This approach separates exact financial calculations from AI-based interpretation.

---

🛠️ Technologies Used

- Python 3
- Streamlit
- Pandas
- NumPy
- NumPy-Financial
- Matplotlib / Plotly
- Anthropic Claude API
- GitHub
- Streamlit Community Cloud

---

📊 Sample Project Results

The application can analyse sample financial information such as:

Financial Metric| Sample Result
Revenue| ₹1,260
Net Profit| ₹121
Net Profit Margin| 9.6%
ROE| 16.9%
Debt-to-Equity| 0.80
Current Ratio| 1.68
WACC| 11.06%
NPV| ₹122.7
IRR| 19.4%
Payback Period| 3.25 years

Based on the sample capital budgeting results, the project recommendation is ACCEPT.

---

💻 Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/corporate-finance-ai-assistant.git

Move into the project directory:

cd corporate-finance-ai-assistant

Install the required packages:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

---

🔐 API Configuration

The Anthropic API key should not be written directly inside "app.py".

The application reads the API key using Streamlit Secrets:

st.secrets["ANTHROPIC_API_KEY"]

For deployment, the secret should be added through the Streamlit application's Secrets settings.

Never upload or commit the actual API key to GitHub.

---

🌐 Deployment

The application can be deployed using:

Streamlit Community Cloud

The GitHub repository contains the application source code, while sensitive API credentials are maintained separately using Streamlit Secrets.

---

⚠️ Limitations

The current version has the following limitations:

- The AI Assistant depends on an external API.
- Confidential financial information should be anonymized before using the AI feature.
- The application does not currently provide live market data.
- Multi-company comparison is not currently included.
- AI-generated information should be treated as decision support rather than a replacement for professional financial judgement.
- API availability and usage limits may affect the AI Assistant.

---

🔮 Future Scope

Future versions of the project can include:

- Multi-company financial comparison
- Financial benchmarking
- Sensitivity and scenario analysis
- Monte Carlo simulation
- DuPont analysis
- Discounted Cash Flow (DCF) analysis
- Live market data
- Automated data validation
- Additional file formats
- Multimodal financial analysis
- Cloud-based authentication and encryption
- Human verification and cross-checking of AI-generated results

---

📚 Conclusion

The Corporate Finance AI Assistant demonstrates how traditional financial analysis can be combined with Generative AI to create an interactive corporate finance decision-support application.

Python is used for structured and accurate financial calculations, while Generative AI provides explanations and assists users in understanding financial concepts and results.

The project demonstrates the potential of AI-assisted tools in improving accessibility and understanding of corporate finance analysis.

---

👩‍🎓 Author

Srividya Gundagani
MBA Finance
Pallavi Engineering College
Academic Year: 2025–2027
