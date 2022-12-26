import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from players.models import Player


class PlayerTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Player.objects.create(name="Julio", last_name="Orellano", team="equipo1", number=11, position="atacante", owner=self.test_user)
        Player.objects.create(name="Mario", last_name="Reggiardo", team="equipo2", number=11, position="atacante", owner=self.test_user)

        player_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(player_test_num)
        ]
        self.mock_last_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(player_test_num)
        ]
        self.mock_teams = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(player_test_num)
        ]
        self.mock_numbers = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(player_test_num)
        ]
        self.mock_positions = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(player_test_num)
        ]

        for mock_name, mock_last_name, mock_team, mock_number, mock_position in zip(self.mock_names, self.mock_last_names, self.mock_teams, self.mock_numbers, self.mock_positions):
            Player.objects.create(name=mock_name, last_name=mock_last_name, team=mock_team, number=mock_number, position=mock_position, owner=self.test_user)

    def test_player_model(self):
        """Players creation are correctly identified"""
        python_player = Player.objects.get(name="Julio")
        docker_player = Player.objects.get(name="Mario")
        self.assertEqual(python_player.owner.username, "testuser")
        self.assertEqual(docker_player.owner.username, "testuser")
        self.assertEqual(python_player.last_name, "Orellano")
        self.assertEqual(docker_player.last_name, "Reggiardo")

    def test_player_list(self):
        for mock_name, mock_last_name, mock_team, mock_number, mock_position in zip(self.mock_names, self.mock_last_names, self.mock_teams, self.mock_numbers, self.mock_positions):
            player_test = Player.objects.get(name=mock_name)
            self.assertEqual(player_test.owner.username, "testuser")
            self.assertEqual(player_test.last_name, mock_last_name)
            self.assertEqual(player_test.team, mock_team)
            self.assertEqual(player_test.number, mock_number)
            self.assertEqual(player_test.position, mock_position)