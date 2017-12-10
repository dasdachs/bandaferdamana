from django.db import models
from django.utils import timezone

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from taggit.managers import TaggableManager


class Home(Page):
    """The main or home page"""
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('cover'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(Home, self).get_context(request)
        # Get the three
        try:
            exposed_pages = Post.objects.filter(exposed=True).order_by('-created')[:3]
        except IndexError:
            exposed_pages = []
        try:
            next_show = Show.objects.order_by('-date')[0]
        except IndexError:
            next_show = ""

        context['exposed_pages'] = exposed_pages
        context['next_show'] = next_show
        return context


class PostIndex(Page):
    """The blog index loop."""
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(PostIndex, self).get_context(request)
        context['posts'] = Post.objects.child_of(self).live().order_by('-created')
        return context


class Post(Page):
    """Posts and blog entries."""
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary = models.TextField(verbose_name="Povzetek", help_text="Prvi odstavek in povzetek")
    body = RichTextField(verbose_name="Besedilo")
    tags = TaggableManager()
    exposed = models.BooleanField(
        default=False,
        verbose_name='Vidno na prvi strani',
        help_text='Should the post be shown on the front page'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover'),
        FieldPanel('summary'),
        FieldPanel('body', classname='full'),
    ]
    
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, 'Common page configuration'),
        FieldPanel('exposed', 'Post will be shown on the front page')
    ]


class Member(Page):
    """Group members."""
    name = models.CharField(max_length=30)
    picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bio = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('bio', classname="full"),
        ImageChooserPanel('picture'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]


# TODO: will be replaced in the future
class Show(Page):
    """A model for posting Shows."""
    posted = models.DateField(auto_now=True)
    date = models.DateTimeField()
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField()
    location = models.CharField(max_length=50)
    location_url = models.URLField(max_length=100)
    tags = TaggableManager()

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('cover'),
        FieldPanel('location'),
        FieldPanel('location_url'),
        FieldPanel('body', classname='full'),
    ]
    
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]


class ShowIndex(Page):
    def get_context(self, request):
        context = super(ShowIndex, self).get_context(request)
        context['shows'] = Show.objects.child_of(self).live().filter(date__gte=timezone.now()).order_by('-date')
        return context
