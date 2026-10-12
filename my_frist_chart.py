import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

walk = [962, 3452, 5135, 21249, 20464]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(walk)
for i, p in enumerate(walk):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")
ax.set_title("나의 일주일 걸음 수")
fig.savefig("my_first_chart.png")
