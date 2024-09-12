import turtle
import matplotlib.pyplot as plt

def display_counts(count, s, e, i, r, d):
    turtle.undo()  # undo previous count display
    turtle.penup()
    turtle.goto(-300, 300)
    turtle.pendown()
    turtle.color('black')
    turtle.write(f"Days: {count}    Susceptible: {s}   Exposed: {e}    Infected: {i}   Recovered: {r}  Dead: {d}",
                 font=("Arial", 16, "normal"))
    
def make_plot(s,e, i, r, d):
    x = range( len(s))
    plt.plot(x,  s, 'blue', label = 'Susceptible')
    plt.plot(x,  e, 'orange', label = 'Exposed')
    plt.plot(x,  i, 'red', label = 'Infected')
    plt.plot(x,  r, 'green', label = 'Recovered')
    plt.plot(x,  d, 'black', label = 'Dead')
    plt.legend()
    plt.savefig('F:/Projects/SIR_modeling/SIR.png', format="png",dpi=300, bbox_inches='tight')

def update_counter(agent, dict):
    match agent.state:
            case 'S':
                dict['s'] += 1
            case 'R':
                dict['r'] += 1 
            case 'D':
                dict['d'] += 1 
            case 'E':
                dict['e'] += 1
            case 'I': 
                dict['i'] += 1