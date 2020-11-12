""""DO NOT MODIFY THIS FILE FOR PROJECT 3"""

from tkinter import *

from libs.Vector import *


class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    ####################################################
    # Initialization
    ####################################################
    def __init__(self, parent, width=700, height=700, verbose=False, gui=True, **options):
        Frame.__init__(self, parent, **options)

        self._turtles = []
        self._items = {}
        self._running = 0
        self._timestamp = 0
        self._period = 10  # milliseconds
        self._verbose = verbose
        self._gui = gui
        self._canvas_offset = Vector(150, 150)

        self.runtime_period = 10  # actual time for each period

        if self._gui:
            self.canvas = Canvas(self, width=width, height=height)
            self.canvas.pack()
            parent.title("UC Berkeley CS9H Turtle Arena")
            Button(self, text='step', command=self.step).pack(side=LEFT)
            Button(self, text='run', command=self.run).pack(side=LEFT)
            Button(self, text='stop', command=self.stop).pack(side=LEFT)
            Button(self, text='quit', command=parent.quit).pack(side=LEFT)
            self.canvas.bind('<ButtonPress>', self.press)
            self.canvas.bind('<Motion>', self.motion)
            self.canvas.bind('<ButtonRelease>', self.release)
            self.width, self.height = width, height
            self.dragging, self.drag_start, self.start = (None, None, None)

    ####################################################
    # Info Gathering Methods
    ####################################################
    def get_timestamp(self):
        """Return current simulation time (in milliseconds)"""
        return self._timestamp

    def is_running(self):
        """Return if the simulation is running"""
        return self._running

    ####################################################
    # GUI Related Methods
    ####################################################
    def press(self, event):
        """Handles button press event"""
        drag_start = Vector(event.x, event.y)
        for turtle in self._turtles:
            if (drag_start - self._canvas_offset - turtle.position).length() < 10:
                self.dragging = turtle
                self.drag_start = drag_start
                self.start = turtle.position
                return

    def motion(self, event):
        """Handles drag event"""
        drag = Vector(event.x, event.y)
        if self.dragging:
            self.dragging.position = self.start + drag - self.drag_start
            self.update(self.dragging)

    def release(self, event):
        """Handles button release event"""
        self.dragging = None

    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self._items[turtle]
        vertices = [(v.x + self._canvas_offset.x, v.y + self._canvas_offset.y)
                    for v in turtle.getshape()]
        self.canvas.coords(item, sum(vertices, ()))
        self.canvas.itemconfigure(item, **turtle.style)

    ####################################################
    # Simulation Related Methods
    ####################################################
    def add(self, turtle):
        """Add a new turtle to this arena."""
        self._turtles.append(turtle)
        if self._gui:
            self._items[turtle] = self.canvas.create_polygon(0, 0)
            self.update(turtle)

    def step(self, stop=True):
        """Advance all the turtles one step."""
        next_states = {}
        self._timestamp += self._period
        for turtle in self._turtles:
            next_states[turtle] = turtle.getnextstate()
        for turtle in self._turtles:
            turtle.setstate(next_states[turtle])
            if self._gui:
                self.update(turtle)
        if stop:
            self._running = 0
        if self._verbose:
            self.track()

    def stop(self):
        """Stop the running turtles."""
        self._running = 0

    def run(self):
        """Start the turtles running."""
        self._running = 1
        self.loop()

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(False)
        if self._running:
            self.tk.createtimerhandler(self.runtime_period, self.loop)
        elif not self._gui:
            exit(0)

    def track(self):
        """Print positions for Cat and Mouse"""
        if self._timestamp % 1000 == 0:
            print("Timestamp: {} s".format(self._timestamp / 1000))
            for turtle in self._turtles:
                print('{} {}'.format(turtle.__class__.__name__, turtle.position))
            print('-' * 20)
