from django.test import TestCase
from django.contrib.auth.models import User
from reviews.models import Genre, Category, Review

class ReviewModelTest(TestCase):
    def setUp(self):
        # Create a category
        self.category = Category.objects.create(name='Books')

        # Create a genre linked to the category
        self.genre = Genre.objects.create(name='Drama', category=self.category)

        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_create_valid_review(self):
        # Create a valid review
        review = Review.objects.create(
            title="Amazing Book",
            author_director="Jane Austen",
            genre=self.genre,
            rating=5,
            content="This is a wonderful book, highly recommended!",
            user=self.user
        )

        # Check if the review was saved correctly
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.title, "Amazing Book")
        self.assertEqual(review.author_director, "Jane Austen")
        self.assertEqual(review.genre, self.genre)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.user, self.user)

    def test_review_relationship_with_user(self):
        # Test if the relationship with the user works correctly
        review = Review.objects.create(
            title="Great Drama",
            author_director="John Director",
            genre=self.genre,
            rating=4,
            content="An engaging and emotional story.",
            user=self.user
        )
        self.assertEqual(self.user.reviews.count(), 1)
        self.assertEqual(self.user.reviews.first(), review)

    def test_review_str_method(self):
        # Test the __str__ method
        review = Review.objects.create(
            title="String Representation",
            author_director="Author Name",
            genre=self.genre,
            rating=5,
            content="A detailed and interesting review.",
            user=self.user
        )
        self.assertEqual(str(review), "String Representation")

