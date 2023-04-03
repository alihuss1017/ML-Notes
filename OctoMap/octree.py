import open3d as o3d
import numpy as np

def update_vis(vis):
    # Update the colors of the voxels in the voxel grid
    vox_colors = np.random.uniform(0, 1, size=(len(vox_grid.voxel_colors), 3))
    vox_grid.colors = o3d.utility.Vector3dVector(vox_colors)
    # Redraw the voxel grid
    vis.update_geometry(vox_grid)
    # Update the visualization
    vis.poll_events()
    vis.update_renderer()

N = 2000
pcd = o3d.io.read_point_cloud("C:/Users/ali49/OneDrive/Documents/Python Scripts/PyTutorials/PyTutorials/Point Cloud/girishpointcloud.ply")
pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),center=pcd.get_center())
pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
#o3d.visualization.draw_geometries([pcd])
octree = o3d.geometry.Octree(max_depth = 8)
octree.convert_from_point_cloud(pcd, size_expand = .001)

vox_grid = octree.to_voxel_grid()
print(vox_grid.get_voxels())
o3d.visualization.draw_geometries_with_animation_callback([vox_grid], update_vis)