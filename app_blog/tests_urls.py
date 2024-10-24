from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from .views import HomePageView, ArticleList, ArticleDetail, ArticleCategoryList
from .models import Article, Category

class HomeTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            category='Test Category',
            slug='test-category'
        )

        self.article = Article.objects.create(
            title='Test Article',
            description='This is a test article for unit testing.',
            pub_date=timezone.now(),
            slug='test-article',
            main_page=False,
            category=self.category
        )

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('test-category',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_url_resolves_category_view(self):
        view = resolve('/articles/category/test-category/')
        self.assertEqual(view.func.view_class, ArticleCategoryList)

    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url_resolves_articles_list_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class, ArticleList)

    def test_article_detail_view_status_code(self):
        url = reverse('news-detail', args=[
            self.article.pub_date.year,
            self.article.pub_date.month,
            self.article.pub_date.day,
            self.article.slug
        ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url_resolves_article_detail_view(self):
        view = resolve(
            f'/articles/{self.article.pub_date.year}/{self.article.pub_date.month}/{self.article.pub_date.day}/{self.article.slug}/')
        self.assertEqual(view.func.view_class, ArticleDetail)




