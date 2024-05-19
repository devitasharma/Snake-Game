# 1.TRACER-UPDATE METHOD / :----
""" In Python's turtle module, the tracer method controls the animation of drawing.
    It's part of a system for controlling the speed and appearance of turtle graphics.

    When you draw something with the turtle module,
    it typically updates the screen after each step, making the drawing process visible in real-time.
    However, this can be slow for complex drawings. The tracer method allows you to control how often
    the screen updates.

    Here's how it works:

    Enabling Tracer: By default, the tracer is enabled with a value of 1. This means that the screen will
    update after each turtle movement or action.

    python
    ----------------------------------EXAMPLE CODE----------------------------
    import turtle
    turtle.tracer(1)
    (#Disabling Tracer: You can disable the tracer completely by setting it to 0.
    This will make the turtle draw instantly without any animation.)

    python
    ----------------------------------EXAMPLE CODE------------------------
    turtle.tracer(0)
    (Customizing Tracer: You can set the tracer to any positive integer value.
    This value represents the number of turtle actions to perform before updating the screen.
    This can speed up the drawing process for complex graphics.)

    python
    ----------------------------------EXAMPLE CODE------------------------
    turtle.tracer(10)  # Update the screen after every 10 turtle actions
    (Forcing Update: If you need to force an update of the screen before the number
    of actions specified by the tracer method, you can use the update method.)

    python
    ----------------------------------EXAMPLE CODE------------------------
    turtle.update()  # Force an update of the screen
    (Here's a simple example to illustrate the usage of tracer:)

    python
    ----------------------------------EXAMPLE CODE------------------------
    import turtle

    # Enable tracer with a delay of 10 turtle actions before updating the screen
    turtle.tracer(10)

    for _ in range(36):  # Draw a circle by moving 10 degrees 36 times
        turtle.forward(100)
        turtle.left(10)

    # Update the screen manually
    turtle.update()
    turtle.done()

    Above example, the screen updates every 10 turtle actions due to the tracer(10) setting,
    making the drawing process faster."""

# 2. time.sleep method:------
"""  The time.sleep() method in Python's turtle module can be used to introduce delays in turtle graphics
     animations. It's similar to the time.sleep() function in Python's standard library, but it's specifically
     used in conjunction with turtle graphics to control the speed of animation."""






