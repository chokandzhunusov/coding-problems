"""
Breadth First:
    Time complexity: O(n^2)
    Space complexity: O(n)

Optimal 1:
    Time complexity: O(n)
    Space complexity: O(n)

Optimal 2:
    Time complexity: O(n)
    Space complexity: O(n) less space.
"""
    

def array_of_products_breadth_first(array: 'list[int]') -> 'list[int]':
    result = []
    
    for i in range(len(array)):
        product = 1
        for j in array[0:i]:
            product *= j
        
        for k in array[i+1:]:
            product *= k
        result.append(product)
    return result


def array_of_products_optimal_1(array: 'list[int]') -> 'list[int]':
    left_products = [1 for _ in array]
    right_products = [1 for _ in array]

    leftProduct = 1
    rightProduct = 1

    result = [1 for _ in array]

    for i in range(len(array)):
        left_products[i] = leftProduct
        leftProduct *= array[i]
    
    for j in reversed(range(len(array))):
        right_products[j] = rightProduct
        rightProduct *= array[j]

    for n in range(len(array)):
        result[n] = left_products[n] * right_products[n]
    
    return result
    

def array_of_products_optimal_2(array: 'list[int]') -> 'list[int]':
    products = [1 for _ in array]
    
    leftProduct = 1
    rightProduct = 1

    for i in range(len(array)):
        products[i] = leftProduct
        leftProduct *= array[i]
    
    for j in reversed(range(len(array))):
        products[j] *= rightProduct
        rightProduct *= array[j]
    
    return products


def main() -> None:
    ans = array_of_products_optimal_2([5, 1, 4, 2])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
