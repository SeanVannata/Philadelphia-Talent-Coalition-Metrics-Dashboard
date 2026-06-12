import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Philadelphia Citywide Talent Coalition Metrics")

category = st.selectbox(
    "Select a category",
    ["Teacher Diversity", "New Teachers", "Teacher Retention"]
)

# Load data
url = "https://docs.google.com/spreadsheets/d/1U8vxh3-cKioR9kCUHXDNbtdBXmK8F0jv/export?format=xlsx"
metrics_data = pd.read_excel(url)

st.set_page_config(page_title="Philadelphia Teacher Workforce Dashboard", layout="wide")

st.markdown("""
    <style>
    .block-container {
        max-width: 1100px;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# -------------------------
# DIVERSITY METRICS
# -------------------------
# -------------------------

if category == "Teacher Diversity":
    st.header("Teacher Diversity")
    
    # -------------------------
    # BIPOC
    # -------------------------

    bipoc = metrics_data[metrics_data["metric"] == "bipoc_pct"].copy()

    # Metric card
    latest_bipoc = bipoc.sort_values("sy").iloc[-1]["value"]
    prev_bipoc = bipoc.sort_values("sy").iloc[-2]["value"]
    delta_bipoc = round(latest_bipoc - prev_bipoc, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        bipoc_line = px.line(
            bipoc,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County Teachers Who Identify as BIPOC"
        )

        bipoc_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[25, 52],
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=16),
            xaxis=dict(showgrid=False, linecolor="black", linewidth=1,
                    title_font=dict(family="Arial", size=13), tickfont=dict(family="Arial", size=12)),
            yaxis=dict(showgrid=False, linecolor="black", linewidth=1,
                    title_font=dict(family="Arial", size=13), tickfont=dict(family="Arial", size=12))
        )

        bipoc_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=bipoc["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=12, color="black"),
            texttemplate="%{text}"
        )

        st.plotly_chart(bipoc_line, use_container_width=True)

    with col2:
        st.write("")  # pushes the metric down
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% BIPOC (2025-2026)",
            value=f"{latest_bipoc}%",
            delta=f"{delta_bipoc} % points vs. prior year"
    )

    st.caption("**Metric definition:** Classroom teachers who identify as American Indian/Alaskan Native, Asian, Black or African American, Hispanic/Latinx, Two or More Races, and Native Hawaiian / Pacific Islander in the PDE data set for Philadelphia schools. Teachers employed by a school/LEA will be counted as 1 for each unit of analysis teacher regardless of their FTE. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()

    #---------------------------
    #  Black % over time
    #---------------------------

    # Filter to Black % metric
    black = metrics_data[metrics_data["metric"] == "black_pct"].copy()

    # Metric card
    latest_black = black.sort_values("sy").iloc[-1]["value"]
    prev_black = black.sort_values("sy").iloc[-2]["value"]
    delta_black = round(latest_black - prev_black, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        # Line chart
        black_line = px.line(
            black,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County Teachers Who Identify as Black"
        )

        black_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[0, 60],
            xaxis_title="School Year",
            yaxis_title="% of Teachers",
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        black_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=black["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(black_line)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% Black Teachers (2025-2026)",
            value=f"{latest_black}%",
            delta=f"{delta_black} % points vs. prior year"
        )

    st.caption("**Metric definition:** The percentage of Philadelphia County classroom teachers who identify as Black or African American. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()


    #---------------------------
    #  Hispanic % over time
    #---------------------------

    # Filter to Hispanic % metric
    hispanic = metrics_data[metrics_data["metric"] == "hispanic_pct"].copy()

    # Metric card
    latest_hispanic = hispanic.sort_values("sy").iloc[-1]["value"]
    prev_hispanic = hispanic.sort_values("sy").iloc[-2]["value"]
    delta_hispanic = round(latest_hispanic - prev_hispanic, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        # Line chart
        hispanic_line = px.line(
            hispanic,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County Teachers Who Identify as Hispanic"
        )

        hispanic_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[0, 60],
            xaxis_title="School Year",
            yaxis_title="% of Teachers",
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        hispanic_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=hispanic["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(hispanic_line)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% Hispanic Teachers (2025-2026)",
            value=f"{latest_hispanic}%",
            delta=f"{delta_hispanic} % points vs. prior year"
        )

    st.caption("**Metric definition:** The percentage of Philadelphia County classroom teachers who identify as Hispanic. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()





# -------------------------
# -------------------------
# NEW TEACHER METRICS
# -------------------------
# -------------------------

elif category == "New Teachers":

    st.header("New Teachers")
    
    #---------------------------
    #  Total New Hires
    #---------------------------

    # Filter to New Hire
    new_hires = metrics_data[metrics_data["metric"] == "new_hires_total"].copy()

    # Metric card
    latest_new_hires = new_hires.sort_values("sy").iloc[-1]["value"]
    prev_new_hires = new_hires.sort_values("sy").iloc[-2]["value"]
    delta_new_hires = round(latest_new_hires - prev_new_hires, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        # Line chart
        new_hires_line = px.line(
            new_hires,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "Number of Teachers"},
            title="Number of Newly Hired Teachers in Philadelphia County"
        )

        new_hires_line.update_layout(
            yaxis_range=[0, 2000],
            xaxis_title="School Year",
            yaxis_title="# of Teachers",
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        new_hires_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=new_hires["value"],
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(new_hires_line)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="New Hires (2025-2026)",
            value=f"{int(latest_new_hires):,}",
            delta=f"{int(delta_new_hires):+,} vs. prior year"
        )

    st.caption("**Metric definition:** The number of Philadelphia County classroom teachers in their first year teaching in Philadelphia County. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()


    #---------------------------
    #  % New Hires BIPOC
    #---------------------------

    # Filter to BIPOC % metric
    new_hires_bipoc = metrics_data[metrics_data["metric"] == "new_hires_bipoc_pct"].copy()

    # Metric card
    latest_new_hires_bipoc = new_hires_bipoc.sort_values("sy").iloc[-1]["value"]
    prev_new_hires_bipoc = new_hires_bipoc.sort_values("sy").iloc[-2]["value"]
    delta_new_hires_bipoc = round(latest_new_hires_bipoc - prev_new_hires_bipoc, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        # Line chart
        new_bipoc_line = px.line(
            new_hires_bipoc,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County New Hires Who Identify as BIPOC"
        )

        new_bipoc_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[0, 80],
            xaxis_title="School Year",
            yaxis_title="% of Teachers",
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        new_bipoc_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=new_hires_bipoc["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(new_bipoc_line)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% BIPOC New Hires (2025-2026)",
            value=f"{latest_new_hires_bipoc}%",
            delta=f"{delta_new_hires_bipoc} % points vs. prior year"
        )

    st.caption("**Metric definition:** The percentage of newly hired Philadelphia County classroom teachers who identify as BIPOC. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()









# -------------------------
# -------------------------
# Teacher Retention
# -------------------------
# -------------------------
# -------------------------

elif category == "Teacher Retention":

    st.header("Teacher Retention")

    #---------------------------
    #  Philadelphia County Retention
    #---------------------------

    # Filter to Retention %
    phl_retention = metrics_data[metrics_data["metric"] == "retention_overall_yty"].copy()

    # Metric card
    latest_phl_retention = phl_retention.sort_values("sy").iloc[-1]["value"]
    prev_phl_retention = phl_retention.sort_values("sy").iloc[-2]["value"]
    delta_phl_retention = round(latest_phl_retention - prev_phl_retention, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        # Line chart
        phl_retention_line = px.line(
            phl_retention,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County Teachers Retained"
        )

        phl_retention_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[50, 100],
            xaxis_title="School Year",
            yaxis_title="% of Teachers",
            margin=dict(t=60),   
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        phl_retention_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=phl_retention["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(phl_retention_line, use_container_width=True)

    with col2:
        st.write("")  # pushes the metric down
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% Retained (2025-2026)",
            value=f"{latest_phl_retention}%",
            delta=f"{delta_phl_retention} % points vs. prior year"
    )
        
    st.caption("**Metric definition:** The percentage of Philadelphia County classroom teachers in a given year who continue to teach as a classroom teacher in Philadelphia County the following year. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()    


    #---------------------------
    #  Philadelphia County School-level Retention
    #---------------------------

    # Filter to School-level retention
    phl_schl_retention = metrics_data[metrics_data["metric"] == "retention_school_level"].copy()

    # Metric card
    latest_phl_schl_retention = phl_schl_retention.sort_values("sy").iloc[-1]["value"]
    prev_phl_schl_retention= phl_schl_retention.sort_values("sy").iloc[-2]["value"]
    delta_phl_schl_retention = round(latest_phl_schl_retention - prev_phl_schl_retention, 1)

    col1, col2 = st.columns([4, 1])

    with col1: 
        # Line chart
        phl_schl_retention_line = px.line(
            phl_schl_retention,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County Teachers Retained within School"
        )

        phl_schl_retention_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[50, 100],
            xaxis_title="School Year",
            yaxis_title="% of Teachers",
            margin=dict(t=60),   
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        phl_schl_retention_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=phl_schl_retention["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(phl_schl_retention_line)

    with col2:
        st.write("") 
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% Retained (2025-2026)",
            value=f"{latest_phl_schl_retention}%",
            delta=f"{delta_phl_schl_retention} % points vs. prior year"
    )
        
    st.caption("**Metric definition:** The percentage of Philadelphia County classroom teachers in a given year who continue to teach as a classroom teacher in the same Philadelphia County school the following year. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider() 

    #---------------------------
    #  Philadelphia County BIPOC Retention
    #---------------------------

    # Filter to BIPOC Retention % Metric
    bipoc_retention = metrics_data[metrics_data["metric"] == "retention_bipoc_yty"].copy()

    # Metric card
    latest_bipoc_retention = bipoc_retention.sort_values("sy").iloc[-1]["value"]
    prev_bipoc_retention = bipoc_retention.sort_values("sy").iloc[-2]["value"]
    delta_bipoc_retention = round(latest_bipoc_retention - prev_bipoc_retention, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        # Line chart
        bipoc_retention_line = px.line(
            bipoc_retention,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County BIPOC Teachers Retained"
        )

        bipoc_retention_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[50, 100],
            xaxis_title="School Year",
            yaxis_title="% of Teachers",
            margin=dict(t=60),
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        bipoc_retention_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=bipoc_retention["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(bipoc_retention_line)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% Retained (2025-2026)",
            value=f"{latest_bipoc_retention}%",
            delta=f"{delta_bipoc_retention} % points vs. prior year"
        )

    st.caption("**Metric definition:** The percentage of Philadelphia County BIPOC classroom teachers in a given year who continue to teach as a classroom teacher in Philadelphia County the following year. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()


    #---------------------------
    #  Philadelphia County New Teacher Retention
    #---------------------------

    # Filter to New Teacher Retention % Metric
    new_retention = metrics_data[metrics_data["metric"] == "retention_new_yty"].copy()

    # Metric card
    latest_new_retention = new_retention.sort_values("sy").iloc[-1]["value"]
    prev_new_retention = new_retention.sort_values("sy").iloc[-2]["value"]
    delta_new_retention = round(latest_new_retention - prev_new_retention, 1)

    col1, col2 = st.columns([4, 1])

    with col1:
        # Line chart
        new_retention_line = px.line(
            new_retention,
            x="sy",
            y="value",
            markers=True,
            labels={"sy": "School Year", "value": "% of Teachers"},
            title="% of Philadelphia County New Teachers Retained"
        )

        new_retention_line.update_layout(
            yaxis_ticksuffix="%",
            yaxis_range=[50, 100],
            xaxis_title="School Year",
            yaxis_title="% of Teachers",
            margin=dict(t=60),
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Arial", color="black"),
            title_font=dict(family="Arial", size=18),
            xaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=15, color="black")
            ),
            yaxis=dict(
                showgrid=False,
                linecolor="black",
                linewidth=1,
                title_font=dict(family="Arial", size=15, color="black"),
                tickfont=dict(family="Arial", size=11, color="black")
            ),
            width=800,
            height=400
        )

        new_retention_line.update_traces(
            line=dict(width=2),
            mode="lines+markers+text",
            text=new_retention["value"].apply(lambda x: f"{x}%"),
            textposition="top center",
            textfont=dict(family="Arial", size=15, color="black")
        )

        st.plotly_chart(new_retention_line)

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.metric(
            label="% Retained (2025-2026)",
            value=f"{latest_new_retention}%",
            delta=f"{delta_new_retention} % points vs. prior year"
        )

    st.caption("**Metric definition:** The percentage of Philadelphia County new classroom teachers (3 or fewer years of experience in Philadelphia County) in a given year who continue to teach as a classroom teacher in Philadelphia County the following year. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()
