import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from teams.models import Team
from federations.models import Federation
from datetime import datetime

class TeamTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        fedaration_test = Federation.objects.create(name="AFA", initials="AFA", official_website="AFA.com.ar", owner=self.test_user)
        fed_pk = Federation.objects.get(name="AFA").id
        Team.objects.create(name="River", federation=fed_pk, country="Argentina", city="Buenos Aires", fundation_date=datetime.now())
        Team.objects.create(name="Racing", federation=fed_pk, country="Argentina", city="Avellaneda", fundation_date=datetime.now())

        team_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(team_test_num)
        ]
        self.mock_federations = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(team_test_num)
        ]
        self.mock_countries = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(team_test_num)
        ]
        self.mock_cities = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(team_test_num)
        ]
        self.mock_fundation_dates = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(team_test_num)
        ]

        for mock_name, mock_federation, mock_country, mock_city, mock_fundation_date in zip(self.mock_names, self.mock_federations, self.mock_countries, self.mock_cities, self.mock_fundation_dates):
            Team.objects.create(name=mock_name, federation=mock_federation, country=mock_country, city=mock_city, fundation_date=mock_fundation_date, owner=self.test_user)

    def test_team_model(self):
        """Teams creation are correctly identified"""
        python_team = Team.objects.get(name="River")
        docker_team = Team.objects.get(name="Racing")
        self.assertEqual(python_team.federation.name, "AFA")
        self.assertEqual(docker_team.federation.name, "AFA")
        self.assertEqual(python_team.city, "Buenos Aires")
        self.assertEqual(docker_team.city, "Avellaneda")