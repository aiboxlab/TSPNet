import os

oits = os.listdir("i3d-features/span=8_stride=2")
dizs = os.listdir("i3d-features/span=16_stride=2")

for elem in oits:

	if not elem in dizs:

		print(elem)