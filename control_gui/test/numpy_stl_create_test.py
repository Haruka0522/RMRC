import numpy as np
from stl import mesh

# 物体の頂点を定義する
vertices = np.array([\
    [3, 0, 0],
    [0, 3, 0],
    [0, 0, 0],
    [0, 0, 3]])

# 三角形ポリゴンを構成する3つの頂点を選ぶ
faces = np.array([\
    [0,1,2],
    [0,1,3],
    [0,2,3],
    [1,2,3]])

# メッシュ（物体）作成
obj= mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        obj.vectors[i][j] = vertices[f[j],:]


#Y軸方向に90度回転
#obj.rotate([0.0, 1.0, 0.0], math.radians(90))

# 保存
obj.save('sample1.stl')
