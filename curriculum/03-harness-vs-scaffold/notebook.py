# Lesson 03 — Harness vs scaffold. Toy shipment-ETA agent, standard library only.
import random
random.seed(42)
# The truth: ETA = base transit days + a hub delay (a third of shipments hit a congested hub).
ships = [{"base": random.randint(2, 5), "delay": random.choice([0, 0, 2])} for _ in range(200)]
TIMEOUT_RATE = 0.3                                  # the live ETA lookup fails ~30% of the time
def eta_tool(s):                                    # a TOOL the agent can call
    if random.random() < TIMEOUT_RATE:
        raise TimeoutError
    return s["base"]
def model(context):                                 # toy MODEL: answers only from what it is shown
    return context["base"] + context.get("delay", 0)
def agent(s, rich_scaffold, good_harness, cache):
    base, stale = None, False
    for _ in range(3 if good_harness else 1):       # HARNESS: how many tries?
        try: base = cache["last"] = eta_tool(s); break
        except TimeoutError: pass
    if base is None:
        if good_harness:
            return "ESCALATE", False                # HARNESS: admit "I don't know"
        base, stale = cache.get("last", 3), True    # HARNESS bug: reuse someone else's ETA
    context = {"base": base}                        # SCAFFOLD: what goes into the context
    if rich_scaffold:
        context["delay"] = s["delay"]               # ...include hub status or not
    return model(context), stale
print(f"{'scaffold':9}{'harness':9}{'wrong':>7}{'escal.':>8}{'blame:scaffold':>16}{'harness':>9}")
for rich in (False, True):
    for good in (False, True):
        random.seed(7)                              # same tool luck for every setup
        wrong = esc = blame_s = blame_h = 0
        cache = {}
        for s in ships:
            ans, stale = agent(s, rich, good, cache)
            if ans == "ESCALATE":
                esc += 1
            elif ans != s["base"] + s["delay"]:
                wrong += 1
                blame_h += stale                    # a stale tool result caused it
                blame_s += (not rich and s["delay"] > 0)  # a missing fact caused it
        print(f"{'rich' if rich else 'thin':9}{'good' if good else 'naive':9}"
              f"{wrong / 2:>6.1f}%{esc / 2:>7.1f}%{blame_s:>16}{blame_h:>9}")
# 5-MINUTE TWEAK CHALLENGE
# 1. Set TIMEOUT_RATE = 0.6. Which layer now causes most of the damage?
# 2. Rich scaffold, naive harness: the context has every fact, yet ~28% are still wrong.
#    Why can no prompt change ever fix that?
# 3. Change retries from 3 to 1 but keep ESCALATE. Is "wrong" or "escalated" the better failure?
