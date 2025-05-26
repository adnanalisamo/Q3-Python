

from portfolio import Portfolio
from proposal import Proposal

def create_portfolio():
    """Create a new portfolio"""
    portfolio = Portfolio()
    
    print("\n=== Create Your Portfolio ===")
    
    # Get personal information
    print("\nPersonal Information:")
    name = input("Enter your name: ")
    title = input("Enter your professional title: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    location = input("Enter your location: ")
    website = input("Enter your website (optional): ")
    
    portfolio.set_personal_info(name, title, email, phone, location, website)
    
    # Add skills
    print("\nAdd Skills (enter 'done' when finished):")
    while True:
        skill = input("Enter skill name (or 'done' to finish): ")
        if skill.lower() == 'done':
            break
        level = input("Enter proficiency level (Beginner/Intermediate/Expert): ")
        portfolio.add_skill(skill, level)
    
    # Add experience
    print("\nAdd Work Experience (enter 'done' when finished):")
    while True:
        company = input("Enter company name (or 'done' to finish): ")
        if company.lower() == 'done':
            break
        position = input("Enter position: ")
        duration = input("Enter duration (e.g., '2020-2022'): ")
        description = input("Enter job description: ")
        portfolio.add_experience(company, position, duration, description)
    
    return portfolio

def create_proposal(portfolio):
    """Create a new proposal"""
    proposal = Proposal(portfolio)
    
    print("\n=== Create Job Proposal ===")
    
    # Get client information
    print("\nClient Information:")
    client_name = input("Enter client name: ")
    company = input("Enter company name: ")
    email = input("Enter client email: ")
    project_title = input("Enter project title: ")
    project_description = input("Enter project description: ")
    budget = input("Enter project budget: ")
    timeline = input("Enter project timeline: ")
    
    proposal.set_client_info(client_name, company, email, project_title, 
                           project_description, budget, timeline)
    
    # Add custom sections
    print("\nAdd Custom Sections (enter 'done' when finished):")
    while True:
        title = input("Enter section title (or 'done' to finish): ")
        if title.lower() == 'done':
            break
        content = input("Enter section content: ")
        proposal.add_section(title, content)
    
    return proposal

def main():
    print("Welcome to Freelancer Portfolio & Job Proposal Generator!")
    
    # Create portfolio
    portfolio = create_portfolio()
    
    while True:
        print("\n=== Main Menu ===")
        print("1. Create new proposal")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '1':
            proposal = create_proposal(portfolio)
            
            # Generate proposal in both formats
            docx_filename = "proposal.docx"
            pdf_filename = "proposal.pdf"
            
            proposal.generate_docx(docx_filename)
            proposal.generate_pdf(pdf_filename)
            
            print(f"\nProposal generated successfully!")
            print(f"DOCX file: {docx_filename}")
            print(f"PDF file: {pdf_filename}")
            
        elif choice == '2':
            print("\nThank you for using Freelancer Portfolio & Job Proposal Generator!")
            break

        else:
            print("\nInvalid choice. Please try again.")
main()
