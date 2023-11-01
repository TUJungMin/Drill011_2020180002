from pico2d import *
import game_framework
objects = [[], [], []]
import game_world
from grass import Grass
from bird import Bird

# bird = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            birds.handle_event(event)

def init():
    global grass
    global birds  # birds 리스트를 추가

    grass = Grass()
    game_world.add_object(grass, 0)

    birds = []  # 새 객체들을 저장할 리스트

    for i in range(10):  # 10마리의 새 객체 생성
        bird = Bird()
        birds.append(bird)  # 리스트에 추가

    game_world.add_objects(birds, 1)  # bird 리스트를 game_world에 추가



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    #delay(0.1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

