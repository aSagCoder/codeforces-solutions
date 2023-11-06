def min_horseshoes(colors):
    unique_colors = set(colors)  
    return 4 - len(unique_colors)  

colors = list(map(int, input().split()))

result = min_horseshoes(colors)
print(result)
