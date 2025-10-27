# game 내의 객체들의 생성과 소멸을 관리하는 모듈입니다.
# 각각 clear_canvas() 와 update_canvas() 는 main.py 에서 처리합니다.
# 이 game_world 모듈은 게임 내의 객체들을 추가, 업데이트, 렌더링 하는 기능을 제공합니다.
# pico2d 모듈과 직접적인 의존성은 없다!

# world[0] : 0 layer
# world[1] : 1 layer
# ...
world = [[], [], []]  # 게임 내의 모든 객체를 담는 리스트

# 게임 내 객체를 추가하는 함수
def add_object(o, depth = 0):
    world[depth].append(o)


# 게임 월드에 객체 리스트를 추가하는 함수
def add_objects(ol, depth = 0): # add_objects([ball1, ball2])
    world[depth].append(ol)


# 게임 월드의 객체를 제거하는 함수
def remove_object(o):
    # 객체가 없는데 제거하려고 하면 에러가 발생함
    for layer in world:
        if o in layer:  # o가 world 리스트에서 layer 리스트에 있을 때만 제거
            layer.remove(o)
            return

    # 에러 방지 장치
    raise Exception("주의! 월드에 존재하지 않는 객체를 삭제하려고 합니다.")


# 게임 월드의 모든 객체들을 업데이트 하는 함수
def update():
    for layer in world:
        for o in layer:
            o.update()


# 게임 월드의 모든 객체들을 그리는 함수
def render():
    for layer in world:
        for o in layer:
            o.draw()