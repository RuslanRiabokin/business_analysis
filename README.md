# Customer Support Analysis for E-commerce Marketplace

## Overview

This project analyzes the performance of a customer support team in a large e-commerce marketplace with two service branches: retail and wholesale. The goal was to assess the quality of customer service, identify inefficiencies, and suggest actionable improvements based on data analysis.

## Objectives

- Evaluate whether support agents meet the service expectations:
  - Requests should be answered within 15 minutes of creation.
  - Any delay over 45 minutes is considered excessive.
- Identify underperforming agents.
- Determine whether support team size is sufficient.
- Analyze traffic and workload distribution between teams.
- Explore the potential benefits of merging retail and wholesale teams.

## Data Sources

- **CSV File**: Order data used to analyze customer purchase behavior.
- **SQLite Database**: Request handling logs from support agents.
- **Tableau Dashboard** and **Python Visualizations**: Used to visualize agent performance and response time patterns.

## Technologies Used

- Python (`pandas`, `sqlite3`, `matplotlib`)
- SQL (CTEs, window functions)
- Tableau

## Key Results

- **Request Handling Time**: Most requests were completed within 5 minutes once started.
- **Delays in Response**: Many requests exceeded the expected 15-minute response time, with some delays over 45 minutes.
- **Agent Outliers**: Agent with ID 133 had significantly higher average processing time.
- **Working Hours Mismatch**: Peak request hours (1:00–15:00) did not align with agent activity hours (6:00–23:00).
- **Uneven Workload**: Wholesale team consistently received more requests than retail team.
- **Inconsistent Agent Utilization**: Average time spent per day varied significantly between agents.

## Recommendations

- Shift support agent schedules to start earlier (1:00 AM) to match request volume.
- Investigate agent 133's request types and workload for possible reassignment or training.
- Consider merging support queues to balance load across all agents.
- Analyze the internal process between request creation and handling to identify bottlenecks.

## Deliverables

- Jupyter Notebook with all code and analysis
- SQL scripts for database queries
- Visualizations in Python and Tableau
- Presentation with findings and optimization strategies

---


