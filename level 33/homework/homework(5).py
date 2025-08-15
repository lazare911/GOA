def delete_nth(order,max_e):
    answer = []
    for i in order:
        if answer.count(i) < max_e:
            answer.append(i)   
    return answer