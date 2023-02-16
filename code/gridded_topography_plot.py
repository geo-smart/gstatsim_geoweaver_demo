import uuid
from install_dependencies import *
from plot_utilities import *
from subglacial_topography_plot import df_bed

res = 1000
df_grid, grid_matrix, rows, cols = gs.Gridding.grid_data(df_bed, 'X', 'Y', 'Bed', res)
# plot gridded bed
fig, ax = plt.subplots(1, figsize=(5,5))
im = plt.imshow(grid_matrix, cmap='gist_earth', vmin=-400, vmax=600,
                interpolation='none', origin='upper')
plt.title('Gridded topography')
plt.xlabel('X [px]'); plt.ylabel('Y [px]')

# make color bar
cbar = make_colorbar(fig, im, -400, 600, 'Bed [m]')

ax.axis('scaled')
plt.savefig(f'{uuid.uuid4().hex}.png')
# plt.show()

