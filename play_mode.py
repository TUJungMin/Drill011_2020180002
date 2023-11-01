from pico2d import *
import game_framework
import game_world
from grass import Grass
from bird import Bird

grass = None
birds = []  # birds 리스트를 추가

def init():
    global grass
    global birds

    grass = Grass()
    game_world.add_object(grass, 0)

    birds = []

    for i in range(10):
        bird = Bird()
        birds.append(bird)

    game_world.add_objects(birds, 1)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            for bird in birds:
                bird.handle_event(event)

def finish():
    game_world.clear()

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass