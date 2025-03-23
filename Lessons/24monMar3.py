import pygame as pg

def main():
	pg.init()
	display = pg.display.set_mode((640, 480))
	clock = pg.time.Clock()
	suf = pg.Surface((240, 300))

	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False

		display.fill(pg.Color(255,255,255))
		pg.draw.rect(
			display,
			pg.Color(0, 36, 28),
			pg.Rect(100, 200, 56, 56)
		)
		pg.draw.circle(
			suf,
			pg.Color(8, 52, 88),
			(20, 40),
			40
		)
		display.blit(suf, (220, 60))
		
		pg.display.flip()

		clock.tick(60)


if __name__ == "__main__":
	main()
	pg.quit()