# Week 0 — SEDS Celestia (Simulations Vertical) 🪐

Hey, and welcome to SEDS Celestia! 🎉

We're really glad you're here. SEDS Celestia is our college's chapter of Students for the Exploration and Development of Space, and the Simulations vertical is where the developers and physics nerds of the club hang out. We're the folks who get genuinely excited about building complex systems from scratch, GPU acceleration, low-level programming, heavy math, the kind of stuff that makes your laptop fan spin up. That's the energy here.

Whether you're a seasoned coder or someone who's just curious about where physics meets programming, you're in the right place. This is the start of your journey with us, and we're stoked to have you along for it.

Week 0 is your very first checkpoint before the real induction begins. No pressure, no jargon overload, just a gentle nudge to get you ready for what's coming.



## The Assignment 

You are required to implement a **bouncing ball simulation** that models one-dimensional motion under gravity with inelastic collisions against a fixed boundary.

### Physics Requirements

- **Kinematics:** The ball's position and velocity must be updated at each timestep using standard kinematic equations of motion under constant gravitational acceleration (g ≈ 9.8 m/s²).
- **Numerical Integration:** Use a discrete time-stepping method (Euler integration is sufficient for this assignment) to update velocity and position at each frame:

```
v(t + dt) = v(t) + g * dt
y(t + dt) = y(t) + v(t + dt) * dt
```

- **Collision Handling:** When the ball's position reaches the floor (i.e., `y <= 0`), the collision must be resolved by inverting the velocity and scaling it by a **coefficient of restitution** `e`, where `0 < e < 1`, to simulate energy loss on impact:

```
v = -e * v
```

- **Termination Condition:** The simulation should either run for a fixed duration or terminate once the ball's velocity falls below a defined threshold (i.e., the system has effectively come to rest).

### Implementation Requirements





This is purely a warm-up. In a few weeks you'll be building actual chaotic systems, and this assignment exists so your tools, your logic, and your understanding of basic numerical simulation are all warmed up and ready for that.

## Why This Matters 

Honestly? Because it's low-stress and kind of fun.

> Completing this gets you brownie points with the team ; and yes, we remember who showed up early.

More importantly, it gets your entire dev environment set up and battle-tested *before* the real 3-week induction series kicks off.

Using Claude, Copilot, or whatever tool you like is completely fine, we're not going to pretend that's not how people code in 2026.

But here's the catch: you need to actually understand what's happening in your code. The physics behind the bounce, the logic behind the loop, all of it. Copy-pasting without understanding defeats the entire point of this vertical.

## Next Steps ✅

- [ ] Fork or clone this repo
- [ ] Set up your dev environment (language of your choice — pick whatever you're comfortable with)
- [ ] Write your bouncing ball simulation
- [ ] Push your code before the deadline

That's genuinely all there is to it. Have fun with it, and welcome to the team. 🚀

## Contact and support

If you get stuck on the math, face a weird bug, or just need a sanity check, don't hesitate to reach out. We've split our support team based on what you're working on:
