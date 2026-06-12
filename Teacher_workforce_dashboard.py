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

    col1, col2 = st.columns([3, 1])

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
            yaxis_range=[25, 50],
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
            textfont=dict(family="Arial", size=12, color="black")
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
            delta=f"{delta_bipoc} pp vs. prior year"
    )

    st.caption("**Metric definition:** Classroom teachers who identify as American Indian/Alaskan Native, Asian, Black or African American, Hispanic/Latinx, Two or More Races, and Native Hawaiian / Pacific Islander in the PDE data set for Philadelphia schools. Teachers employed by a school/LEA will be counted as 1 for each unit of analysis teacher regardless of their FTE. [Data Source: PDE Professional Personnel Individual Staff Report](https://www.pa.gov/agencies/education/data-and-reporting/school-staff/professional-and-support-personnel)")

    st.divider()

    #---------------------------
    #  Black % over time
    #---------------------------

    # Filter to Black % metric
    black = metrics_data[metrics_data["metric"] == "black_pct"].copy()

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




    #---------------------------
    #  Hispanic % over time
    #---------------------------

    # Filter to Black % metric
    hispanic = metrics_data[metrics_data["metric"] == "hispanic_pct"].copy()

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







elif category == "New Teachers":

    st.header("New Teachers")
    
    #---------------------------
    #  Total New Hires
    #---------------------------

    # Filter to New Hire
    new_hires = metrics_data[metrics_data["metric"] == "new_hires_total"].copy()

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




    #---------------------------
    #  % New Hires BIPOC
    #---------------------------

    # Filter to Black % metric
    new_hires_bipoc = metrics_data[metrics_data["metric"] == "new_hires_bipoc_pct"].copy()

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














elif category == "Teacher Retention":

    st.header("Teacher Retention")

    #---------------------------
    #  Philadelphia County Retention
    #---------------------------

    # Filter to Retention %
    phl_retention = metrics_data[metrics_data["metric"] == "retention_overall_yty"].copy()

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
        yaxis_range=[0, 100],
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

    st.plotly_chart(phl_retention_line)


    #---------------------------
    #  Philadelphia County School-level Retention
    #---------------------------

    # Filter to School-level retention
    phl_schl_retention = metrics_data[metrics_data["metric"] == "retention_school_level"].copy()

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
        yaxis_range=[0, 100],
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



    #---------------------------
    #  Philadelphia County BIPOC Retention
    #---------------------------

    # Filter to BIPOC Retention % Metric
    bipoc_retention = metrics_data[metrics_data["metric"] == "retention_bipoc_yty"].copy()

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
        yaxis_range=[0, 100],
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



    
    #---------------------------
    #  Philadelphia County New Retention
    #---------------------------

    # Filter to BIPOC Retention % Metric
    new_retention = metrics_data[metrics_data["metric"] == "retention_new_yty"].copy()

    # Line chart
    new_retention_line = px.line(
        new_retention,
        x="sy",
        y="value",
        markers=True,
        labels={"sy": "School Year", "value": "% of Teachers"},
        title="% of Philadelphia County BIPOC Teachers Retained"
    )

    new_retention_line.update_layout(
        yaxis_ticksuffix="%",
        yaxis_range=[0, 100],
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
