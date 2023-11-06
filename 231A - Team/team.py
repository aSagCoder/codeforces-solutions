def count_problems(n, problems):
    implemented_count = 0 
    
    for problem in problems:
        sure_count = sum(problem)
        
        if sure_count >= 2:
            implemented_count += 1
            
    return implemented_count

n = int(input())
problems = [list(map(int, input().split())) for _ in range(n)]

result = count_problems(n, problems)
print(result)
