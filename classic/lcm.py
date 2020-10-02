from hcf import hcf

# LCM (Least Common Multiple)
def lcm(x, y):
    return x * y // hcf(x, y)

print(lcm(24,36))