def hanoi_solver(n):
    source = list(range(n, 0, -1))
    helper = []
    target = []
    giant = []

    def format_state():
        return f"{source} {helper} {target}"
    
    
    def real_solver(n, source, helper, target):
        if n == 1:
            dest = source.pop()
            target.append(dest)
            giant.append(format_state())
            return
        
        
        real_solver(n-1, source, target, helper)
        dest = source.pop()
        target.append(dest)
        giant.append(format_state())
        real_solver(n-1, helper, source, target)
        
        
        


    giant.append(format_state())
    real_solver(n, source, helper, target)
    return "\n".join(giant)

print(hanoi_solver(3))
