from art import logo
from art import vs
from game_data import data
import random
print(logo)
# def compare():


def random_choose(data):
    element1 = random.randint(1, len(data))
    element2 = random.randint(1, len(data))
    return element1, element2


def compare_elements(data):
    compare_a = data[random_choose(data)[0]]
    compare_b = data[random_choose(data)[1]]
    print(f"Compare A {compare_a["name"]},a {compare_a["description"]},from {compare_a['country']}")
    print(vs)
    print(f"Compare B {compare_b["name"]},a {compare_b["description"]},from {compare_b['country']}")
    choose = input('Make your choose "A" or "B"')
    if compare_a['follower_count'] > compare_b['follower_count'] and choose == 'a':
        print('you win')
    elif compare_a['follower_count'] < compare_b['follower_count'] and choose == 'b':
        print('you win')
    elif compare_a['follower_count'] < compare_b['follower_count'] and choose == 'a':
        print('you lose')
    elif compare_a['follower_count'] > compare_b['follower_count'] and choose == 'b':
        print('you lose')

compare_elements(data)