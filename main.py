from pico2d import *
from boy import Boy
from grass import Grass
import game_world

# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global boy

    # grass = Grass()
    # game_world.add_object(grass)    # 게임 월드에 객체 추가

    # 사이에 낄 소년과 공
    boy = Boy()
    game_world.add_object(boy, 1)  # 게임 월드에 객체 추가

    # 가장 뒤에 올 잔디
    grass1 = Grass()
    game_world.add_object(grass1, 2)    # 게임 월드에 객체 추가

    # 가장 앞에 올 잔디
    grass2 = Grass(80)
    game_world.add_object(grass2, 0)  # 게임 월드에 객체 추가


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
