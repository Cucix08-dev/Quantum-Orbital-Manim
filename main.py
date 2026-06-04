from manim import *
import numpy as np

class QuantumOrbital(Scene):
    def construct(self):
        self.camera.background_color = "#000022"

        N = 10000  # punti probabilistici
        a0 = 1.0  # raggio di Bohr

        dots = VGroup()

        for _ in range(N):
            r = np.random.exponential(scale=1.5)
            theta = np.random.uniform(0, np.pi)
            phi = np.random.uniform(0, 2*np.pi)

            psi = (r/a0) * np.exp(-r/(2*a0)) * np.cos(theta)
            prob = psi**2

            if np.random.random() < prob * 5:
                x = r * np.sin(theta) * np.cos(phi)
                y = r * np.sin(theta) * np.sin(phi)
                z = r * np.cos(theta)

                dot = Dot3D(point=[x, y, z], radius=0.03)
                color_factor = (prob * 50) % 1
                dot.set_color(interpolate_color(BLUE, RED, color_factor))
                dots.add(dot)

        def rotate_cloud(mob, dt):
            mob.rotate(0.3 * dt, axis=UP)
            mob.rotate(0.1 * dt, axis=RIGHT)

        dots.add_updater(rotate_cloud)

        self.play(FadeIn(dots), run_time=3)
        self.wait(6)

        def warp(p):
            return p + np.array([
                0.2 * np.sin(p[1] * 2),
                0.2 * np.cos(p[0] * 2),
                0.1 * np.sin(p[2] * 3)
            ])

        self.play(dots.animate.apply_function(warp), run_time=4)
        self.wait(4)
