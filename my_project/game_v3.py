import numpy as np


def game_core_v3(number) -> int:
    # number = np.random.randint(1, 101)  # компьютер загадывает число
    # print("num:", number)
    pr_min = 1
    pr_max = 101
    # количество попыток
    count = 1
    predict_number = np.random.randint(1, 101)  # компьюьер предсеазывает число

    while number != predict_number:
       
        if (pr_max - pr_min) < 2:
            break 
        count += 1
       

        if predict_number > number:  # если предсказанное число больше загаданного
            pr_max = predict_number
            predict_number = round((pr_min + pr_max) / 2)
        
        else:
            # если предсказанное число меньше загаданного
            pr_min = predict_number
            predict_number = round((pr_min + pr_max) / 2)
   
    return count

def score_game(game_core_v3) -> int:

    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел
   
    for number in random_array:
        count_ls.append(game_core_v3(number))
        score = int(np.mean(count_ls))
   
    return score


score_game(game_core_v3)