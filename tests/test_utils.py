# This is part of Requiem
# Copyright (C) 2020  God Empress Verin

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pwpy import utils


def test_score_range():
    min_att, max_att = utils.score_range(1000)
    assert min_att == 750.0
    assert max_att == 1750.0
    min_att, max_att = utils.score_range(5000)
    assert min_att == 3750.0
    assert max_att == 8750.0


def test_infra_cost():
    cost = utils.infra_cost(1000, 1500)
    assert cost == 4337302.0
    cost = utils.infra_cost(2000, 3000)
    assert cost == 40932054.0


def test_land_cost():
    cost = utils.land_cost(1000, 1500)
    assert cost == 985400.0
    cost = utils.land_cost(2000, 3000)
    assert cost == 10120800.0


def test_city_cost():
    cost = utils.city_cost(15)
    assert cost == 112025000.0
    cost = utils.city_cost(30)
    assert cost == 1102025000.0


def test_sort_ongoing_wars():
    wars = [
        {"turnsleft": 14, "winner": 0},
        {"turnsleft": 20, "winner": 0},
        {"turnsleft": 0, "winner": 100},
        {"turnsleft": 3, "winner": 0},
        {"turnsleft": 0, "winner": 0}
    ]
    correct = [
        {"turnsleft": 14, "winner": 0},
        {"turnsleft": 20, "winner": 0},
        {"turnsleft": 3, "winner": 0}
    ]
    actual = utils.sort_ongoing_wars(wars)
    assert correct == actual
