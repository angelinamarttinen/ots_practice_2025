import turtle

def perform_switch_case(state, t, step_count):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    
    if state == "INIT":
        state = "LEFT"
        t.setheading(180)  # Направление влево
        return state, step_count
        
    elif state == "LEFT":
        t.forward(10)  # Перемещение
        step_count += 1
        
        if step_count >= 5:  # Пройти 5 шагов влево
            state = "DOWN"
            t.setheading(270)  # Разворот вниз
            step_count = 0
        return state, step_count
        
    elif state == "DOWN":
        t.forward(10)  # Перемещение
        step_count += 1
        
        if step_count >= 1:  # Пройти 1 шаг вниз
            # Определяем следующее направление на основе текущей позиции
            if t.heading() == 270:  # Если двигались вниз
                if x < 0:  # Если находимся слева
                    state = "RIGHT"
                    t.setheading(0)  # Разворот вправо
                else:  # Если находимся справа
                    state = "LEFT"
                    t.setheading(180)  # Разворот влево
            step_count = 0
        return state, step_count
        
    elif state == "RIGHT":
        t.forward(10)  # Перемещение
        step_count += 1
        
        if step_count >= 5:  # Пройти 5 шагов вправо
            state = "DOWN"
            t.setheading(270)  # Разворот вниз
            step_count = 0
        return state, step_count
        
    elif state == "STOP":
        return state, step_count
        
    return state, step_count

def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(3)
    step_count = 0
    
    # Выполняем зигзаг: влево, вниз, вправо, вниз, влево, вниз, вправо, вниз, влево
    pattern = ["LEFT", "DOWN", "RIGHT", "DOWN", "LEFT", "DOWN", "RIGHT", "DOWN", "LEFT"]
    pattern_index = 0
    
    while pattern_index < len(pattern):
        if curr_state == pattern[pattern_index]:
            pattern_index += 1
            if pattern_index >= len(pattern):
                curr_state = "STOP"
                break
        
        curr_state, step_count = perform_switch_case(curr_state, t, step_count)
    
    turtle.done()

if __name__ == "__main__":
    draw()
