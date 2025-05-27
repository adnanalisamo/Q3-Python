class Portfolio:
    def __init__(self):
        self.personal_info = {
            'name': '',
            'title': '',
            'email': '',
            'phone': '',
            'location': '',
            'website': ''
        }
        self.skills = []
        self.experience = []
        self.education = []
        self.projects = []

    def set_personal_info(self, name, title, email, phone, location, website=''):
        """Set personal information for the portfolio"""
        self.personal_info = {
            'name': name,
            'title': title,
            'email': email,
            'phone': phone,
            'location': location,
            'website': website
        }

    def add_skill(self, skill, level):
        """Add a skill with proficiency level"""
        self.skills.append({
            'name': skill,
            'level': level
        })

    def add_experience(self, company, position, duration, description):
        """Add work experience"""
        self.experience.append({
            'company': company,
            'position': position,
            'duration': duration,
            'description': description
        })

    def add_education(self, institution, degree, year, description=''):
        """Add educational background"""
        self.education.append({
            'institution': institution,
            'degree': degree,
            'year': year,
            'description': description
        })

    def add_project(self, name, description, technologies, link=''):
        """Add a project to the portfolio"""
        self.projects.append({
            'name': name,
            'description': description,
            'technologies': technologies,
            'link': link
        })

    def get_portfolio_summary(self):
        """Get a summary of the portfolio"""
        return {
            'personal_info': self.personal_info,
            'skills': self.skills,
            'experience': self.experience,
            'education': self.education,
            'projects': self.projects
        } 