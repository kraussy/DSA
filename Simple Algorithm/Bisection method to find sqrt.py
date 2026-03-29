def square_root_bisection(number, tolerance = 0.01, max_iteration = 100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    elif number == 0 or number == 1:
        print (f"The square root of {number} is {number}" )
        return number

    else:
        low = 0
        high = max(1, number)
        
        
        iteration = 0
        while (high - low) >= tolerance:
            
            if iteration >= max_iteration:
                print (f"Failed to converge within {max_iteration} iterations")
                return None
            iteration += 1
            mid = (low + high) / 2
            if mid ** 2 < number:
                low = mid
            
            else:
                high = mid     
        
        mid = (low + high) / 2
        print(f"The square root of {number} is approximately {mid}")
        return mid
        
        
square_root_bisection(0.25, 1e-7, 50)
