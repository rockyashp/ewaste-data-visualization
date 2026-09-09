# E-Waste Intelligence

An interactive Streamlit dashboard for exploring how 20 countries generated and recycled electronic waste in 2022.

The dashboard turns a compact country-level dataset into a visual comparison of scale, recycling performance, and the gap between waste generated and material recovered.

## What You Can Explore

- **The Scale** — total generated waste, recycled material, weighted recycling rate, and the top performer for the current selection.
- **The Leaders** — sortable country rankings with recycling-rate comparisons.
- **The Recycling Gap** — generated-versus-recycled volume charts and a recycling-rate signal map.
- **Country Face-Off** — compare two countries side by side.
- **Data Signals** — automatically generated observations from the selected countries.
- **Data Explorer** — inspect filtered source rows and download the selection as a CSV file.
- **The Team** — project credits for the people behind the visualization.

## Quick Start

### Requirements

- Python 3.10 or newer
- Internet access on first launch if the browser needs to load the dashboard fonts

### Install and run

From the project directory:

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install the project dependencies and start Streamlit:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Deployment

This project is a Streamlit application. It cannot be deployed directly as a Vercel Python Function: Vercel expects a top-level HTTP entry point such as `app`, `application`, or `handler`, while Streamlit starts and manages its own web server.

### Recommended: Streamlit Community Cloud

1. Push this repository to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new app and select the repository and `main` branch.
4. Set the main file path to `app.py`.
5. Deploy.

Streamlit Community Cloud installs `requirements.txt` and runs the app with the correct Streamlit runtime.

Other suitable hosts include Render or Railway when configured as a long-running web service with this start command:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
```

Do not add a fake `app` or `handler` variable to `app.py`; that would satisfy Vercel's error message without making the Streamlit dashboard compatible with Vercel Functions.

## Using the Dashboard

1. Use the country selector to focus the dashboard on one or more countries.
2. Adjust the recycling-rate slider to narrow the range of results.
3. Choose whether rankings are sorted by rate, generated waste, or recycled waste.
4. Use the top navigation to jump between sections.
5. Open **EXPLORE THE RAW DATA** near the end of the page to inspect or download the filtered rows.

The calculations update from the active selection. Clearing every country is prevented from producing misleading empty charts by a visible validation message.

## Dataset

Source file: `e-waste_data_2022_complete.csv`

| Column | Description |
| --- | --- |
| `Country` | Country name |
| `Year` | Dataset year, 2022 |
| `E-Waste Generated (Kt)` | E-waste generated in kilotonnes |
| `E-Waste Recycled (Kt)` | E-waste recycled in kilotonnes |
| `Recycling Rate (%)` | Reported recycling rate as a percentage |

The app cleans column names, converts numeric fields safely, and trims country names before calculating the dashboard metrics.

## Project Structure

```text
.
├── app.py                         # Streamlit application
├── e-waste_data_2022_complete.csv # 2022 country-level dataset
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## Dependencies

- [Streamlit](https://streamlit.io/) for the interactive application
- [Pandas](https://pandas.pydata.org/) for loading and transforming the dataset
- [Plotly](https://plotly.com/python/) for interactive charts

## Project Team

- **Yash Patil** — `24101A0065`
- **Gaurav Ghude** — `24101A0061`
- **Sayali Andhale** — `24101A0024`

## Validation

Run a lightweight syntax check before launching the app:

```bash
python -m py_compile app.py
```

Then start Streamlit and verify the navigation, filters, charts, CSV download, responsive layout, and team section in the browser.
