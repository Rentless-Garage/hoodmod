import pygame

class Game():
	def __init__(self, caption: str, size: tuple[int, int]) -> None:
		pygame.init()
		self.wind = pygame.display.set_mode(size)
		pygame.display.set_caption(caption)
		self.clock = pygame.time.Clock()
		self.running = False

	def start(self) -> None:
		self.running = True
		self.main_loop()

	def main_loop(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					pygame.quit()
		self.render()
		self.clock.tick(60)

	def render(self) -> None:
		self.wind.fill("purple")
		pygame.display.flip()
