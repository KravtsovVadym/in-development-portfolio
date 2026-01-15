from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
class SkillIcon(models.Model):
    name = models.CharField('Icon name', max_length=50)

    icon = models.ImageField(
        'Skill Icon',
        upload_to='skills_icon/',
        null=True,
        blank=True
    )

    link = models.URLField(
        'Skill Link',
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Skill Icon: {self.name}'   


    def clean(self):
        if not self.icon and not link:
            raise ValidationErron({'icon': 'install the icon or link below'})


class Skill(models.Model):
    name = models.CharField('Skills', max_length=50)

    level = models.PositiveSmallIntegerField(
        default=0,
        validators=[
        MinValueValidator(0, message='the level connot be less than zero'),
        MaxValueValidator(100, message='the level connot be more than one hundred')
    ])

    icon = models.OneToOneField(
        SkillIcon,
        on_delete=models.SET_NULL,
        related_name='skills',
        null=True,
        blank=True
    )


    def __str__(self):
        return f'Skill: {self.name}'



class Profile(models.Model):
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    about = models.TextField('About')

    aboutFooter = models.TextField(
        'AboutFooter',
        blank=True
        )
    
    aboutStart = models.TextField(
        'AboutStart',
        blank=True
    )

    learning_technologies = models.TextField(
        'learning_technologies',
        blank=True
    )

    skills = models.ManyToManyField(
        Skill,
        related_name='profiles'
    )


    image = models.ImageField(
        'Profile Image',
        upload_to='profile/'
        )


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


    def __str__(self):
        full_name = self.author.get_full_name()

        if full_name:
            return f'{self.author.username}: {full_name}'

        return self.author.username


class Project(models.Model):
    title = models.CharField(
        'Projects',
        max_length=50,
        unique=True
    )

    description = models.CharField(
        'Descriptions',
        max_length=255
    )

    image = models.ImageField(
        'Projects Images',
        upload_to='project/'
    )

    links = models.URLField(
        'Git Link',
        max_length=255
    )

    technologies = models.CharField(
        'Technogies',
        max_length=255
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
