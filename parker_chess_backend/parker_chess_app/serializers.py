from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'username', 'password', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'profile_name', 'bio', 'profile_picture', 'date_time_played')

class GameSerializer(serializers.ModelSerializer):
    white_player = UserSerializer(read_only=True)
    black_player = UserSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'white_player', 'black_player', 'white_player_elo', 'black_player_elo', 'game_winner', 'game_color_winner', 'date_time_played')

class MoveSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    mover = UserSerializer(read_only=True)

    class Meta:
        model = Move
        fields = ('game', 'move_id', 'move', 'mover', 'piece', 'fen_string', 'date_time_move_played')

class FollowingSerializer(serializers.ModelSerializer):
    main_account = UserSerializer(read_only=True)
    account_following = UserSerializer(read_only=True)

    class Meta:
        model = Following
        fields = ('main_account', 'account_following', 'date_time')

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Notification
        fields = ('user', 'message', 'timestamp', 'urgency', 'read')