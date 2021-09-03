from board import board
from matplotlib import pyplot as plt
import operator
import time


def populate_generation(initial_board, population_size, number_of_generations,elitism, crosover, mutation):
#convert percentages to numbers
    start_time = time.time()
    elitism_num = (population_size*elitism)/100
    crosover_num = (population_size*crosover)/100
    mutation_num = (population_size*mutation)/100
    snapshots = []
#population is a list of boards
    generation_elites = [] #best (lowest cost) of every generation
    population = []
    initial_board.initialize()
    initial_board.hireistic_flag = True
    print("initial cost: ",initial_board.cost)
    population.append(initial_board)
    for i in range (2,population_size+1):
        population.append(initial_board.create_new_board(i))
        #built in sorting func
    population.sort(key=operator.attrgetter('cost'))
    generation_elites.append([1,(population[0].cost)]) #add first elite
    snapshots.append([population[0].cost,time.time()])
    #print(generation_elites)
#next generation
    for i in range(1,number_of_generations):
        population = pass_generation(population,elitism_num,crosover_num,mutation_num)
        population.sort(key=operator.attrgetter('cost'))
        generation_elites.append([i+1,(population[0].cost)])
        if (time.time()-snapshots[-1][1]) > 0.25:
            snapshots.append([population[0].cost,time.time()])

    for i in population:
        print(i.cost)



    print("--- %s seconds ---" % (time.time() - start_time))
    ploting_over_generations(generation_elites,population_size,number_of_generations,elitism, crosover, mutation, snapshots)


def pass_generation(population, elitism_num, crosover_num, mutation_num):
    new_population = []
#passing the elitism number of boards to next gen
    for i in range(0,elitism_num):
        new_population.append(population.pop(0))
#passing the culling number of boards to next gen
    for i in range(0,crosover_num,2):
        A = population.pop(0)
        B = population.pop(0)
        A.merge_boards(B)
        B.merge_boards(A)
        new_population.append(A)
        new_population.append(B)
#passing the mutation number of boards to next gen
    for i in range(0,mutation_num):
        board = population.pop(0)
        board.move_a_random_queen()
        new_population.append(board)

    return new_population

def ploting_over_generations(generation_elites,population_size,number_of_generations,elitism, crosover, mutation,snapshots):

    ps = population_size
    nog = number_of_generations
    e = elitism
    c = crosover
    m = mutation

    #end
    Xs = []
    Ys = []

    # for gen in generation_elites:
    #     Xs.append(gen[0])
    #     Ys.append(gen[1])

    for snap in snapshots:
        Xs.append(snap[1])
        Ys.append(snap[0])

    plt.figure()
    plt.ylabel('Best Score (performance)')
    plt.xlabel('Time (seconds)')
    plt.plot(Xs, Ys)
    # plt.yscale('log', basey=(math.exp(1)))
    # plt.legend(ps,nog,e,c,m)
    plt.title("Genetic Algorithm")
    plt.show()
