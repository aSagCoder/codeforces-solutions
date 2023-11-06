def boy_or_girl(user_name):
    dist_chars = set(user_name)
    count_dist = len(dist_chars)
    
    if count_dist % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"
    
user_name = input().strip()

print(boy_or_girl(user_name))
