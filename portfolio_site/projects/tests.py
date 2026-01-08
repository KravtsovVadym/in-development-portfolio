from django.test import TestCase
from projects.models import Projects
# Create your tests here.

class ProjectsTest(TestCase):
    
    def test_portfolio_creation_and_deletion(self):
        portfolio = Projects.objects.create(
            title = "TODO menager",
            description = "CRUD operations",
            image = "static/images/your_image.jpg",
            technologies = "Django, HTML, CSS",
            links = "https://github.com/KravtsovVadym/tasks_course"
        )

        self.assertIsNotNone(portfolio)

        portfolio.delete()

        self.assertFalse(Projects.objects.filter(id=portfolio.id).exists())

        
