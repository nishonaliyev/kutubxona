from rest_framework import serializers

from .models import CustomUser, Comment, Book, Like


class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Book
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'book']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

        def create(self, validated_data):
            custom_user = CustomUser.objects.create(**validated_data)
            custom_user.set_password(validated_data['password'])
            custom_user.save()

            return custom_user


