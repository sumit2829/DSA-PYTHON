def canShip(weights, capacity, days):
    day = 1
    load = 0

    for weight in weights:
        if load + weight <= capacity:
            load += weight
        else:
            day += 1
            load = weight

    return day <= days


def shipWithinDays(weights, days):
    start = max(weights)
    end = sum(weights)

    while start <= end:
        mid = start + (end - start) // 2

        if canShip(weights, mid, days):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(shipWithinDays(weights, days))