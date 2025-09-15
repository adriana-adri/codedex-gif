import imageio.v3 as iio

filenames = ['pic1.png', 'pic2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
  
iio.imwrite('moving.gif', images, duration = 500, loop = 0)

