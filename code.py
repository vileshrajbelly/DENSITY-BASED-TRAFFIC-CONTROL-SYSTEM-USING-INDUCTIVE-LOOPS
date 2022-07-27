import digitalio
import board
import time
"""pins for the inductive loops """
il_p_n = board.GP15
il_p_s = board.GP14
il_p_e = board.GP13
il_p_w = board.GP12
"""pins for the red lights """
SL_north_red = board.GP16
SL_south_red = board.GP17
SL_east_red = board.GP18
SL_west_red = board.GP19
"""pins for the green lights """
SL_north_green = board.GP7
SL_south_green = board.GP6
SL_east_green = board.GP5
SL_west_green = board.GP4
"""pins for the amber lights """
SL_north_amber = board.GP11
SL_south_amber = board.GP10
SL_east_amber = board.GP9
SL_west_amber = board.GP8

trans_t_constant = 1

north = south = east = west = False  # which direction is the car going
time_north = time_south = time_east = time_west = 0

ilp_n_t = ilp_s_t = ilp_e_t = ilp_w_t = 0
il_n_t = il_s_t = il_e_t = il_w_t = 0

next = 0

t_constant = 20

il_n_const = 2
il_s_const = 2
il_e_const = 2
il_w_const = 2

il_n = digitalio.DigitalInOut(il_p_n)
il_n.direction = digitalio.Direction.INPUT
il_n.pull = digitalio.Pull.UP

il_s = digitalio.DigitalInOut(il_p_s)
il_s.direction = digitalio.Direction.INPUT
il_s.pull = digitalio.Pull.UP

il_e = digitalio.DigitalInOut(il_p_e)
il_e.direction = digitalio.Direction.INPUT
il_e.pull = digitalio.Pull.UP

il_w = digitalio.DigitalInOut(il_p_w)
il_w.direction = digitalio.Direction.INPUT
il_w.pull = digitalio.Pull.UP

SL_north_red = digitalio.DigitalInOut(SL_north_red)
SL_north_red.direction = digitalio.Direction.OUTPUT

SL_south_red = digitalio.DigitalInOut(SL_south_red)
SL_south_red.direction = digitalio.Direction.OUTPUT

SL_east_red = digitalio.DigitalInOut(SL_east_red)
SL_east_red.direction = digitalio.Direction.OUTPUT

SL_west_red = digitalio.DigitalInOut(SL_west_red)
SL_west_red.direction = digitalio.Direction.OUTPUT


SL_north_green = digitalio.DigitalInOut(SL_north_green)
SL_north_green.direction = digitalio.Direction.OUTPUT

SL_south_green = digitalio.DigitalInOut(SL_south_green)
SL_south_green.direction = digitalio.Direction.OUTPUT

SL_east_green = digitalio.DigitalInOut(SL_east_green)
SL_east_green.direction = digitalio.Direction.OUTPUT

SL_west_green = digitalio.DigitalInOut(SL_west_green)
SL_west_green.direction = digitalio.Direction.OUTPUT


SL_north_amber = digitalio.DigitalInOut(SL_north_amber)
SL_north_amber.direction = digitalio.Direction.OUTPUT

SL_south_amber = digitalio.DigitalInOut(SL_south_amber)
SL_south_amber.direction = digitalio.Direction.OUTPUT

SL_east_amber = digitalio.DigitalInOut(SL_east_amber)
SL_east_amber.direction = digitalio.Direction.OUTPUT

SL_west_amber = digitalio.DigitalInOut(SL_west_amber)
SL_west_amber.direction = digitalio.Direction.OUTPUT


SL_north_red.value = SL_south_red.value = SL_east_red.value = SL_west_red.value = False
SL_north_green.value = SL_south_green.value = SL_east_green.value = SL_west_green.value = True
SL_north_amber.value = SL_south_amber.value = SL_east_amber.value = SL_west_amber.value = False
time.sleep(1)

SL_north_red.value = SL_south_red.value = SL_east_red.value = SL_west_red.value = False
SL_north_green.value = SL_south_green.value = SL_east_green.value = SL_west_green.value = False
SL_north_amber.value = SL_south_amber.value = SL_east_amber.value = SL_west_amber.value = True
time.sleep(1)

SL_north_red.value = SL_south_red.value = SL_east_red.value = SL_west_red.value = True
SL_north_green.value = SL_south_green.value = SL_east_green.value = SL_west_green.value = False
SL_north_amber.value = SL_south_amber.value = SL_east_amber.value = SL_west_amber.value = False
time.sleep(1)


def north_stop_light():
    global SL_north_red, SL_north_amber, SL_north_green, north, ilp_n_t
    if(north == False):  # red to green
        SL_north_red.value = False
        SL_north_amber.value = True
        time.sleep(1)
        SL_north_green.value = True
        SL_north_amber.value = False
        ilp_n_t = time.time()
        north = True
    elif(north == True):  # green to red
        SL_north_green.value = False
        SL_north_amber.value = True
        time.sleep(1)
        SL_north_red.value = True
        SL_north_amber.value = False
        north = False


def south_stop_light():
    global SL_south_red, SL_south_amber, SL_south_green, south, ilp_s_t
    if(south == False):  # red to green
        SL_south_red.value = False
        SL_south_amber.value = True
        time.sleep(1)
        SL_south_green.value = True
        SL_south_amber.value = False
        ilp_s_t = time.time()
        south = True
    elif(south == True):  # green to red
        SL_south_green.value = False
        SL_south_amber.value = True
        time.sleep(1)
        SL_south_red.value = True
        SL_south_amber.value = False
        south = False


def east_stop_light():
    global SL_east_red, SL_east_amber, SL_east_green, east, ilp_e_t
    if(east == False):  # red to green
        SL_east_red.value = False
        SL_east_amber.value = True
        time.sleep(1)
        SL_east_green.value = True
        SL_east_amber.value = False
        ilp_e_t = time.time()
        east = True
    elif(east == True):  # green to red
        SL_east_green.value = False
        SL_east_amber.value = True
        time.sleep(1)
        SL_east_red.value = True
        SL_east_amber.value = False
        east = False


def west_stop_light():
    global SL_west_red, SL_west_amber, SL_west_green, west, ilp_w_t
    if(west == False):  # red to green
        SL_west_red.value = False
        SL_west_amber.value = True
        time.sleep(1)
        SL_west_green.value = True
        SL_west_amber.value = False
        ilp_w_t = time.time()
        west = True
    elif(west == True):  # green to red
        SL_west_green.value = False
        SL_west_amber.value = True
        time.sleep(1)
        SL_west_red.value = True
        SL_west_amber.value = False
        west == False


north_stop_light()
init_time = time.time()
##################################################################################
while True:
    current_time = time.time()-init_time
    if(current_time > t_constant):
        next += 1
        if(next > 4):
            next = 0

        init_time = time.time()

    time.sleep(0.1)
    print(current_time)
    print("next", next)

    if(il_n.value == False and north == True):
        il_n_t = time.time()-ilp_n_t
        if(il_n_t > il_n_const):
            next += 1
    else:
        ilp_n_t = time.time()

    if(il_s.value == False and south == True):
        il_s_t = time.time()-ilp_s_t
        if(il_s_t > il_s_const):
            next += 1
    else:
        ilp_s_t = time.time()

    if(il_e.value == False and east == True):
        il_e_t = time.time()-ilp_e_t
        if(il_e_t > il_e_const):
            next += 1
    else:
        ilp_e_t = time.time()

    if(il_w.value == False and west == True):
        il_w_t = time.time()-ilp_w_t
        if(il_w_t > il_w_const):
            next += 1
    else:
        ilp_w_t = time.time()

    if(next == 0 and north == False):
        north_stop_light()

    elif(next == 1 and north == True):
        north_stop_light()  # north off
        time.sleep(trans_t_constant)
        south_stop_light()  # south on

    elif(next == 2 and south == True):
        south_stop_light()  # south off
        time.sleep(trans_t_constant)
        east_stop_light()  # east on

    elif(next == 3 and east == True):
        east_stop_light()  # east off
        time.sleep(trans_t_constant)
        west_stop_light()  # west on

    elif(next == 4 and west == True):
        west_stop_light()  # west off
        time.sleep(trans_t_constant)
        north_stop_light()  # north on