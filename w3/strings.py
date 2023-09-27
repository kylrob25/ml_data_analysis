import random
import matplotlib.pyplot as plt


def exercise_1():
    welcome = 'Welcome to Machine Learning for Data Analytics'
    words = welcome.split(' ')

    for word in words:
        if 'm' in word or "a" not in word or len(word) < 7:
            print(word)

    welcome_length = len(welcome)
    first = slice(0, welcome_length // 2)
    second = slice(welcome_length // 2, welcome_length)

    print(welcome[first])
    print(welcome[second])


def exercise_2():
    term1 = ['Advisory', 'Asset', 'Baselining', 'Block List', 'Clearance', 'Collision', 'Competency', 'Event',
             'Failover', 'Impact']
    term2 = ['Manual Key Transport', 'Message Digest', 'Outside Threat', 'Passive Attack', 'Perimeter', 'Privilege',
             'Protocol', 'Resilience', 'Sanitization', 'Tunneling']
    term3 = ['Validation', 'Whitelist', 'Zeroisation', 'Threat', 'Standard', 'Speacialism', 'Rootkit', 'Risk',
             'Regulation', 'Proxy']
    phrase = ''

    phrase += term1[random.randint(0, len(term1))]
    phrase += " "
    phrase += term2[random.randint(0, len(term2))]
    phrase += " "
    phrase += term3[random.randint(0, len(term3))]

    print(phrase)


def exercise_3():
    x = list(range(1, 10))

    y = comprehension(x)

    plt.plot(x, y, label='y = 2x+3')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot (y = 2x + 3)')
    plt.legend()

    plt.show()


def generate(x):
    y = []
    for value in x:
        y.append(2 * value + 3)
    return y


def comprehension(x):
    y = [2 * value + 3 for value in x]
    return y

exercise_3()

