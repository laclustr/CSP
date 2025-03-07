import pygame as pg

def main():
	DISPLAY_WIDTH  = 640
	DISPLAY_HEIGHT = 480
	pg.init()
	display = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
	clock = pg.time.Clock()
	suf = pg.Surface((240, 300))

	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False

		display.fill(pg.Color("#FFFFFF"))
		pg.draw.rect(
			display,
			pg.Color("#14FF21"),
			pg.Rect(100, 200, 56, 56)
		)
		pg.draw.circle(
			suf,
			pg.Color(8, 52, 88),
			(40, 40),
			40
		)
		display.blit(suf, (220, 60))
		
		pg.display.flip()

		clock.tick(60)


if __name__ == "__main__":
	main()
	pg.quit()