from flask import Flask, render_template, request
from time import sleep

from sense_hat import SenseHat
import threading


red = (100, 0, 0)

g = (100, 80, 50)
w = (0, 0, 0)
b = (0, 100, 100)

room =[
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

heart =[
w,w,g,w,w,g,w,w,
w,g,g,g,g,g,g,w,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
w,g,g,g,g,g,g,w,
w,w,g,g,g,g,w,w,
w,w,w,g,g,w,w,w,
w,w,w,g,g,w,w,w
]


x = y = 4
hat = SenseHat()

def update_screen():
    global x, y

    hat.clear()
    hat.set_pixels(heart)
    hat.set_pixel(x, y, 255, 255, 255)

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_dot(event):
    global x, y
    if event.action in ('pressed', 'held'):
        x = clamp(x + {'left': -1,'right': 1,}.get(event.direction, 0))
        
        
        y = clamp(y + {
            'up': -1,
            'down': 1,
            }.get(event.direction, 0))




app = Flask(__name__)

    
room ={'101': 0, '102': 1,'103': 2,'104': 3,'105': 4}
    
@app.route('/')
def hello_world():
    #return render_template('form.html')
    return 'Hello World!'


@app.route('/test')
def test():
    return render_template('form.html')

@app.route('/post', methods=['POST'])
def post():
    

    sleep(3)
    value_submit = request.form['submit']
    #value_drop_down = request.form['asfasfdas']
    
    room_101 = ['full___^^','empty','full___^^','empty','full___^^']

    number = room['101']
    
    if heart[number] == red:
        room_101[number] = 'full___^^__________'
    else:
        room_101[number] = 'empty____________'
        
    
    tdata ={
        'room_status':room_101[number]
        }
    sleep(1)
    
    
    return render_template('form.html', **tdata)


   
    
'''
def main__():
    app.run(debug=True, host='172.30.1.58')
'''


def hotel_people():
    global x, y, room
    update_screen()
    while True:
        for event in hat.stick.get_events():
            print('event~~', event)
            move_dot(event)
            update_screen()
            
            if event.direction == 'middle' and event.action == 'pressed':
                if heart[x + 8*y] == red:
                    heart[x + 8*y] = w
                else:
                    heart[x + 8*y] = red
     
                
            
        sleep(0.1)
        print('hotel~~~')


if __name__ == '__main__':
    th_hotel = threading.Thread(target = hotel_people)
    th_hotel.start()
    print('kkk~~~ ')
    app.run(debug=True, host='172.30.1.58', threaded =True)
    print('hi~~~ ')

    
    
#th_server = threading.Thread(target = main__)
#th_hotel = threading.Thread(target = hotel_people)

#th_hotel.start()
#th_server.start()


