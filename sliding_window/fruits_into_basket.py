def fruits_into_baskets(fruits):
    basket_1 = {}
    # Might not need counters
    counter_b1 = 0

    basket_2 = {}
    counter_b2 = 0

    max_fruits = float('-inf')

    left = 0
    for right in range(len(fruits)):
        right_fruit = fruits[right]

        if right_fruit in basket_1:
            basket_1[right_fruit] += 1
            counter_b1 += 1
        elif right_fruit in basket_2:
            basket_2[right_fruit] += 1
            counter_b2 += 1
        elif counter_b1 == 0:
            basket_1[right_fruit] = 1
            counter_b1 += 1
        elif counter_b2 == 0:
            basket_2[right_fruit] = 1
            counter_b2 += 1
        else:
            # Not in either basket, need to move left
            # Find room in either basket
            while left < right:
                left_fruit = fruits[left]
                if left_fruit in basket_1:
                    basket_1[left_fruit] -= 1
                    counter_b1 -= 1
                    if basket_1[left_fruit] == 0:
                        del basket_1[left_fruit]
                        basket_1[right_fruit] = 1
                        break
                elif left_fruit in basket_2:
                    basket_2[left_fruit] -= 1
                    counter_b2 -= 1
                    if basket_2[left_fruit] == 0:
                        del basket_2[left_fruit]
                        basket_2[left_fruit] = 1
                        break
                left += 1

        max_fruits = max(max_fruits, counter_b1 + counter_b2)

    print("basket_1", basket_1)
    print("basket_2", basket_2)
    return max_fruits

def solution_fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # Try to extend the range
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # Shrink sliding window with maximum of 2 fruits
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length

if __name__=="__main__":
   fruits = ['A', 'B', 'C', 'A', 'C'] 
   print(fruits_into_baskets(fruits))
   fruits_2=['A', 'B', 'C', 'B', 'B', 'C']
   print(fruits_into_baskets(fruits_2))