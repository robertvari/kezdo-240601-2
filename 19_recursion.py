def call_myself(n):
    n += 1
    print(f"Number: {n}")

    if n == 10:
        return
    
    call_myself(n)


call_myself(0)