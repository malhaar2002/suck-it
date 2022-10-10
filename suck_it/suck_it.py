from PIL import Image, ImageDraw, ImageSequence
import io

def suck_it(name):
	im = Image.open('static/suck-it-mime.gif')

	# A list of the frames to be outputted
	frames = []
	# Loop over each frame in the animated image
	for frame in ImageSequence.Iterator(im):
		# Draw the text on the frame
		d = ImageDraw.Draw(frame)
		d.text((10,100), f"Suck it, {name}", fill=255)
		del d
		
		# However, 'frame' is still the animated image with many frames
		# It has simply been seeked to a later frame
		# For our list of frames, we only want the current frame
		
		# Saving the image without 'save_all' will turn it into a single frame image, and we can then re-open it
		# To be efficient, we will save it to a stream, rather than to file
		b = io.BytesIO()
		frame.save(b, format="GIF")
		frame = Image.open(b)
		
		# Then append the single frame image to a list of frames
		frames.append(frame)
	# Save the frames as a new image
	frames[0].save('static/out.gif', save_all=True, append_images=frames[1:])

suck_it('Malhaar')