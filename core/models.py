from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Product model with ForeignKey relationship
class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)  # Linking to Category with ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ManyToMany- Author and Book
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')  # Many authors can be linked to many books

    def __str__(self):
        return self.title

# OneToOne- UserProfile for a user
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Linking to Django's built-in User model
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# comment model linked to Post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # One-to-Many relationship
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
    
    from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()







