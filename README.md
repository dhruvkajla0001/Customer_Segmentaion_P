<!DOCTYPE html>
<html>
<head>
    <title>Customer Segmentation Dashboard - README</title>
</head>
<body>

<h1>Customer Segmentation Dashboard</h1>

<p>
This project performs <strong>customer segmentation</strong> using KMeans clustering
and visualizes the results through a <strong>Streamlit dashboard</strong>.
The dataset is synthetic and contains 1,000 customers with the following features:
Age, Recency, Frequency, Monetary Value, Tenure, Preferred Channel, and Cluster Assignments.
</p>

<h2>Project Structure</h2>
<ul>
    <li><code>Customer_Segmentation_Final.ipynb</code> - Jupyter Notebook for generating data, performing EDA, clustering, and saving results.</li>
    <li><code>segmented_customers.csv</code> - The final dataset with customer segments.</li>
    <li><code>app.py</code> - Streamlit dashboard to visualize and explore customer segments.</li>
    <li><code>README.html</code> - This documentation file.</li>
</ul>

<h2>Steps to Run</h2>
<ol>
    <li>Ensure you have Python installed (3.8+ recommended).</li>
    <li>Install dependencies:
        <pre>pip install streamlit pandas numpy matplotlib seaborn scikit-learn plotly</pre>
    </li>
    <li>Run the notebook to generate <code>segmented_customers.csv</code>:
        <pre>jupyter notebook Customer_Segmentation_Final.ipynb</pre>
    </li>
    <li>Launch the Streamlit dashboard:
        <pre>streamlit run app.py</pre>
    </li>
    <li>Open <code>http://localhost:8501</code> in your browser.</li>
</ol>

<h2>Dashboard Features</h2>
<ul>
    <li><strong>Filters:</strong> Filter customers by Segment and Preferred Channel.</li>
    <li><strong>Visualizations:</strong>
        <ul>
            <li>Pie Chart showing segment distribution.</li>
            <li>Interactive bubble chart (Recency vs Monetary, bubble size = Frequency).</li>
        </ul>
    </li>
    <li><strong>Cluster Summary Table:</strong> Displays average metrics per segment.</li>
    <li><strong>Data Export:</strong> Download the filtered customer list as CSV.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li>Add interactive 3D cluster visualization using Plotly.</li>
    <li>Include automated text insights for each segment.</li>
    <li>Integrate with a real CRM or database for live data.</li>
</ul>

<p><strong>Author:</strong> Your Name</p>

</body>
</html>
