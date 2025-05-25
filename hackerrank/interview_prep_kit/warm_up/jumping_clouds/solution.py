# This is cool recursion/backtracking problem
# see: https://www.hackerrank.com/challenges/jumping-on-the-clouds

# 0 - safe cloud, 1 - not safe cloud
# we can only jump to the next or After next
# there's always a solution

def is_safe(cloud: int) -> bool:
    return cloud == 0

def jumpingOnClouds(clouds):
    current_cloud_index = 0
    jumps = 0

    while current_cloud_index < len(clouds):
        # try to jump two clouds
        if current_cloud_index + 2 < len(clouds) and is_safe(clouds[current_cloud_index + 2]):
           current_cloud_index += 2
        else:
            current_cloud_index += 1
        jumps += 1

    return jumps