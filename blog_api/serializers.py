from rest_framework.serializers import ModelSerializer
from .models import Post, Comment, Like

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance): 
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(Comment.objects.filter(post=instance.pk), many=True).data
        representation['likes_count'] = instance.likes.count()
        return representation

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
