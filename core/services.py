from core.models import Post  
import csv  

class PostFetcher:
    def fetch_posts(self):
        return Post.objects.all()

class CSVExporter:
    def export_posts_to_csv(self, posts):
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Title', 'Content'])
            for post in posts:
                writer.writerow([post.id, post.title, post.content])
