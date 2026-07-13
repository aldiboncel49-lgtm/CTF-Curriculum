
FLAG = "[REDACTED]"
def check(password):
    return password == FLAG

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print("GRANTED" if check(sys.argv[1]) else "DENIED")
    else:
        print("Provide password")
