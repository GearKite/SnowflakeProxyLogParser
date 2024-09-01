import re
import sys
from datetime import datetime, timedelta

import pandas as pd
import plotly.express as px

# Regular expression pattern to match the log lines
p = re.compile(
    r"^.*? (\d*?\/\d*?\/\d*? \d*?:\d*?:\d*?) In the last (\d*?)h(\d*?)m(\d*?)s, there were (\d*?) completed connections. Traffic Relayed ↓ (\d*?) KB, ↑ (\d*?) KB.$"
)

# Initialize lists to store the extracted data
timestamps = []
downloads = []
uploads = []
connections = []

if len(sys.argv) < 2:
    print("You must provide a log file path as the first argument!")
    sys.exit(1)

FILE_NAME = sys.argv[1]

# Read the log file
with open(FILE_NAME, "r", encoding="utf8") as f:
    logs = f.readlines()

# Parse each line in the log file
for line in logs:
    m = p.match(line)

    if m is None:
        continue

    # Extract timestamp and calculate the start time
    timestamp = datetime.strptime(m.group(1), "%Y/%m/%d %H:%M:%S")
    delta = timedelta(
        hours=int(m.group(2)), minutes=int(m.group(3)), seconds=int(m.group(4))
    )
    full_time = timestamp - delta

    # Extract download and upload values
    download = int(m.group(6)) / 1000
    upload = int(m.group(7)) / 1000

    # Append the extracted data to the lists
    timestamps.append(full_time)
    downloads.append(download)
    uploads.append(upload)

# Create a DataFrame from the extracted data
data = {
    "Timestamp": timestamps,
    "Download (MB)": downloads,
    "Upload (MB)": uploads,
}
df = pd.DataFrame(data)

# Create a line chart using Plotly Express
fig = px.line(
    df,
    x="Timestamp",
    y=["Download (MB)", "Upload (MB)"],
    title="Traffic Over Time (Snowflake Proxy)",
    labels={"value": "Traffic (MB)", "variable": "Type"},
    markers=True,
)

# Show the plot
fig.show()

print("Total download:", sum(downloads), end=" MB \n")
print("Total upload:", sum(uploads), end=" MB \n")
