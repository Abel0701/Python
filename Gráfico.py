import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [7, 8, 5, 3, 8]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

ax.set_title("Gráfico", fontsize = 24)
ax.set_xlabel("Valor", fontsize = 14)
ax.set_ylabel("Números", fontsize = 14)

ax.tick_params(axis = 'both', labelsize = 14)
plt.show()