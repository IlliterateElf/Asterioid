import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()
def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

gamewindow = pyglet.window.Window(800, 600)
cat = pyglet.resource.image('cat.jpg')
center_image(cat)
score_label = pyglet.text.Label(text="Score: 0", x=10, y=460)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=gamewindow.width//2, y=gamewindow.height//2, anchor_x='center')
player = pyglet.sprite.Sprite(img=cat, x=gamewindow.width//2, y=gamewindow.height//2 - 100)
player.update(scale=.25)



@gamewindow.event
def on_draw():
    gamewindow.clear()

    level_label.draw()
    score_label.draw()

    player.draw()

center_image(cat)

if __name__ == '__main__':
    pyglet.app.run()
