from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=25)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics',  blank=True, null=True)
    date_time_played = models.DateTimeField(auto_now_add=True)
    elo = models.IntegerField(default=1000)

class Game(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    white_player = models.ForeignKey(User, related_name='white', on_delete=models.SET_NULL, null=True)
    black_player = models.ForeignKey(User, related_name='black', on_delete=models.SET_NULL, null=True)
    white_player_elo = models.IntegerField(default=None)
    black_player_elo = models.IntegerField(default=None)
    game_winner = models.ForeignKey(User, related_name='wins', on_delete=models.SET_NULL, null=True, blank=True)
    game_color_winner = models.TextField()
    date_time_played = models.DateTimeField(auto_now_add=True)

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    move_id = models.IntegerField()
    move = models.CharField(max_length=6) # formatted like 'A1A2' or 'A1O-O-O' or 'A7A8=Q'
    mover = models.ForeignKey(User, related_name='white_games', on_delete=models.SET_NULL, null=True)
    piece = models.CharField(max_length=1)
    fen_string = models.CharField(max_length=90)
    date_time_move_played = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('game', 'move_id')

class Following(models.Model):
    main_account = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    account_following = models.ForeignKey(User, related_name='followee', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('main_account', 'account_following')

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    sub_message = models.TextField()
    sub_message_link = models.TextField()
    notification_type = models.TextField()
    read = models.BooleanField(default=False)