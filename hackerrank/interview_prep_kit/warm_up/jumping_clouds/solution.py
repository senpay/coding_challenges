# This is cool intro to greedy problems
# see: https://www.hackerrank.com/challenges/jumping-on-the-clouds

# 0 - safe cloud, 1 - not safe cloud
# we can only jump to the next or After next
# there's always a solution

def is_safe(cloud: int) -> bool:
    return cloud == 0

def jumpingOnClouds(clouds):
    current_cloud_index = 0
    jumps = 0

    # use len(clouds) - 1 because we don't need to evaluate the last one
    while current_cloud_index < len(clouds) - 1:
        # try to jump two clouds
        if current_cloud_index + 1 >= len(clouds) or current_cloud_index + 2 >= len(clouds):
            # reached end of the cloud list
            current_cloud_index += 1
        elif is_safe(clouds[current_cloud_index + 2]):
            current_cloud_index += 2
        else:
            current_cloud_index += 1
        jumps += 1

    return jumps