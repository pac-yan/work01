import random
file = open("image.ppm", "w")
file.write("P3 500 500 255\n")
num = 0
while(num < 500 * 500):
	file.write(str((num + 1) % 200) + " " + str((num + random.randint(-30, 30)) % 255) + " " + str((100 - num + 1) % 255) + " ")
	num += 1
