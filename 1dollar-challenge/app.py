import streamlit as st
from portfolio import Portfolio
from proposal import Proposal
import os
from fpdf import FPDF

def generate_portfolio_pdf(portfolio):
    """Generate a PDF version of the portfolio"""
    pdf = FPDF()
    pdf.add_page()
    
    # Add header
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 20, 'Professional Portfolio', 0, 1, 'C')
    
    # Personal Information
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Personal Information', 0, 1)
    pdf.set_font('Arial', '', 12)
    
    personal_info = portfolio.personal_info
    pdf.cell(0, 10, f"Name: {personal_info['name']}", 0, 1)
    pdf.cell(0, 10, f"Title: {personal_info['title']}", 0, 1)
    pdf.cell(0, 10, f"Email: {personal_info['email']}", 0, 1)
    pdf.cell(0, 10, f"Phone: {personal_info['phone']}", 0, 1)
    pdf.cell(0, 10, f"Location: {personal_info['location']}", 0, 1)
    if personal_info['website']:
        pdf.cell(0, 10, f"Website: {personal_info['website']}", 0, 1)
    
    # Skills
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Skills', 0, 1)
    pdf.set_font('Arial', '', 12)
    
    for skill in portfolio.skills:
        pdf.cell(0, 10, f"- {skill['name']} - {skill['level']}", 0, 1)
    
    # Experience
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Work Experience', 0, 1)
    pdf.set_font('Arial', '', 12)
    
    for exp in portfolio.experience:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, f"{exp['position']} at {exp['company']}", 0, 1)
        pdf.set_font('Arial', 'I', 12)
        pdf.cell(0, 10, f"Duration: {exp['duration']}", 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, exp['description'])
        pdf.ln(5)
    
    # Education
    if portfolio.education:
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Education', 0, 1)
        pdf.set_font('Arial', '', 12)
        
        for edu in portfolio.education:
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, f"{edu['degree']} - {edu['institution']}", 0, 1)
            pdf.set_font('Arial', 'I', 12)
            pdf.cell(0, 10, f"Year: {edu['year']}", 0, 1)
            if edu['description']:
                pdf.set_font('Arial', '', 12)
                pdf.multi_cell(0, 10, edu['description'])
            pdf.ln(5)
    
    # Projects
    if portfolio.projects:
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Projects', 0, 1)
        pdf.set_font('Arial', '', 12)
        
        for project in portfolio.projects:
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, project['name'], 0, 1)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 10, project['description'])
            pdf.cell(0, 10, f"Technologies: {project['technologies']}", 0, 1)
            if project['link']:
                pdf.cell(0, 10, f"Link: {project['link']}", 0, 1)
            pdf.ln(5)
    
    return pdf

def main():
    st.set_page_config(page_title="Freelancer Portfolio & Proposal Generator", layout="wide")
    
    st.title("Freelancer Portfolio & Job Proposal Generator")
    
    # Initialize session state
    if 'portfolio' not in st.session_state:
        st.session_state.portfolio = Portfolio()
    
    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Portfolio", "Create Proposal"])
    
    if page == "Portfolio":
        show_portfolio_page()
    else:
        show_proposal_page()

def show_portfolio_page():
    st.header("Create Your Portfolio")
    
    # Personal Information
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name")
        email = st.text_input("Email")
        location = st.text_input("Location")
    
    with col2:
        title = st.text_input("Professional Title")
        phone = st.text_input("Phone Number")
        website = st.text_input("Website (optional)")
    
    if st.button("Save Personal Info"):
        st.session_state.portfolio.set_personal_info(name, title, email, phone, location, website)
        st.success("Personal information saved!")
    
    # Skills
    st.subheader("Skills")
    col1, col2 = st.columns(2)
    
    with col1:
        skill = st.text_input("Skill Name")
    with col2:
        level = st.selectbox("Proficiency Level", ["Beginner", "Intermediate", "Expert"])
    
    if st.button("Add Skill"):
        st.session_state.portfolio.add_skill(skill, level)
        st.success(f"Added skill: {skill}")
    
    # Experience
    st.subheader("Work Experience")
    col1, col2 = st.columns(2)
    
    with col1:
        company = st.text_input("Company Name")
        position = st.text_input("Position")
    with col2:
        duration = st.text_input("Duration (e.g., 2020-2022)")
        description = st.text_area("Job Description")
    
    if st.button("Add Experience"):
        st.session_state.portfolio.add_experience(company, position, duration, description)
        st.success(f"Added experience at {company}")
    
    # Education
    st.subheader("Education")
    col1, col2 = st.columns(2)
    
    with col1:
        institution = st.text_input("Institution")
        degree = st.text_input("Degree")
    with col2:
        year = st.text_input("Year")
        edu_description = st.text_area("Description (optional)")
    
    if st.button("Add Education"):
        st.session_state.portfolio.add_education(institution, degree, year, edu_description)
        st.success(f"Added education at {institution}")
    
    # Projects
    st.subheader("Projects")
    col1, col2 = st.columns(2)
    
    with col1:
        project_name = st.text_input("Project Name")
        technologies = st.text_input("Technologies Used")
    with col2:
        project_description = st.text_area("Project Description")
        project_link = st.text_input("Project Link (optional)")
    
    if st.button("Add Project"):
        st.session_state.portfolio.add_project(project_name, project_description, technologies, project_link)
        st.success(f"Added project: {project_name}")
    
    # Generate Portfolio PDF
    if st.button("Generate Portfolio PDF"):
        pdf = generate_portfolio_pdf(st.session_state.portfolio)
        pdf_filename = "portfolio.pdf"
        pdf.output(pdf_filename)
        
        with open(pdf_filename, "rb") as pdf_file:
            st.download_button(
                label="Download Portfolio PDF",
                data=pdf_file,
                file_name=pdf_filename,
                mime="application/pdf"
            )
        st.success("Portfolio PDF generated successfully!")

def show_proposal_page():
    st.header("Create Job Proposal")
    
    # Client Information
    st.subheader("Client Information")
    col1, col2 = st.columns(2)
    
    with col1:
        client_name = st.text_input("Client Name")
        company = st.text_input("Company Name")
        email = st.text_input("Client Email")
    
    with col2:
        project_title = st.text_input("Project Title")
        budget = st.text_input("Project Budget")
        timeline = st.text_input("Project Timeline")
    
    project_description = st.text_area("Project Description")
    
    # Custom Sections
    st.subheader("Custom Sections")
    section_title = st.text_input("Section Title")
    section_content = st.text_area("Section Content")
    
    if st.button("Add Section"):
        if 'proposal' not in st.session_state:
            st.session_state.proposal = Proposal(st.session_state.portfolio)
        st.session_state.proposal.add_section(section_title, section_content)
        st.success(f"Added section: {section_title}")
    
    # Generate Proposal
    if st.button("Generate Proposal"):
        if 'proposal' not in st.session_state:
            st.session_state.proposal = Proposal(st.session_state.portfolio)
        
        st.session_state.proposal.set_client_info(
            client_name, company, email, project_title,
            project_description, budget, timeline
        )
        
        # Generate both formats
        docx_filename = "proposal.docx"
        pdf_filename = "proposal.pdf"
        
        st.session_state.proposal.generate_docx(docx_filename)
        st.session_state.proposal.generate_pdf(pdf_filename)
        
        st.success("Proposal generated successfully!")
        
        # Provide download buttons
        with open(docx_filename, "rb") as docx_file:
            st.download_button(
                label="Download DOCX",
                data=docx_file,
                file_name=docx_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        
        with open(pdf_filename, "rb") as pdf_file:
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name=pdf_filename,
                mime="application/pdf"
            )

if __name__ == "__main__":
    main() 