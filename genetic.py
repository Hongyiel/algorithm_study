# find random password
import random
import string

password = "brad1234"
min_len = 2
max_len = 10

def generate_word(length):
    result = ''
    x = ''.join(random.sample(string.ascii_letters + string.digits, k=length))
    return x

def generate_population(size, min_len, max_len):
    population = []
    for i in range(size):
        length = i % (max_len - min_len + 1) + min_len
        population.append(generate_word(length))
    return population

def fitness(password, test_word):
    score = 0
    
    if len(password) != len(test_word):
        return score

    score_len = 0.5
    score += score_len
    
    for i in range(len(password)):
        if password[i] == test_word[i]:
            score +=1
    
    return score / (len(password) + score_len) * 100

def compute_performance(population, password):
    performance_list = []
    for individual in population:
        score = fitness(password, individual)
    


print(generate_word(length=10))
pop  = generate_population(size=100,min_len=min_len,max_len=max_len)
print(pop)

