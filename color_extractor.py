import pandas as pd
import extcolors
import PIL
from PIL import Image
import matplotlib.pyplot as plt


# short formula to get hex code from rgb values
def rgb_to_hex(rgb):
    return "%02x%02x%02x" % rgb


# get the RGB colors
my_image = "test.jpg"
image = PIL.Image.open(my_image)
colors, pixels = extcolors.extract_from_image(image)

# build colors DataFrame from pandas
df = pd.DataFrame(colors)
df.columns = ["RGB colors", "pixels w/color"]
df = df.nlargest(5, "pixels w/color")

color_list = []
for item in df["RGB colors"]:
    y = "#" + f"{rgb_to_hex(item)}"
    y = y.upper()
    # print "y" for easy access to the hex code for fast use
    print(y)
    color_list.append(y)


pixel_list = list(df["pixels w/color"])

fig, ax = plt.subplots(figsize=(90, 90), dpi=10)
wedges, text, mis = ax.pie(pixel_list,
                      labels=color_list,
                      labeldistance=1.05,
                      autopct="%1.1f%%",
                      colors=color_list,
                      textprops={'fontsize': 120, 'color': 'black'}
                     )
plt.setp(wedges, width=0.3)

# create space in the center
plt.setp(wedges, width=0.36)

ax.set_aspect("equal")
fig.set_facecolor('white')
plt.show()


